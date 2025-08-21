#!/usr/bin/env python3
"""
Script de instalación para la Calculadora Profesional Avanzada
"""

import subprocess
import sys
import os

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y maneja errores"""
    print(f"🔄 {descripcion}...")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {descripcion} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {descripcion}: {e}")
        print(f"   Salida de error: {e.stderr}")
        return False

def verificar_python():
    """Verifica que Python esté instalado y sea compatible"""
    print("🐍 Verificando versión de Python...")
    
    if sys.version_info < (3, 8):
        print(f"❌ Python {sys.version} no es compatible. Se requiere Python 3.8 o superior.")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} es compatible")
    return True

def instalar_dependencias():
    """Instala las dependencias del proyecto"""
    print("📦 Instalando dependencias...")
    
    # Actualizar pip
    if not ejecutar_comando(f"{sys.executable} -m pip install --upgrade pip", "Actualizando pip"):
        return False
    
    # Instalar dependencias
    if not ejecutar_comando(f"{sys.executable} -m pip install -r requirements.txt", "Instalando dependencias"):
        return False
    
    return True

def ejecutar_tests():
    """Ejecuta los tests para verificar la instalación"""
    print("🧪 Ejecutando tests...")
    
    if not ejecutar_comando(f"{sys.executable} -m unittest test/test_calculadora.py -v", "Ejecutando tests"):
        return False
    
    return True

def crear_archivos_configuracion():
    """Crea archivos de configuración iniciales"""
    print("⚙️ Creando archivos de configuración...")
    
    # Crear archivo de configuración por defecto
    config_default = {
        "tema": "dark",
        "color_tema": "blue",
        "tamaño_ventana": "500x700",
        "decimales": 6,
        "historial_maximo": 100
    }
    
    try:
        import json
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config_default, f, indent=4, ensure_ascii=False)
        print("✅ Archivo de configuración creado")
    except Exception as e:
        print(f"❌ Error creando archivo de configuración: {e}")
        return False
    
    return True

def mostrar_instrucciones():
    """Muestra instrucciones de uso"""
    print("\n" + "="*60)
    print("🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
    print("="*60)
    print("\n📋 Para ejecutar la calculadora:")
    print("   python src/main.py")
    print("\n🧪 Para ejecutar los tests:")
    print("   python -m unittest test/test_calculadora.py -v")
    print("\n📖 Para ver la documentación:")
    print("   Ver README.md")
    print("\n🎮 Atajos de teclado:")
    print("   Enter: Calcular")
    print("   Escape: Limpiar todo")
    print("   Backspace: Borrar último carácter")
    print("   Delete: Limpiar entrada actual")
    print("\n✨ Características principales:")
    print("   • Interfaz moderna y profesional")
    print("   • Funciones científicas avanzadas")
    print("   • Sistema de memoria múltiple")
    print("   • Historial persistente")
    print("   • Temas personalizables")
    print("\n🚀 ¡Disfruta calculando con estilo profesional!")
    print("="*60)

def main():
    """Función principal de instalación"""
    print("🧮 INSTALADOR - CALCULADORA PROFESIONAL AVANZADA")
    print("="*60)
    
    # Verificar Python
    if not verificar_python():
        sys.exit(1)
    
    # Instalar dependencias
    if not instalar_dependencias():
        print("❌ Error instalando dependencias. Verifica tu conexión a internet.")
        sys.exit(1)
    
    # Crear archivos de configuración
    if not crear_archivos_configuracion():
        print("⚠️ Advertencia: No se pudieron crear archivos de configuración")
    
    # Ejecutar tests
    if not ejecutar_tests():
        print("⚠️ Advertencia: Algunos tests fallaron")
    
    # Mostrar instrucciones
    mostrar_instrucciones()

if __name__ == "__main__":
    main()
