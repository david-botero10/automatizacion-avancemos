#!/usr/bin/env python
"""
Script principal para ejecutar la aplicación de procesamiento de expedientes.
Este script inicia la interfaz gráfica de usuario y gestiona la inicialización
de la aplicación.
"""

import os
import sys
import traceback
from pathlib import Path

# Asegurarse de que la ruta actual está en el path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Intentar importaciones con manejo de errores
try:
    # Inicializar la aplicación
    from app import init_app
    init_app()
    
    # Importar configuraciones
    from app.config import CONFIG
    from app.config.settings import UI_CONFIG, DEFAULT_PATHS
    
    # Importar módulo de logging
    from app.utils.logger import setup_logger
    
    # Importar interfaz gráfica
    import customtkinter as ctk
    from app.ui.main_window import SeleccionadorExpedientes
    
except ImportError as e:
    # Si falla alguna importación, mostrar mensaje de error y salir
    print(f"Error al iniciar la aplicación: {e}")
    print("Asegúrese de que todas las dependencias estén instaladas.")
    print("Intente ejecutar: pip install -r requirements.txt")
    sys.exit(1)

def main():
    """
    Función principal que inicia la aplicación.
    """
    # Configurar logger principal
    log_level = CONFIG.get("PROCESAMIENTO", "nivel_log", fallback="INFO")
    log_path = CONFIG.get("RUTAS", "ruta_log", fallback=os.path.join(current_dir, "logs"))
    logger = setup_logger("main", log_level, log_path)
    
    try:
        logger.info("Iniciando aplicación")
        
        # Verificar directorios necesarios
        for key, path in DEFAULT_PATHS.items():
            if "LOG" in key and not os.path.exists(path):
                logger.info(f"Creando directorio para logs: {path}")
                os.makedirs(path, exist_ok=True)
        
        # Verificar existencia de la carpeta de expedientes
        expedientes_path = CONFIG.get("RUTAS", "ruta_expedientes", fallback=DEFAULT_PATHS["EXPEDIENTES"])
        if not os.path.exists(expedientes_path):
            logger.warning(f"La carpeta de expedientes no existe: {expedientes_path}")
            # No fallamos aquí, permitimos que la interfaz gestione este caso
        
        # Configurar tema de la interfaz
        tema = CONFIG.get("INTERFAZ", "tema", fallback="system")
        ctk.set_appearance_mode(tema)
        ctk.set_default_color_theme("blue")
        
        # Iniciar interfaz gráfica
        logger.info("Iniciando interfaz gráfica")
        app = SeleccionadorExpedientes()
        
        # Configurar ventana principal
        ancho_minimo = CONFIG.getint("INTERFAZ", "ancho_minimo", fallback=800)
        alto_minimo = CONFIG.getint("INTERFAZ", "alto_minimo", fallback=600)
        app.minsize(ancho_minimo, alto_minimo)
        
        # Centrar la ventana en la pantalla
        app.update_idletasks()
        width = app.winfo_width()
        height = app.winfo_height()
        x = (app.winfo_screenwidth() // 2) - (width // 2)
        y = (app.winfo_screenheight() // 2) - (height // 2)
        app.geometry(f'{width}x{height}+{x}+{y}')
        
        # Mensaje de bienvenida en el log
        logger.info("Aplicación iniciada correctamente")
        
        # Iniciar el bucle principal de la aplicación
        app.mainloop()
        
        # Mensaje de cierre
        logger.info("Aplicación cerrada correctamente")
        
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        logger.error(traceback.format_exc())
        
        # Mostrar mensaje de error al usuario
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Error inesperado",
                f"Ha ocurrido un error inesperado al iniciar la aplicación:\n\n{str(e)}\n\n"
                "Por favor, contacte al soporte técnico."
            )
            root.destroy()
        except:
            # Si falla incluso mostrar el mensaje de error gráfico, imprimir en consola
            print(f"ERROR CRÍTICO: {str(e)}")
            print(traceback.format_exc())
        
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())