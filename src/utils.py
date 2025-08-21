import json
import os
from datetime import datetime

class Configuracion:
    def __init__(self, archivo_config="config.json"):
        self.archivo_config = archivo_config
        self.config = self._cargar_configuracion()
    
    def _cargar_configuracion(self):
        """Carga la configuración desde archivo JSON"""
        config_default = {
            "tema": "dark",
            "color_tema": "blue",
            "tamaño_ventana": "450x650",
            "decimales": 6,
            "historial_maximo": 100,
            "memorias": {
                "M1": 0.0,
                "M2": 0.0,
                "M3": 0.0
            }
        }
        
        if os.path.exists(self.archivo_config):
            try:
                with open(self.archivo_config, 'r', encoding='utf-8') as f:
                    config_cargada = json.load(f)
                    # Combinar con configuración por defecto
                    config_default.update(config_cargada)
            except:
                pass
        
        return config_default
    
    def guardar_configuracion(self):
        """Guarda la configuración actual en archivo JSON"""
        try:
            with open(self.archivo_config, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
    
    def obtener(self, clave, valor_default=None):
        """Obtiene un valor de configuración"""
        return self.config.get(clave, valor_default)
    
    def establecer(self, clave, valor):
        """Establece un valor de configuración"""
        self.config[clave] = valor
        self.guardar_configuracion()

class GestorHistorial:
    def __init__(self, archivo_historial="historial.json"):
        self.archivo_historial = archivo_historial
        self.historial = self._cargar_historial()
    
    def _cargar_historial(self):
        """Carga el historial desde archivo JSON"""
        if os.path.exists(self.archivo_historial):
            try:
                with open(self.archivo_historial, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def agregar_calculo(self, expresion, resultado, timestamp=None):
        """Agrega un cálculo al historial"""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        entrada = {
            "expresion": expresion,
            "resultado": resultado,
            "timestamp": timestamp,
            "fecha": datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.historial.append(entrada)
        self._guardar_historial()
    
    def obtener_historial(self, limite=None):
        """Obtiene el historial completo o limitado"""
        if limite:
            return self.historial[-limite:]
        return self.historial
    
    def buscar_historial(self, termino):
        """Busca en el historial por término"""
        resultados = []
        termino = termino.lower()
        for entrada in self.historial:
            if (termino in entrada["expresion"].lower() or 
                termino in str(entrada["resultado"]).lower()):
                resultados.append(entrada)
        return resultados
    
    def limpiar_historial(self):
        """Limpia todo el historial"""
        self.historial = []
        self._guardar_historial()
    
    def _guardar_historial(self):
        """Guarda el historial en archivo JSON"""
        try:
            with open(self.archivo_historial, 'w', encoding='utf-8') as f:
                json.dump(self.historial, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar historial: {e}")
    
    def exportar_txt(self, archivo_destino):
        """Exporta el historial a archivo de texto"""
        try:
            with open(archivo_destino, 'w', encoding='utf-8') as f:
                f.write("=== HISTORIAL DE CÁLCULOS ===\n\n")
                for entrada in self.historial:
                    f.write(f"Fecha: {entrada['fecha']}\n")
                    f.write(f"Expresión: {entrada['expresion']}\n")
                    f.write(f"Resultado: {entrada['resultado']}\n")
                    f.write("-" * 40 + "\n")
            return True
        except Exception as e:
            print(f"Error al exportar historial: {e}")
            return False

class GestorMemoria:
    def __init__(self):
        self.memorias = {
            "M1": 0.0,
            "M2": 0.0,
            "M3": 0.0,
            "M4": 0.0,
            "M5": 0.0
        }
    
    def obtener_memoria(self, nombre):
        """Obtiene el valor de una memoria"""
        return self.memorias.get(nombre, 0.0)
    
    def establecer_memoria(self, nombre, valor):
        """Establece el valor de una memoria"""
        if nombre in self.memorias:
            self.memorias[nombre] = float(valor)
    
    def sumar_memoria(self, nombre, valor):
        """Suma un valor a la memoria especificada"""
        if nombre in self.memorias:
            self.memorias[nombre] += float(valor)
    
    def restar_memoria(self, nombre, valor):
        """Resta un valor a la memoria especificada"""
        if nombre in self.memorias:
            self.memorias[nombre] -= float(valor)
    
    def limpiar_memoria(self, nombre=None):
        """Limpia una memoria específica o todas"""
        if nombre:
            if nombre in self.memorias:
                self.memorias[nombre] = 0.0
        else:
            for key in self.memorias:
                self.memorias[key] = 0.0
    
    def obtener_todas_memorias(self):
        """Obtiene todas las memorias"""
        return self.memorias.copy()

def formatear_numero(numero, decimales=6):
    """Formatea un número con el número de decimales especificado"""
    try:
        if isinstance(numero, (int, float)):
            if numero == int(numero):
                return str(int(numero))
            else:
                return f"{numero:.{decimales}f}".rstrip('0').rstrip('.')
        return str(numero)
    except:
        return str(numero)

def validar_expresion(expresion):
    """Valida si una expresión matemática es válida"""
    try:
        # Reemplazar funciones personalizadas
        expr_temp = expresion.lower()
        expr_temp = expr_temp.replace('sin', 'math.sin')
        expr_temp = expr_temp.replace('cos', 'math.cos')
        expr_temp = expr_temp.replace('tan', 'math.tan')
        expr_temp = expr_temp.replace('log', 'math.log')
        expr_temp = expr_temp.replace('sqrt', 'math.sqrt')
        
        # Evaluar la expresión
        eval(expr_temp)
        return True
    except:
        return False
