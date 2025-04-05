"""
Información de versión para la aplicación de procesamiento de expedientes.
Este archivo se actualiza automáticamente durante el proceso de compilación.
"""

# Versión actual de la aplicación (MAYOR.MENOR.PARCHE)
VERSION = "1.0.0"

# Fecha de compilación (se actualiza automáticamente durante la compilación)
BUILD_DATE = "2025-04-05"

# Información adicional de versión
VERSION_INFO = {
    "name": "Procesador de Expedientes de Insolvencia",
    "description": "Herramienta para automatizar el procesamiento de expedientes de insolvencia",
    "company": "Corporación Avancemos S.A.S.",
    "copyright": "© 2025 Corporación Avancemos S.A.S. Todos los derechos reservados.",
    "build_type": "release"  # 'development', 'beta', 'release'
}

def get_version_string(include_build_type=False):
    """
    Obtiene una cadena de texto con la versión formateada.
    
    Args:
        include_build_type (bool): Si es True, incluye el tipo de compilación.
        
    Returns:
        str: Cadena con la versión formateada
    """
    if include_build_type and VERSION_INFO["build_type"] != "release":
        return f"v{VERSION} ({VERSION_INFO['build_type']})"
    return f"v{VERSION}"

def get_full_version_info():
    """
    Obtiene la información completa de versión como un diccionario.
    
    Returns:
        dict: Diccionario con toda la información de versión
    """
    info = VERSION_INFO.copy()
    info.update({
        "version": VERSION,
        "build_date": BUILD_DATE,
        "version_string": get_version_string(True)
    })
    return info

# Para pruebas
if __name__ == "__main__":
    print(f"Versión: {get_version_string(True)}")
    print(f"Fecha de compilación: {BUILD_DATE}")
    print(f"Información completa: {get_full_version_info()}")