"""
Configuraciones globales para la aplicación de procesamiento de expedientes.
Incluye constantes, rutas predeterminadas y otras configuraciones.
"""

import os
import sys
from pathlib import Path

# Modo de depuración (True para desarrollo, False para producción)
DEBUG = False

# Nivel de log predeterminado
LOG_LEVEL = "INFO"

# Rutas predeterminadas
DEFAULT_PATHS = {
    # Ruta base para los expedientes
    "EXPEDIENTES": r"C:\Users\Usuario\Corporacion Avancemos S.A.S\Avancemos Conciliación - Documentos\CENTRO DE CONCILIACION\Insolvencias 2025\Insolvencias 2025",
    
    # Ruta para los formatos de operadores
    "FORMATOS": os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "formatos"),
    
    # Ruta para los logs
    "LOGS": os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs"),
    
    # Ruta para la configuración
    "CONFIG": os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "config.ini")
}

# Ajustar rutas si estamos en un entorno empaquetado con PyInstaller
if hasattr(sys, '_MEIPASS'):
    # Rutas dentro del ejecutable
    DEFAULT_PATHS.update({
        "FORMATOS": os.path.join(sys._MEIPASS, "data", "formatos"),
        "CONFIG": os.path.join(sys._MEIPASS, "data", "config.ini")
    })
    
    # Rutas en el directorio del usuario (para archivos que necesitan ser escritos)
    user_data_dir = os.path.join(str(Path.home()), "ProcesadorExpedientes")
    os.makedirs(user_data_dir, exist_ok=True)
    
    DEFAULT_PATHS.update({
        "LOGS": os.path.join(user_data_dir, "logs")
    })

# Configuración de la interfaz de usuario
UI_CONFIG = {
    # Tema predeterminado ('light', 'dark', 'system')
    "THEME": "system",
    
    # Mostrar ventana de progreso durante el procesamiento
    "SHOW_PROGRESS": True,
    
    # Mostrar resumen al finalizar el procesamiento
    "SHOW_SUMMARY": True,
    
    # Tamaño mínimo de la ventana
    "MIN_WIDTH": 800,
    "MIN_HEIGHT": 600
}

# Configuración del procesamiento de documentos
DOCUMENT_CONFIG = {
    # Extensiones válidas para archivos de expedientes
    "VALID_EXTENSIONS": [".docx"],
    
    # Nombre del archivo de aceptación (patrón)
    "ACCEPTANCE_FILE_PATTERN": "Aceptación de solicitud",
    
    # Patrones de texto para extracción de información
    "PATTERNS": {
        "DEUDOR": r'Deudora?\s*\n*\s*([A-Z\s]+)\s*\n*\s*CC No',
        "CEDULA": r'CC No\.\s*(\d+(?:\.\d+)*)',
        "RADICADO": r'Radicado:\s*([0-9-]+)',
        "OPERADOR": r'([A-Z\s]{10,}GUERRERO|[A-Z\s]{10,})'
    }
}

# Configuración para el mapeo de operadores
OPERATOR_CONFIG = {
    # Ruta al archivo JSON de mapeo
    "MAPPING_FILE": os.path.join(os.path.dirname(__file__), "operadores.json"),
    
    # Refresco automático de mapeo (en días)
    "AUTO_REFRESH": 30
}

# Configuración de notificaciones
NOTIFICATION_CONFIG = {
    # Enviar notificaciones por correo
    "EMAIL_ENABLED": False,
    
    # Servidor SMTP
    "SMTP_SERVER": "",
    "SMTP_PORT": 587,
    "SMTP_USER": "",
    "SMTP_PASSWORD": "",
    
    # Destinatarios de notificaciones
    "NOTIFICATION_RECIPIENTS": []
}