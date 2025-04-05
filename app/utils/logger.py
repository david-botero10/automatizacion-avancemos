"""
Utilidades para configurar y gestionar el sistema de logging de la aplicación.
Proporciona funciones para crear y obtener loggers con configuraciones específicas.
"""

import os
import logging
import sys
from datetime import datetime

def setup_logger(nombre="app", nivel="INFO", ruta_log=None, console=True, formato=None):
    """
    Configura y devuelve un logger con la configuración especificada.
    
    Args:
        nombre (str): Nombre del logger
        nivel (str): Nivel de logging ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        ruta_log (str): Ruta donde guardar los archivos de log (opcional)
        console (bool): Indica si se debe mostrar el log en consola
        formato (str): Formato personalizado para los mensajes de log
        
    Returns:
        logging.Logger: Logger configurado
    """
    # Convertir nivel a constante de logging
    nivel_numerico = getattr(logging, nivel.upper(), logging.INFO)
    
    # Crear logger
    logger = logging.getLogger(nombre)
    logger.setLevel(nivel_numerico)
    
    # Evitar duplicación de handlers
    if logger.handlers:
        return logger
    
    # Definir formato
    if not formato:
        formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formato)
    
    # Handler para consola
    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # Handler para archivo si se especificó ruta
    if ruta_log:
        # Crear directorio si no existe
        os.makedirs(ruta_log, exist_ok=True)
        
        # Crear nombre de archivo de log con fecha actual
        fecha = datetime.now().strftime("%Y%m%d")
        archivo_log = os.path.join(ruta_log, f"{nombre}_{fecha}.log")
        
        # Configurar file handler
        file_handler = logging.FileHandler(archivo_log, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    logger.info(f"Logger '{nombre}' configurado con nivel {nivel}")
    return logger

def get_logger(nombre="app"):
    """
    Obtiene un logger existente o crea uno nuevo.
    
    Args:
        nombre (str): Nombre del logger
        
    Returns:
        logging.Logger: Logger solicitado
    """
    logger = logging.getLogger(nombre)
    
    # Si el logger no tiene handlers, configurarlo con valores por defecto
    if not logger.handlers:
        return setup_logger(nombre)
    
    return logger

def set_log_level(logger, nivel):
    """
    Cambia el nivel de logging de un logger existente.
    
    Args:
        logger (logging.Logger or str): Logger o nombre del logger
        nivel (str): Nuevo nivel ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    """
    if isinstance(logger, str):
        logger = logging.getLogger(logger)
    
    nivel_numerico = getattr(logging, nivel.upper(), logging.INFO)
    logger.setLevel(nivel_numerico)
    
    # También actualizar el nivel en todos los handlers
    for handler in logger.handlers:
        handler.setLevel(nivel_numerico)
    
    logger.info(f"Nivel de log cambiado a {nivel}")