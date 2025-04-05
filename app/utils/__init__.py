"""
Paquete de utilidades para la aplicación de procesamiento de expedientes.
Contiene módulos auxiliares para tareas comunes como manipulación de documentos,
logging, y otras funcionalidades de soporte.
"""

# Importar funciones principales para facilitar su acceso
from .docx_helper import replace_text_in_doc, save_document
from .logger import setup_logger, get_logger

# Versión del paquete de utilidades
__version__ = '1.0.0'