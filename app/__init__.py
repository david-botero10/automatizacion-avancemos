"""
Paquete principal para la aplicación de procesamiento de expedientes.
Este módulo contiene las clases y utilidades principales para el procesamiento
de expedientes de insolvencia.
"""

__version__ = '1.0.0'

# Importar componentes principales para facilitar su uso
from .procesador import ProcesadorExpedientes

# Configuración inicial del paquete
import os
import sys

# Asegurar que la ruta de la aplicación esté en el path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

# Importar configuraciones
try:
    from .config.settings import DEBUG
except ImportError:
    DEBUG = False

# Inicialización
def init_app():
    """Inicializa la aplicación y verifica las dependencias necesarias."""
    # Verificar que existan las carpetas necesarias
    logs_dir = os.path.join(os.path.dirname(APP_DIR), 'logs')
    if not os.path.exists(logs_dir):
        try:
            os.makedirs(logs_dir)
        except Exception as e:
            print(f"Advertencia: No se pudo crear el directorio de logs: {e}")
    
    # Información de inicialización
    if DEBUG:
        print(f"App inicializada en: {APP_DIR}")
        print(f"Versión: {__version__}")
    
    return True