# Procesador de Expedientes de Insolvencia

Aplicación para automatizar el procesamiento de expedientes de insolvencia para Corporación Avancemos S.A.S.

## Descripción

Esta herramienta automatiza el flujo de trabajo para el procesamiento de expedientes de insolvencia, especialmente el proceso de generación de notificaciones para acreedores. La aplicación identifica automáticamente la información del deudor y el operador de insolvencia, selecciona el formato correspondiente y genera los documentos necesarios.

## Características principales

- **Selección intuitiva de expedientes** desde la ruta institucional
- **Extracción automática** de información del deudor y operador de insolvencia
- **Mapeo inteligente** de operadores con sus formatos correspondientes
- **Generación automática** de notificaciones con un solo clic
- **Interfaz gráfica moderna** y fácil de usar
- **Registro detallado** de todas las operaciones realizadas

## Instalación

### Requisitos previos

- Sistema operativo Windows 10 o superior
- Resolución de pantalla mínima: 1280x720
- Permisos de lectura/escritura en la carpeta de expedientes

### Mediante instalador

1. Ejecute el archivo `Instalador_ProcesadorExpedientes.exe`
2. Siga las instrucciones del asistente de instalación
3. Una vez completada la instalación, encontrará un acceso directo en el escritorio

### Versión portable

1. Descomprima el archivo `ProcesadorExpedientes_vX.X.X_Portable.zip` en cualquier ubicación
2. Abra la carpeta extraída
3. Ejecute el archivo `ProcesadorExpedientes.exe`

## Uso básico

1. **Configuración inicial**:
   - Al iniciar por primera vez, la aplicación utilizará por defecto la ruta institucional:
     ```
     C:\Users\Usuario\Corporacion Avancemos S.A.S\Avancemos Conciliación - Documentos\CENTRO DE CONCILIACION\Insolvencias 2025\Insolvencias 2025
     ```
   - Configure la carpeta de formatos desde la sección "Configuración de Rutas"

2. **Selección de expediente**:
   - Navegue por la lista de expedientes disponibles (se ignorarán automáticamente los que contengan "00" en el nombre)
   - Utilice el campo de búsqueda para filtrar por nombre
   - Seleccione el expediente que desea procesar

3. **Procesamiento**:
   - Para un análisis preliminar: Haga clic en "Procesar Expediente"
   - Para la automatización completa: Haga clic en "EJECUTAR AUTOMATIZACIÓN"

4. **Resultados**:
   - Los documentos generados se guardarán en la carpeta "02. NOTIFICACIONES" dentro del expediente
   - Consulte el registro de actividad para ver los detalles del proceso

## Estructura del proyecto

```
expedientes-automatizacion/
│
├── app/                            # Código fuente
│   ├── __init__.py                # Inicialización del paquete
│   ├── procesador.py              # Clase principal
│   ├── utils/                     # Utilidades
│   │   ├── __init__.py
│   │   ├── docx_helper.py         # Manipulación de documentos Word
│   │   └── logger.py              # Sistema de logging
│   └── config/                    # Configuraciones
│       ├── __init__.py
│       ├── settings.py            # Configuraciones generales
│       └── version.py             # Información de versión
│
├── data/                          # Datos y formatos
│   ├── formatos/                  # Formatos de operadores
│   ├── config.ini                 # Configuración
│   └── icon.ico                   # Ícono de la aplicación
│
├── logs/                          # Carpeta para archivos de log
│
├── run.py                         # Script principal
├── build_exe.py                   # Script para generar ejecutable
├── requirements.txt               # Dependencias
└── README.md                      # Este archivo
```

## Desarrollo

### Requisitos de desarrollo

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

### Configuración del entorno de desarrollo

1. Clonar el repositorio:
   ```
   git clone https://repositorio.empresa.com/procesador-expedientes.git
   cd procesador-expedientes
   ```

2. Crear y activar entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación en modo desarrollo:
   ```
   python run.py
   ```

### Generación del ejecutable

Para generar el ejecutable y la versión portable:

```
python build_exe.py
```

Esto creará:
- Un ejecutable `ProcesadorExpedientes.exe` en la carpeta `dist/`
- Un archivo ZIP con la versión portable

## Soporte

Para consultas o reportar problemas:

- Email: soporte@avancemosconciliacion.com
- Teléfono: 3106511303

## Licencia

© 2025 Corporación Avancemos S.A.S. Todos los derechos reservados.

Este software es confidencial y de uso exclusivo para Corporación Avancemos S.A.S. No está permitida su distribución, copia o modificación sin autorización expresa.