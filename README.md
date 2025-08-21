# 🧮 Calculadora Profesional Avanzada

Una calculadora científica profesional en Python con **interfaz gráfica moderna**, funciones matemáticas avanzadas y características profesionales. Optimizada para **carga ultra-rápida** y **experiencia de usuario excepcional**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

---

## 🚀 **Características Principales**

### ✨ **Interfaz Profesional**
- **Diseño moderno** con CustomTkinter
- **Tema oscuro/claro** intercambiable
- **Pantalla dual**: expresión y resultado
- **Botones organizados** como calculadora real
- **Información de memoria** en tiempo real
- **Responsive design** que se adapta a cualquier tamaño

### ⚡ **Rendimiento Optimizado**
- **Carga ultra-rápida**: < 1 segundo
- **Carga progresiva** de elementos
- **Threading** para operaciones pesadas
- **Debouncing** en redimensionamiento
- **Lazy loading** de funciones avanzadas

### 🧮 **Funciones Matemáticas**

#### **Operaciones Básicas**
- Suma, resta, multiplicación, división
- Potenciación y raíz cuadrada
- Módulo y porcentaje
- Paréntesis y precedencia de operadores

#### **Funciones Trigonométricas**
- Seno, coseno, tangente
- **Funciones inversas**: arcoseno, arcocoseno, arcotangente
- **Funciones hiperbólicas**: sinh, cosh, tanh
- Conversión entre grados y radianes

#### **Funciones Logarítmicas**
- Logaritmo natural (ln)
- Logaritmo base 10 (log)
- Logaritmo base 2
- Logaritmo base personalizada

#### **Funciones Estadísticas**
- Factorial
- Combinatoria
- Permutación
- Valor absoluto

#### **Constantes Matemáticas**
- π (Pi)
- e (Número de Euler)
- φ (Número áureo)

### 💾 **Gestión de Memoria**
- **5 memorias independientes** (M1-M5)
- Operaciones: MC, MR, M+, M-, MS, M^
- Visualización en tiempo real
- Persistencia entre sesiones

### 📋 **Historial Inteligente**
- **Registro automático** de cálculos
- **Búsqueda** en historial
- **Exportación** a archivo TXT
- **Límite configurable** de entradas
- **Persistencia** entre sesiones

### 🎨 **Personalización**
- **Temas**: Oscuro/Claro
- **Colores personalizables**
- **Tamaño de ventana** configurable
- **Precisión decimal** ajustable
- **Configuración persistente**

### ⌨️ **Atajos de Teclado**
- **Enter**: Calcular
- **Escape**: Limpiar todo
- **Backspace**: Borrar último carácter
- **Delete**: Limpiar entrada actual
- **Números y operadores**: Directos

---

## 🛠️ **Instalación**

### **Requisitos**
- Python 3.8 o superior
- Windows, macOS o Linux

### **Instalación Automática**
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/Calculadora-Avanzada.git
cd Calculadora-Avanzada

# Ejecutar instalador automático
python install.py
```

### **Instalación Manual**
```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Calculadora-Avanzada.git
cd Calculadora-Avanzada

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la calculadora
python src/main.py
```

### **Dependencias**
```
customtkinter==5.2.0
pillow==10.0.1
```

---

## 🎮 **Uso**

### **Inicio Rápido**
```bash
python src/main.py
```

### **Operaciones Básicas**
1. **Números**: Hacer clic en los botones numéricos
2. **Operadores**: +, -, ×, ÷, ^
3. **Calcular**: Presionar = o Enter
4. **Limpiar**: C (todo) o CE (entrada actual)

### **Funciones Científicas**
1. **Cambiar a modo científico**: Botón "BÁSICA" → "CIENTÍFICA"
2. **Funciones trigonométricas**: sin, cos, tan
3. **Funciones inversas**: asin, acos, atan
4. **Funciones hiperbólicas**: sinh, cosh, tanh
5. **Logaritmos**: log, ln
6. **Estadísticas**: n!, |x|, x², x³

### **Gestión de Memoria**
- **MC**: Limpiar memoria
- **MR**: Recuperar valor de memoria
- **M+**: Sumar a memoria
- **M-**: Restar de memoria
- **MS**: Guardar en memoria
- **M^**: Ver todas las memorias

### **Historial**
- **Visualización automática** de últimos cálculos
- **🗑️ Limpiar**: Borrar todo el historial
- **💾 Exportar**: Guardar en archivo TXT
- **🔍 Buscar**: Buscar en historial

### **Personalización**
- **🌙/☀️**: Cambiar tema oscuro/claro
- **⚙️**: Configuración avanzada
- **Redimensionar**: Ventana responsive

---

## 🏗️ **Arquitectura del Proyecto**

```
Calculadora-Avanzada/
├── src/
│   ├── main.py              # Interfaz gráfica principal
│   ├── calculadora.py       # Lógica matemática
│   └── utils.py             # Utilidades (config, historial, memoria)
├── test/
│   └── test_calculadora.py  # Tests unitarios
├── config.json              # Configuración persistente
├── historial.json           # Historial de cálculos
├── requirements.txt         # Dependencias
├── install.py              # Instalador automático
├── README.md               # Documentación principal
├── OPTIMIZACIONES.md       # Documentación de optimizaciones
├── DEMO.md                 # Guía de demostración
└── .gitignore              # Archivos ignorados por Git
```

### **Componentes Principales**

#### **`CalculadoraProfesional` (main.py)**
- Interfaz gráfica con CustomTkinter
- Gestión de eventos y responsividad
- Carga optimizada y threading

#### **`Calculadora` (calculadora.py)**
- Funciones matemáticas avanzadas
- Manejo de errores robusto
- Constantes matemáticas

#### **`Configuracion` (utils.py)**
- Gestión de configuración persistente
- Temas y personalización
- Archivo JSON de configuración

#### **`GestorHistorial` (utils.py)**
- Registro de cálculos
- Búsqueda y exportación
- Persistencia en JSON

#### **`GestorMemoria` (utils.py)**
- 5 memorias independientes
- Operaciones estándar
- Persistencia de datos

---

## 🧪 **Testing**

### **Ejecutar Tests**
```bash
# Todos los tests
python -m unittest test/test_calculadora.py -v

# Test específico
python -m unittest test.test_calculadora.TestCalculadora.test_operaciones_basicas -v
```

### **Cobertura de Tests**
- ✅ **19 tests** implementados
- ✅ **Operaciones básicas** y avanzadas
- ✅ **Manejo de errores** (división por cero, etc.)
- ✅ **Funciones trigonométricas** e hiperbólicas
- ✅ **Logaritmos** y funciones estadísticas
- ✅ **Constantes matemáticas**

---

## ⚡ **Optimizaciones de Rendimiento**

### **Problemas Resueltos**
- ❌ **Carga lenta** (3-5 segundos)
- ❌ **Interfaz bloqueada** durante carga
- ❌ **Experiencia de usuario** pobre

### **Soluciones Implementadas**
- ✅ **Carga lazy** (< 1 segundo)
- ✅ **Threading** para operaciones pesadas
- ✅ **Carga progresiva** de elementos
- ✅ **Debouncing** en redimensionamiento
- ✅ **Verificaciones de seguridad**

### **Técnicas Utilizadas**
- **Lazy Loading**: Solo carga elementos necesarios
- **Background Threading**: Datos pesados en segundo plano
- **Progressive Enhancement**: Funcionalidad básica → avanzada
- **Debouncing**: Optimización de eventos
- **Fallbacks**: Configuración por defecto

---

## 🎨 **Personalización Avanzada**

### **Configuración de Temas**
```json
{
  "tema": "dark",
  "color_tema": "blue",
  "tamaño_ventana": "500x700",
  "decimales": 6,
  "limite_historial": 100
}
```

### **Colores Personalizables**
- **Números**: `#2C3E50` (gris oscuro)
- **Operadores**: `#E74C3C` (rojo)
- **Funciones**: `#4ECDC4` (turquesa)
- **Memoria**: `#FF6B6B` (coral)
- **Constantes**: `#9B59B6` (púrpura)

---

## 🚀 **Características Avanzadas**

### **Responsive Design**
- **Adaptación automática** a cualquier tamaño de ventana
- **Fuentes escalables** según el espacio disponible
- **Botones responsivos** que se ajustan al layout
- **Grid system** flexible y optimizado

### **Modo Científico**
- **Botones adicionales** para funciones avanzadas
- **Ventana expandida** automáticamente
- **Funciones trigonométricas inversas**
- **Funciones hiperbólicas**
- **Transición suave** entre modos

### **Gestión de Errores**
- **Validación robusta** de entradas
- **Mensajes de error** informativos
- **Recuperación automática** de errores
- **Prevención** de operaciones inválidas

---

## 📊 **Métricas de Rendimiento**

### **Tiempos de Carga**
- **Interfaz básica**: < 0.5 segundos
- **Funcionalidad completa**: < 1 segundo
- **Modo científico**: < 0.2 segundos adicionales

### **Uso de Memoria**
- **Inicial**: ~15 MB
- **Con historial**: ~20 MB
- **Máximo**: ~25 MB

### **Tests de Rendimiento**
- **19 tests unitarios**: 100% pasando
- **Tiempo de ejecución**: < 0.01 segundos
- **Cobertura**: Operaciones básicas y avanzadas

---

## 🤝 **Contribución**

### **Cómo Contribuir**
1. **Fork** el repositorio
2. **Crear** una rama para tu feature
3. **Implementar** tus cambios
4. **Ejecutar** los tests
5. **Crear** un Pull Request

### **Estándares de Código**
- **PEP 8** para estilo de código
- **Docstrings** para documentación
- **Tests unitarios** para nuevas funciones
- **Manejo de errores** robusto

---

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

*¡Disfruta de una experiencia de calculadora profesional con carga ultra-rápida! ⚡🧮✨*
