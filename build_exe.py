#!/usr/bin/env python
"""
Script para crear el ejecutable del procesador de expedientes usando PyInstaller.
Este script automatiza el proceso de compilación y empaquetado de la aplicación.
"""
import os
import sys
import shutil
import subprocess
import datetime
import configparser
from pathlib import Path

def actualizar_version():
    """
    Actualiza el archivo de versión con la fecha de compilación actual.
    
    Returns:
        tuple: (version, fecha_compilacion)
    """
    version_file = os.path.join("app", "config", "version.py")
    version = "1.0.0"  # Versión predeterminada
    
    # Leer el archivo actual para extraer la versión
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as f:
            content = f.read()
            version_match = content.split('VERSION = "')[1].split('"')[0]
            if version_match:
                version = version_match
    
    # Fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Escribir archivo actualizado
    with open(version_file, "w", encoding="utf-8") as f:
        f.write(f'''"""
Información de versión para la aplicación de procesamiento de expedientes.
Este archivo se actualiza automáticamente durante el proceso de compilación.
"""

# Versión actual de la aplicación (MAYOR.MENOR.PARCHE)
VERSION = "{version}"

# Fecha de compilación (actualizada automáticamente)
BUILD_DATE = "{fecha_actual}"

# Información adicional de versión
VERSION_INFO = {{
    "name": "Procesador de Expedientes de Insolvencia",
    "description": "Herramienta para automatizar el procesamiento de expedientes de insolvencia",
    "company": "Corporación Avancemos S.A.S.",
    "copyright": "© {datetime.datetime.now().year} Corporación Avancemos S.A.S. Todos los derechos reservados.",
    "build_type": "release"  # 'development', 'beta', 'release'
}}

def get_version_string(include_build_type=False):
    """
    Obtiene una cadena de texto con la versión formateada.
    
    Args:
        include_build_type (bool): Si es True, incluye el tipo de compilación.
        
    Returns:
        str: Cadena con la versión formateada
    """
    if include_build_type and VERSION_INFO["build_type"] != "release":
        return f"v{{VERSION}} ({{VERSION_INFO['build_type']}}"
    return f"v{{VERSION}}"

def get_full_version_info():
    """
    Obtiene la información completa de versión como un diccionario.
    
    Returns:
        dict: Diccionario con toda la información de versión
    """
    info = VERSION_INFO.copy()
    info.update({{
        "version": VERSION,
        "build_date": BUILD_DATE,
        "version_string": get_version_string(True)
    }})
    return info
''')
    
    print(f"Archivo de versión actualizado: v{version} ({fecha_actual})")
    return version, fecha_actual

def copiar_archivos_data(dist_dir):
    """
    Copia los archivos necesarios a la carpeta de distribución.
    
    Args:
        dist_dir (str): Directorio de distribución
    """
    # Crear carpeta data en dist si no existe
    dist_data = os.path.join(dist_dir, "data")
    dist_formatos = os.path.join(dist_data, "formatos")
    
    os.makedirs(dist_data, exist_ok=True)
    os.makedirs(dist_formatos, exist_ok=True)
    
    # Copiar config.ini a la carpeta dist/data
    config_src = os.path.join("data", "config.ini")
    if os.path.exists(config_src):
        shutil.copy(config_src, os.path.join(dist_data, "config.ini"))
        print(f"Copiado archivo de configuración: {config_src}")
    
    # Copiar ícono si existe
    icon_src = os.path.join("data", "icon.ico")
    if os.path.exists(icon_src):
        shutil.copy(icon_src, os.path.join(dist_data, "icon.ico"))
        print(f"Copiado archivo de ícono: {icon_src}")
    
    # Copiar formatos a la carpeta dist/data/formatos
    formatos_path = os.path.join("data", "formatos")
    if os.path.exists(formatos_path):
        for archivo in os.listdir(formatos_path):
            if archivo.endswith(".docx"):
                shutil.copy(
                    os.path.join(formatos_path, archivo), 
                    os.path.join(dist_formatos, archivo)
                )
        print(f"Copiados {len(os.listdir(dist_formatos))} formatos a la carpeta de distribución.")
    else:
        print(f"Advertencia: No se encontró la carpeta de formatos en {formatos_path}")

def crear_ejecutable(nombre_app, version):
    """
    Crea el ejecutable usando PyInstaller.
    
    Args:
        nombre_app (str): Nombre de la aplicación
        version (str): Versión de la aplicación
        
    Returns:
        bool: True si la compilación fue exitosa, False en caso contrario
    """
    try:
        # Verificar si existe ícono
        icon_path = os.path.join("data", "icon.ico")
        icon_param = f"--icon={icon_path}" if os.path.exists(icon_path) else ""
        
        # Versión para el ejecutable
        file_version = version.replace(".", ",") + ",0"
        
        # Crear el ejecutable con PyInstaller
        cmd = [
            sys.executable, 
            "-m", 
            "PyInstaller",
            f"--name={nombre_app}",
            "--onefile",
            "--windowed",
            "--clean",
            f"--add-data=app;app",
            f"--add-data=data;data",
            icon_param,
            f"--version-file=file_version_info.txt",
            "run.py"
        ]
        
        print("Ejecutando PyInstaller...")
        print(" ".join(cmd))
        
        subprocess.run(cmd, check=True)
        
        print("\n¡Compilación exitosa!")
        print(f"El ejecutable se encuentra en: {os.path.abspath(os.path.join('dist', nombre_app + '.exe'))}")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Error al generar el ejecutable: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

def crear_archivo_version(version, fecha_compilacion):
    """
    Crea el archivo de información de versión para Windows.
    
    Args:
        version (str): Versión de la aplicación
        fecha_compilacion (str): Fecha de compilación
    """
    # Convertir versión a formato de Windows
    partes_version = version.split(".")
    while len(partes_version) < 4:
        partes_version.append("0")
    
    version_win = ",".join(partes_version)
    version_str = ".".join(partes_version)
    
    # Obtener año actual
    año_actual = datetime.datetime.now().year
    
    # Crear archivo de información de versión
    with open("file_version_info.txt", "w", encoding="utf-8") as f:
        f.write(f"""# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=({version_win}),
    prodvers=({version_win}),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x40004,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Corporación Avancemos S.A.S.'),
        StringStruct(u'FileDescription', u'Procesador de Expedientes de Insolvencia'),
        StringStruct(u'FileVersion', u'{version_str}'),
        StringStruct(u'InternalName', u'ProcesadorExpedientes'),
        StringStruct(u'LegalCopyright', u'© {año_actual} Corporación Avancemos S.A.S. Todos los derechos reservados.'),
        StringStruct(u'OriginalFilename', u'ProcesadorExpedientes.exe'),
        StringStruct(u'ProductName', u'Procesador de Expedientes'),
        StringStruct(u'ProductVersion', u'{version_str} ({fecha_compilacion})'),
        StringStruct(u'Comments', u'Desarrollado para Corporación Avancemos S.A.S.')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
""")
    print("Archivo de información de versión creado.")

def crear_portable_zip(nombre_app, version):
    """
    Crea una versión portable en formato ZIP.
    
    Args:
        nombre_app (str): Nombre de la aplicación
        version (str): Versión de la aplicación
    """
    try:
        # Nombre de archivo ZIP
        zip_name = f"{nombre_app}_v{version}_Portable"
        
        # Directorio de distribución
        dist_dir = "dist"
        
        # Crear directorio temporal para versión portable
        portable_dir = os.path.join(dist_dir, zip_name)
        os.makedirs(portable_dir, exist_ok=True)
        
        # Copiar el ejecutable
        shutil.copy(
            os.path.join(dist_dir, f"{nombre_app}.exe"),
            os.path.join(portable_dir, f"{nombre_app}.exe")
        )
        
        # Crear y copiar README para versión portable
        with open(os.path.join(portable_dir, "LEEME.txt"), "w", encoding="utf-8") as f:
            f.write(f"""PROCESADOR DE EXPEDIENTES DE INSOLVENCIA - VERSIÓN PORTABLE
==================================================
Versión: {version}
Fecha: {datetime.datetime.now().strftime("%d/%m/%Y")}

Esta es la versión portable de la aplicación "Procesador de Expedientes".

INSTRUCCIONES:
1. No es necesario instalar. Simplemente ejecute el archivo "{nombre_app}.exe".
2. La primera vez que ejecute la aplicación, deberá configurar las rutas de expedientes y formatos.
3. Los archivos de log se guardarán en una carpeta "logs" dentro del directorio donde se ejecute la aplicación.

SOPORTE:
Para cualquier consulta o asistencia técnica, contacte a:
Email: soporte@avancemosconciliacion.com
Teléfono: 3106511303

© {datetime.datetime.now().year} Corporación Avancemos S.A.S. Todos los derechos reservados.
""")
        
        # Crear archivo ZIP
        shutil.make_archive(os.path.join(dist_dir, zip_name), "zip", dist_dir, zip_name)
        
        # Eliminar directorio temporal
        shutil.rmtree(portable_dir)
        
        print(f"Versión portable creada: {os.path.abspath(os.path.join(dist_dir, zip_name + '.zip'))}")
        return True
    
    except Exception as e:
        print(f"Error al crear versión portable: {e}")
        return False

def main():
    """
    Función principal para la creación del ejecutable.
    """
    print("===== GENERADOR DE EJECUTABLE - PROCESADOR DE EXPEDIENTES =====")
    print(f"Fecha y hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("==============================================================\n")
    
    # Nombre de la aplicación
    nombre_app = "ProcesadorExpedientes"
    
    # Verificar requisitos
    try:
        # Verificar que PyInstaller esté instalado
        subprocess.run([sys.executable, "-m", "pip", "show", "pyinstaller"], 
                       check=True, 
                       stdout=subprocess.PIPE, 
                       stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("PyInstaller no está instalado. Instalando...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
            print("PyInstaller instalado correctamente.")
        except subprocess.CalledProcessError:
            print("Error al instalar PyInstaller. Verifique su conexión a internet.")
            return 1
    
    # Limpiar carpeta dist si existe
    if os.path.exists("dist"):
        shutil.rmtree("dist")
        print("Carpeta dist limpiada.")
    
    # Crear carpeta dist
    os.makedirs("dist")
    
    # Actualizar versión
    version, fecha_compilacion = actualizar_version()
    
    # Crear archivo de información de versión para Windows
    crear_archivo_version(version, fecha_compilacion)
    
    # Copiar archivos de datos
    copiar_archivos_data("dist")
    
    # Crear ejecutable
    if not crear_ejecutable(nombre_app, version):
        print("Error al crear el ejecutable. Abortando.")
        return 1
    
    # Crear versión portable
    crear_portable_zip(nombre_app, version)
    
    # Limpiar archivos temporales
    if os.path.exists("file_version_info.txt"):
        os.remove("file_version_info.txt")
    
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    if os.path.exists(f"{nombre_app}.spec"):
        os.remove(f"{nombre_app}.spec")
    
    print("\n==============================================================")
    print("PROCESO COMPLETADO")
    print("==============================================================")
    print(f"Versión generada: {version} ({fecha_compilacion})")
    print(f"Ejecutable: dist/{nombre_app}.exe")
    print(f"Versión portable: dist/{nombre_app}_v{version}_Portable.zip")
    print("==============================================================")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())