"""
Paquete de configuración para la aplicación de procesamiento de expedientes.
Contiene módulos y variables para la configuración global de la aplicación.
"""

import os
import sys
import configparser
from pathlib import Path

# Importar configuraciones principales
from .settings import DEBUG, LOG_LEVEL, DEFAULT_PATHS
try:
    from .version import VERSION
except ImportError:
    VERSION = '1.0.0'  # Versión por defecto

def load_config(config_file=None):
    """
    Carga la configuración desde un archivo .ini
    
    Args:
        config_file (str): Ruta al archivo de configuración. Si es None,
                          se busca en ubicaciones predeterminadas.
    
    Returns:
        configparser.ConfigParser: Objeto con la configuración cargada
    """
    config = configparser.ConfigParser()
    
    # Si no se especificó un archivo, buscar en ubicaciones predeterminadas
    if not config_file:
        # Posibles ubicaciones del archivo config.ini
        possible_locations = [
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'config.ini'),
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'config.ini'),
            os.path.join(str(Path.home()), 'ProcesadorExpedientes', 'config.ini')
        ]
        
        # Si estamos en un entorno empaquetado con PyInstaller
        if hasattr(sys, '_MEIPASS'):
            possible_locations.insert(0, os.path.join(sys._MEIPASS, 'data', 'config.ini'))
        
        # Buscar en cada ubicación
        for location in possible_locations:
            if os.path.exists(location):
                config_file = location
                break
    
    # Si encontramos un archivo de configuración, cargarlo
    if config_file and os.path.exists(config_file):
        config.read(config_file)
    
    return config

# Cargar configuración inicial
CONFIG = load_config()