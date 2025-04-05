#!/usr/bin/env python
"""
Módulo que contiene la ventana principal de la aplicación para la selección
y procesamiento de expedientes.
"""

import os
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter as ctk
from app.config import CONFIG
from app.config.settings import DEFAULT_PATHS
from app.utils.logger import get_logger

class SeleccionadorExpedientes(ctk.CTk):
    """
    Ventana principal de la aplicación que permite seleccionar y procesar expedientes.
    """
    
    def __init__(self):
        """
        Inicializa la ventana principal de la aplicación.
        """
        super().__init__()
        
        # Obtener logger
        self.logger = get_logger("ui")
        
        # Configurar ventana
        self.title("Procesador de Expedientes")
        self.geometry("800x600")
        
        # Definir variables
        self.ruta_expedientes = tk.StringVar(value=CONFIG.get(
            "RUTAS", "ruta_expedientes", 
            fallback=DEFAULT_PATHS["EXPEDIENTES"]
        ))
        
        # Crear interfaz
        self._crear_interfaz()
        
        self.logger.info("Interfaz gráfica inicializada")
    
    def _crear_interfaz(self):
        """
        Crea los componentes de la interfaz gráfica.
        """
        # Crear frame principal con padding
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = ctk.CTkLabel(
            main_frame, 
            text="Procesador de Expedientes", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo.pack(pady=10)
        
        # Frame para seleccionar ruta de expedientes
        ruta_frame = ctk.CTkFrame(main_frame)
        ruta_frame.pack(fill=tk.X, padx=10, pady=10)
        
        lbl_ruta = ctk.CTkLabel(ruta_frame, text="Ruta de expedientes:")
        lbl_ruta.pack(side=tk.LEFT, padx=5)
        
        entry_ruta = ctk.CTkEntry(ruta_frame, textvariable=self.ruta_expedientes, width=400)
        entry_ruta.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        btn_examinar = ctk.CTkButton(
            ruta_frame, 
            text="Examinar", 
            command=self._seleccionar_ruta_expedientes
        )
        btn_examinar.pack(side=tk.RIGHT, padx=5)
        
        # Mensaje informativo
        info_label = ctk.CTkLabel(
            main_frame,
            text="Seleccione la carpeta que contiene los expedientes a procesar y luego haga clic en 'Procesar'.",
            wraplength=780
        )
        info_label.pack(pady=10)
        
        # Botón de procesar
        btn_procesar = ctk.CTkButton(
            main_frame,
            text="Procesar Expedientes",
            command=self._procesar_expedientes,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn_procesar.pack(pady=20)
    
    def _seleccionar_ruta_expedientes(self):
        """
        Abre un diálogo para seleccionar la carpeta de expedientes.
        """
        ruta = filedialog.askdirectory(
            title="Seleccionar carpeta de expedientes",
            initialdir=self.ruta_expedientes.get()
        )
        if ruta:
            self.ruta_expedientes.set(ruta)
            self.logger.info(f"Ruta de expedientes seleccionada: {ruta}")
    
    def _procesar_expedientes(self):
        """
        Inicia el procesamiento de los expedientes en la ruta seleccionada.
        """
        ruta = self.ruta_expedientes.get()
        if not ruta or not os.path.exists(ruta):
            messagebox.showerror(
                "Error",
                "La ruta de expedientes seleccionada no existe. Por favor seleccione una ruta válida."
            )
            return
        
        self.logger.info(f"Iniciando procesamiento de expedientes en: {ruta}")
        
        # Aquí se implementará la lógica de procesamiento de expedientes
        # Por ahora solo mostramos un mensaje
        messagebox.showinfo(
            "Información",
            "El procesamiento de expedientes se implementará en la próxima versión."
        ) 