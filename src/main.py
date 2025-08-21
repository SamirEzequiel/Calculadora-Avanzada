import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from calculadora import Calculadora
from utils import Configuracion, GestorHistorial, GestorMemoria, formatear_numero
import math
import re
import threading
import time

class CalculadoraProfesional:
    def __init__(self):
        # Configurar tema ANTES de crear la ventana (más rápido)
        self._configurar_tema_inicial()
        
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Calculadora Profesional Avanzada")
        self.root.geometry("500x700")
        self.root.resizable(True, True)
        self.root.minsize(400, 600)
        
        # Variables de estado
        self.expresion = ""
        self.resultado_anterior = ""
        self.modo_cientifico = False
        self.angulo_en_radianes = False
        self.cargando = True
        
        # Configurar grid principal para responsividad
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=3)  # Área de botones
        self.root.grid_rowconfigure(3, weight=1)  # Historial
        
        # Crear interfaz básica primero
        self._crear_interfaz_basica()
        
        # Cargar configuración y datos en segundo plano
        self._cargar_datos_background()
        
        # Configurar atajos
        self._configurar_atajos()
        
        # Marcar como cargada
        self.cargando = False
        
        self.root.mainloop()
    
    def _configurar_tema_inicial(self):
        """Configura el tema inicial de forma rápida"""
        try:
            # Cargar configuración mínima
            import json
            import os
            if os.path.exists("config.json"):
                with open("config.json", 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    tema = config.get("tema", "dark")
            else:
                tema = "dark"
            
            ctk.set_appearance_mode(tema)
            ctk.set_default_color_theme("blue")
        except:
            # Fallback rápido
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
    
    def _crear_interfaz_basica(self):
        """Crea la interfaz básica de forma rápida"""
        # Pantalla básica
        self._crear_pantalla_basica()
        
        # Botones básicos
        self._crear_botones_basicos()
        
        # Historial básico
        self._crear_historial_basico()
    
    def _crear_pantalla_basica(self):
        """Crea la pantalla básica"""
        pantalla_frame = ctk.CTkFrame(self.root)
        pantalla_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        pantalla_frame.grid_columnconfigure(0, weight=1)
        
        # Pantalla principal
        self.display = ctk.CTkEntry(
            pantalla_frame, 
            font=("Consolas", 24, "bold"),
            justify="right",
            height=50
        )
        self.display.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        
        # Pantalla secundaria
        self.display_secundario = ctk.CTkEntry(
            pantalla_frame,
            font=("Consolas", 12),
            justify="right",
            height=30,
            fg_color="transparent"
        )
        self.display_secundario.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))
        
        # Info memoria
        self.info_memoria = ctk.CTkLabel(
            pantalla_frame,
            text="",
            font=("Arial", 10),
            text_color="gray"
        )
        self.info_memoria.grid(row=2, column=0, sticky="w", padx=10, pady=(0, 5))
    
    def _crear_botones_basicos(self):
        """Crea los botones básicos de forma optimizada"""
        botones_frame = ctk.CTkFrame(self.root)
        botones_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        botones_frame.grid_columnconfigure(0, weight=1)
        botones_frame.grid_rowconfigure(0, weight=1)
        
        # Frame interno para botones
        self.grid_frame = ctk.CTkFrame(botones_frame)
        self.grid_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # Configurar grid
        for i in range(8):
            self.grid_frame.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.grid_frame.grid_columnconfigure(i, weight=1)
        
        # Crear botones básicos (solo los esenciales)
        self._crear_botones_esenciales()
    
    def _crear_botones_esenciales(self):
        """Crea solo los botones esenciales para carga rápida"""
        # Botones esenciales (números y operaciones básicas)
        botones_esenciales = [
            # Fila 3 - Números y operaciones
            ("7", 3, 0, "#2C3E50"), ("8", 3, 1, "#2C3E50"), ("9", 3, 2, "#2C3E50"),
            ("÷", 3, 3, "#E74C3C"), ("C", 3, 4, "#E67E22"), ("⌫", 3, 5, "#E67E22"),
            
            # Fila 4 - Números y operaciones
            ("4", 4, 0, "#2C3E50"), ("5", 4, 1, "#2C3E50"), ("6", 4, 2, "#2C3E50"),
            ("×", 4, 3, "#E74C3C"), ("(", 4, 4, "#9B59B6"), (")", 4, 5, "#9B59B6"),
            
            # Fila 5 - Números y operaciones
            ("1", 5, 0, "#2C3E50"), ("2", 5, 1, "#2C3E50"), ("3", 5, 2, "#2C3E50"),
            ("-", 5, 3, "#E74C3C"), ("π", 5, 4, "#9B59B6"), ("e", 5, 5, "#9B59B6"),
            
            # Fila 6 - Números y operaciones
            ("0", 6, 0, "#2C3E50"), (".", 6, 1, "#2C3E50"), ("±", 6, 2, "#2C3E50"),
            ("+", 6, 3, "#E74C3C"), ("=", 6, 4, "#27AE60", 2), ("", 6, 5, "transparent"),
        ]
        
        # Crear botones esenciales
        for (texto, fila, col, color, *args) in botones_esenciales:
            if texto == "":
                continue
                
            colspan = args[0] if args else 1
            
            btn = ctk.CTkButton(
                self.grid_frame,
                text=texto,
                font=("Arial", 14, "bold"),
                fg_color=color,
                height=40,
                command=lambda t=texto: self._click_boton(t)
            )
            btn.grid(row=fila, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
        
        # Crear botones adicionales después de la carga
        self.root.after(100, self._crear_botones_completos)
    
    def _crear_botones_completos(self):
        """Crea todos los botones después de la carga inicial"""
        if self.cargando:
            return
        
        # Botones de memoria
        botones_memoria = [
            ("MC", 0, 0, "#FF6B6B"), ("MR", 0, 1, "#FF6B6B"), ("M+", 0, 2, "#FF6B6B"), 
            ("M-", 0, 3, "#FF6B6B"), ("MS", 0, 4, "#FF6B6B"), ("M^", 0, 5, "#FF6B6B"),
        ]
        
        # Botones científicos básicos
        botones_cientificos = [
            ("sin", 1, 0, "#4ECDC4"), ("cos", 1, 1, "#4ECDC4"), ("tan", 1, 2, "#4ECDC4"),
            ("log", 1, 3, "#4ECDC4"), ("ln", 1, 4, "#4ECDC4"), ("√", 1, 5, "#4ECDC4"),
        ]
        
        # Botones adicionales
        botones_adicionales = [
            ("x²", 2, 0, "#45B7D1"), ("x³", 2, 1, "#45B7D1"), ("x^y", 2, 2, "#45B7D1"),
            ("1/x", 2, 3, "#45B7D1"), ("|x|", 2, 4, "#45B7D1"), ("n!", 2, 5, "#45B7D1"),
        ]
        
        # Botones de control
        botones_control = [
            ("CE", 7, 0, "#E67E22"), ("%", 7, 1, "#9B59B6"), ("EXP", 7, 2, "#9B59B6"),
            ("RAD", 7, 3, "#9B59B6"), ("DEG", 7, 4, "#9B59B6"), ("", 7, 5, "transparent")
        ]
        
        # Crear todos los botones
        todos_botones = botones_memoria + botones_cientificos + botones_adicionales + botones_control
        
        for (texto, fila, col, color) in todos_botones:
            if texto == "":
                continue
                
            btn = ctk.CTkButton(
                self.grid_frame,
                text=texto,
                font=("Arial", 14, "bold"),
                fg_color=color,
                height=40,
                command=lambda t=texto: self._click_boton(t)
            )
            btn.grid(row=fila, column=col, padx=2, pady=2, sticky="nsew")
        
        # Crear menú después
        self.root.after(50, self._crear_menu)
    
    def _crear_menu(self):
        """Crea la barra de menú superior"""
        menu_frame = ctk.CTkFrame(self.root, height=50)
        menu_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        menu_frame.grid_columnconfigure(1, weight=1)
        
        # Botón modo científico
        self.btn_cientifico = ctk.CTkButton(
            menu_frame, 
            text="BÁSICA", 
            width=100,
            height=35,
            command=self._toggle_modo_cientifico
        )
        self.btn_cientifico.grid(row=0, column=0, padx=5, pady=5)
        
        # Botón tema
        self.btn_tema = ctk.CTkButton(
            menu_frame, 
            text="🌙", 
            width=50,
            height=35,
            command=self._toggle_tema
        )
        self.btn_tema.grid(row=0, column=2, padx=5, pady=5)
        
        # Botón configuración
        btn_config = ctk.CTkButton(
            menu_frame, 
            text="⚙️", 
            width=50,
            height=35,
            command=self._mostrar_configuracion
        )
        btn_config.grid(row=0, column=3, padx=5, pady=5)
        
        # Actualizar icono del tema
        self._actualizar_icono_tema()
    
    def _crear_historial_basico(self):
        """Crea el historial básico"""
        historial_frame = ctk.CTkFrame(self.root)
        historial_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
        historial_frame.grid_columnconfigure(0, weight=1)
        
        # Título del historial
        titulo_historial = ctk.CTkLabel(
            historial_frame,
            text="📋 Historial de Cálculos",
            font=("Arial", 12, "bold")
        )
        titulo_historial.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        # Área de historial
        self.historial_text = ctk.CTkTextbox(
            historial_frame,
            height=100,
            font=("Consolas", 10)
        )
        self.historial_text.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        
        # Crear botones de historial después
        self.root.after(100, self._crear_botones_historial)
    
    def _crear_botones_historial(self):
        """Crea los botones del historial"""
        historial_frame = self.historial_text.master
        
        # Frame para botones de historial
        btn_historial_frame = ctk.CTkFrame(historial_frame)
        btn_historial_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        btn_historial_frame.grid_columnconfigure(0, weight=1)
        btn_historial_frame.grid_columnconfigure(1, weight=1)
        btn_historial_frame.grid_columnconfigure(2, weight=1)
        
        # Botones de historial
        ctk.CTkButton(
            btn_historial_frame,
            text="🗑️ Limpiar",
            command=self._limpiar_historial,
            height=30
        ).grid(row=0, column=0, padx=5, pady=5)
        
        ctk.CTkButton(
            btn_historial_frame,
            text="💾 Exportar",
            command=self._exportar_historial,
            height=30
        ).grid(row=0, column=1, padx=5, pady=5)
        
        ctk.CTkButton(
            btn_historial_frame,
            text="🔍 Buscar",
            command=self._buscar_historial,
            height=30
        ).grid(row=0, column=2, padx=5, pady=5)
    
    def _cargar_datos_background(self):
        """Carga los datos en segundo plano"""
        def cargar_datos():
            try:
                # Cargar configuración
                self.config = Configuracion()
                
                # Cargar historial
                self.historial = GestorHistorial()
                
                # Cargar memoria
                self.memoria = GestorMemoria()
                
                # Crear calculadora
                self.calc = Calculadora()
                
                # Actualizar historial
                self.root.after(0, self._actualizar_historial)
                
                # Configurar redimensionamiento
                self.root.after(0, lambda: self.root.bind("<Configure>", self._on_resize))
                
            except Exception as e:
                print(f"Error cargando datos: {e}")
        
        # Ejecutar en hilo separado
        threading.Thread(target=cargar_datos, daemon=True).start()
    
    def _on_resize(self, event):
        """Maneja el redimensionamiento de la ventana (optimizado)"""
        if self.cargando:
            return
            
        # Evitar múltiples llamadas
        if hasattr(self, '_resize_timer'):
            self.root.after_cancel(self._resize_timer)
        
        self._resize_timer = self.root.after(100, lambda: self._actualizar_tamanos(event.width, event.height))
    
    def _actualizar_tamanos(self, width, height):
        """Actualiza los tamaños de forma optimizada"""
        # Fuente del display principal
        if width < 450:
            self.display.configure(font=("Consolas", 18, "bold"))
        elif width < 600:
            self.display.configure(font=("Consolas", 22, "bold"))
        else:
            self.display.configure(font=("Consolas", 24, "bold"))
        
        # Fuente del display secundario
        if width < 450:
            self.display_secundario.configure(font=("Consolas", 10))
        else:
            self.display_secundario.configure(font=("Consolas", 12))
        
        # Altura de botones
        if height < 700:
            button_height = 35
            font_size = 12
        elif height < 900:
            button_height = 40
            font_size = 14
        else:
            button_height = 45
            font_size = 16
        
        # Actualizar botones (solo si es necesario)
        for child in self.grid_frame.winfo_children():
            if isinstance(child, ctk.CTkButton):
                child.configure(height=button_height, font=("Arial", font_size, "bold"))
    
    def _click_boton(self, valor):
        """Maneja el clic en los botones"""
        if self.cargando:
            return
            
        if valor in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            self._agregar_numero(valor)
        elif valor in ["+", "-", "×", "÷", "(", ")", "^"]:
            self._agregar_operador(valor)
        elif valor == "=":
            self._calcular()
        elif valor == "C":
            self._limpiar()
        elif valor == "CE":
            self._limpiar_entrada()
        elif valor == "⌫":
            self._borrar_ultimo()
        elif valor == "±":
            self._cambiar_signo()
        elif valor in ["sin", "cos", "tan", "log", "ln", "√", "x²", "x³", "x^y", "1/x", "|x|", "n!", "asin", "acos", "atan", "sinh", "cosh", "tanh"]:
            self._funcion_cientifica(valor)
        elif valor in ["MC", "MR", "M+", "M-", "MS", "M^"]:
            self._gestionar_memoria(valor)
        elif valor in ["π", "e"]:
            self._agregar_constante(valor)
        elif valor in ["RAD", "DEG"]:
            self._cambiar_unidad_angulo(valor)
        elif valor == "%":
            self._calcular_porcentaje()
        elif valor == "EXP":
            self._agregar_exponente()
    
    def _agregar_numero(self, numero):
        """Agrega un número a la expresión"""
        self.expresion += numero
        self._actualizar_display()
    
    def _agregar_operador(self, operador):
        """Agrega un operador a la expresión"""
        # Mapear símbolos de operadores
        mapeo = {"×": "*", "÷": "/", "^": "**"}
        operador_real = mapeo.get(operador, operador)
        
        # Evitar operadores consecutivos
        if self.expresion and self.expresion[-1] not in "+-*/^(":
            self.expresion += operador_real
            self._actualizar_display()
        elif operador in "(":
            self.expresion += operador_real
            self._actualizar_display()
    
    def _funcion_cientifica(self, funcion):
        """Maneja funciones científicas"""
        try:
            if not hasattr(self, 'calc'):
                return
                
            valor_actual = float(self.display.get() or "0")
            
            if funcion == "sin":
                resultado = self.calc.seno(valor_actual)
            elif funcion == "cos":
                resultado = self.calc.coseno(valor_actual)
            elif funcion == "tan":
                resultado = self.calc.tangente(valor_actual)
            elif funcion == "asin":
                resultado = self.calc.arcoseno(valor_actual)
            elif funcion == "acos":
                resultado = self.calc.arcocoseno(valor_actual)
            elif funcion == "atan":
                resultado = self.calc.arcotangente(valor_actual)
            elif funcion == "sinh":
                resultado = self.calc.seno_hiperbolico(valor_actual)
            elif funcion == "cosh":
                resultado = self.calc.coseno_hiperbolico(valor_actual)
            elif funcion == "tanh":
                resultado = self.calc.tangente_hiperbolica(valor_actual)
            elif funcion == "log":
                resultado = self.calc.logaritmo_base_10(valor_actual)
            elif funcion == "ln":
                resultado = self.calc.logaritmo_natural(valor_actual)
            elif funcion == "√":
                resultado = self.calc.raiz_cuadrada(valor_actual)
            elif funcion == "x²":
                resultado = valor_actual ** 2
            elif funcion == "x³":
                resultado = valor_actual ** 3
            elif funcion == "1/x":
                resultado = 1 / valor_actual if valor_actual != 0 else "Error"
            elif funcion == "|x|":
                resultado = self.calc.valor_absoluto(valor_actual)
            elif funcion == "n!":
                resultado = self.calc.factorial(valor_actual)
            
            if resultado != "Error":
                self.expresion = str(resultado)
                self._actualizar_display()
                self._agregar_al_historial(f"{funcion}({valor_actual})", resultado)
            else:
                messagebox.showerror("Error", "Operación no válida")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error en función {funcion}: {str(e)}")
    
    def _gestionar_memoria(self, operacion):
        """Gestiona las operaciones de memoria"""
        try:
            if not hasattr(self, 'memoria'):
                return
                
            valor_actual = float(self.display.get() or "0")
            
            if operacion == "MC":  # Memory Clear
                self.memoria.limpiar_memoria()
            elif operacion == "MR":  # Memory Recall
                valor_memoria = self.memoria.obtener_memoria("M1")
                self.expresion = str(valor_memoria)
                self._actualizar_display()
            elif operacion == "M+":  # Memory Add
                self.memoria.sumar_memoria("M1", valor_actual)
            elif operacion == "M-":  # Memory Subtract
                self.memoria.restar_memoria("M1", valor_actual)
            elif operacion == "MS":  # Memory Store
                self.memoria.establecer_memoria("M1", valor_actual)
            elif operacion == "M^":  # Memory View
                self._mostrar_memorias()
            
            self._actualizar_info_memoria()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en memoria: {str(e)}")
    
    def _agregar_constante(self, constante):
        """Agrega una constante matemática"""
        if not hasattr(self, 'calc'):
            return
            
        if constante == "π":
            self.expresion += str(self.calc.obtener_pi())
        elif constante == "e":
            self.expresion += str(self.calc.obtener_e())
        self._actualizar_display()
    
    def _cambiar_unidad_angulo(self, unidad):
        """Cambia entre radianes y grados"""
        if unidad == "RAD":
            self.angulo_en_radianes = True
            # Actualizar botón si existe
            for child in self.grid_frame.winfo_children():
                if isinstance(child, ctk.CTkButton) and child.cget("text") in ["RAD", "DEG"]:
                    child.configure(text="RAD")
        else:
            self.angulo_en_radianes = False
            # Actualizar botón si existe
            for child in self.grid_frame.winfo_children():
                if isinstance(child, ctk.CTkButton) and child.cget("text") in ["RAD", "DEG"]:
                    child.configure(text="DEG")
    
    def _calcular_porcentaje(self):
        """Calcula el porcentaje"""
        try:
            valor = float(self.display.get() or "0")
            resultado = valor / 100
            self.expresion = str(resultado)
            self._actualizar_display()
        except:
            messagebox.showerror("Error", "Error al calcular porcentaje")
    
    def _agregar_exponente(self):
        """Agrega notación científica"""
        self.expresion += "e"
        self._actualizar_display()
    
    def _calcular(self):
        """Calcula el resultado de la expresión"""
        try:
            if not self.expresion:
                return
            
            # Reemplazar símbolos de operadores
            expr = self.expresion.replace("×", "*").replace("÷", "/")
            
            # Evaluar la expresión
            resultado = eval(expr)
            
            # Formatear resultado
            if hasattr(self, 'config'):
                decimales = self.config.obtener("decimales", 6)
            else:
                decimales = 6
                
            resultado_formateado = formatear_numero(resultado, decimales)
            
            # Actualizar displays
            self.display.delete(0, "end")
            self.display.insert(0, resultado_formateado)
            self.display_secundario.delete(0, "end")
            self.display_secundario.insert(0, self.expresion)
            
            # Agregar al historial
            self._agregar_al_historial(self.expresion, resultado_formateado)
            
            # Actualizar expresión
            self.expresion = str(resultado)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")
            self.expresion = ""
            self._actualizar_display()
    
    def _limpiar(self):
        """Limpia todo"""
        self.expresion = ""
        self.display.delete(0, "end")
        self.display_secundario.delete(0, "end")
    
    def _limpiar_entrada(self):
        """Limpia solo la entrada actual"""
        self.expresion = ""
        self.display.delete(0, "end")
    
    def _borrar_ultimo(self):
        """Borra el último carácter"""
        self.expresion = self.expresion[:-1]
        self._actualizar_display()
    
    def _cambiar_signo(self):
        """Cambia el signo del número actual"""
        try:
            valor = float(self.display.get() or "0")
            nuevo_valor = -valor
            self.expresion = str(nuevo_valor)
            self._actualizar_display()
        except:
            pass
    
    def _actualizar_display(self):
        """Actualiza la pantalla principal"""
        self.display.delete(0, "end")
        self.display.insert(0, self.expresion)
    
    def _actualizar_info_memoria(self):
        """Actualiza la información de memoria"""
        if not hasattr(self, 'memoria'):
            return
            
        memorias = self.memoria.obtener_todas_memorias()
        info = " | ".join([f"{k}: {v}" for k, v in memorias.items() if v != 0])
        self.info_memoria.configure(text=info if info else "")
    
    def _agregar_al_historial(self, expresion, resultado):
        """Agrega un cálculo al historial"""
        if not hasattr(self, 'historial'):
            return
            
        self.historial.agregar_calculo(expresion, resultado)
        self._actualizar_historial()
    
    def _actualizar_historial(self):
        """Actualiza el display del historial"""
        if not hasattr(self, 'historial'):
            return
            
        self.historial_text.delete("1.0", "end")
        historial_reciente = self.historial.obtener_historial(10)
        
        for entrada in reversed(historial_reciente):
            linea = f"{entrada['fecha']} | {entrada['expresion']} = {entrada['resultado']}\n"
            self.historial_text.insert("1.0", linea)
    
    def _limpiar_historial(self):
        """Limpia el historial"""
        if not hasattr(self, 'historial'):
            return
            
        if messagebox.askyesno("Confirmar", "¿Deseas borrar todo el historial?"):
            self.historial.limpiar_historial()
            self._actualizar_historial()
    
    def _exportar_historial(self):
        """Exporta el historial a archivo"""
        if not hasattr(self, 'historial'):
            return
            
        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            if self.historial.exportar_txt(archivo):
                messagebox.showinfo("Éxito", f"Historial exportado a {archivo}")
            else:
                messagebox.showerror("Error", "No se pudo exportar el historial")
    
    def _buscar_historial(self):
        """Busca en el historial"""
        # Implementar diálogo de búsqueda
        pass
    
    def _mostrar_memorias(self):
        """Muestra todas las memorias"""
        if not hasattr(self, 'memoria'):
            return
            
        memorias = self.memoria.obtener_todas_memorias()
        info = "\n".join([f"{k}: {v}" for k, v in memorias.items()])
        messagebox.showinfo("Memorias", f"Valores en memoria:\n{info}")
    
    def _toggle_modo_cientifico(self):
        """Alterna entre modo básico y científico"""
        self.modo_cientifico = not self.modo_cientifico
        
        # Limpiar botones existentes
        for child in self.grid_frame.winfo_children():
            child.destroy()
        
        # Recrear botones
        self._crear_botones_esenciales()
        
        if self.modo_cientifico:
            self.btn_cientifico.configure(text="CIENTÍFICA")
            self.root.after(50, self._crear_botones_cientificos_adicionales)
            # Ajustar tamaño de ventana
            self.root.geometry("600x900")
        else:
            self.btn_cientifico.configure(text="BÁSICA")
            # Ajustar tamaño de ventana
            self.root.geometry("500x700")
    
    def _crear_botones_cientificos_adicionales(self):
        """Crea botones adicionales para modo científico"""
        # Botones científicos adicionales
        botones_cientificos = [
            # Fila 8 - Funciones trigonométricas inversas
            ("asin", 8, 0, "#8E44AD"), ("acos", 8, 1, "#8E44AD"), ("atan", 8, 2, "#8E44AD"),
            ("sinh", 8, 3, "#8E44AD"), ("cosh", 8, 4, "#8E44AD"), ("tanh", 8, 5, "#8E44AD"),
        ]
        
        for (texto, fila, col, color) in botones_cientificos:
            btn = ctk.CTkButton(
                self.grid_frame,
                text=texto,
                font=("Arial", 12, "bold"),
                fg_color=color,
                height=35,
                command=lambda t=texto: self._click_boton(t)
            )
            btn.grid(row=fila, column=col, padx=2, pady=2, sticky="nsew")
    
    def _toggle_tema(self):
        """Alterna entre tema claro y oscuro"""
        tema_actual = ctk.get_appearance_mode()
        nuevo_tema = "light" if tema_actual == "dark" else "dark"
        ctk.set_appearance_mode(nuevo_tema)
        
        if hasattr(self, 'config'):
            self.config.establecer("tema", nuevo_tema)
        self._actualizar_icono_tema()
    
    def _actualizar_icono_tema(self):
        """Actualiza el icono del botón de tema"""
        tema_actual = ctk.get_appearance_mode()
        if tema_actual == "dark":
            self.btn_tema.configure(text="☀️")
        else:
            self.btn_tema.configure(text="🌙")
    
    def _mostrar_configuracion(self):
        """Muestra la ventana de configuración"""
        # Implementar ventana de configuración
        pass
    
    def _configurar_atajos(self):
        """Configura atajos de teclado"""
        self.root.bind("<Return>", lambda e: self._calcular())
        self.root.bind("<BackSpace>", lambda e: self._borrar_ultimo())
        self.root.bind("<Escape>", lambda e: self._limpiar())
        self.root.bind("<Delete>", lambda e: self._limpiar_entrada())
        
        # Números y operadores
        for tecla in "0123456789":
            self.root.bind(tecla, lambda e, t=tecla: self._agregar_numero(t))
        
        for tecla, operador in [("plus", "+"), ("minus", "-"), ("period", ".")]:
            self.root.bind(f"<{tecla}>", lambda e, o=operador: self._agregar_operador(o))

if __name__ == "__main__":
    CalculadoraProfesional()
