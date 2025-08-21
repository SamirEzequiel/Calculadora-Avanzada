import math

class Calculadora:
    def __init__(self):
        # Constantes matemáticas
        self.PI = math.pi
        self.E = math.e
        self.PHI = (1 + math.sqrt(5)) / 2  # Número áureo
        
    # Operaciones básicas
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Error: División por cero")
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("Error: Raíz de número negativo")
        return math.sqrt(a)

    def raiz_n_esima(self, a, n):
        if a < 0 and n % 2 == 0:
            raise ValueError("Error: Raíz par de número negativo")
        return a ** (1/n)

    # Funciones trigonométricas (en grados)
    def seno(self, a):
        return math.sin(math.radians(a))

    def coseno(self, a):
        return math.cos(math.radians(a))

    def tangente(self, a):
        return math.tan(math.radians(a))

    # Funciones trigonométricas inversas (resultado en grados)
    def arcoseno(self, a):
        if a < -1 or a > 1:
            raise ValueError("Error: Dominio inválido para arcoseno")
        return math.degrees(math.asin(a))

    def arcocoseno(self, a):
        if a < -1 or a > 1:
            raise ValueError("Error: Dominio inválido para arcocoseno")
        return math.degrees(math.acos(a))

    def arcotangente(self, a):
        return math.degrees(math.atan(a))

    # Funciones hiperbólicas
    def seno_hiperbolico(self, a):
        return math.sinh(a)

    def coseno_hiperbolico(self, a):
        return math.cosh(a)

    def tangente_hiperbolica(self, a):
        return math.tanh(a)

    # Logaritmos
    def logaritmo_natural(self, a):
        if a <= 0:
            raise ValueError("Error: Logaritmo no definido para valores <= 0")
        return math.log(a)

    def logaritmo_base_10(self, a):
        if a <= 0:
            raise ValueError("Error: Logaritmo no definido para valores <= 0")
        return math.log10(a)

    def logaritmo_base_2(self, a):
        if a <= 0:
            raise ValueError("Error: Logaritmo no definido para valores <= 0")
        return math.log2(a)

    def logaritmo_base(self, a, base):
        if a <= 0 or base <= 0 or base == 1:
            raise ValueError("Error: Argumentos inválidos para logaritmo")
        return math.log(a, base)

    # Funciones estadísticas
    def factorial(self, n):
        if n < 0 or n != int(n):
            raise ValueError("Error: Factorial solo definido para enteros no negativos")
        if n == 0 or n == 1:
            return 1
        return math.factorial(int(n))

    def combinatoria(self, n, r):
        if n < 0 or r < 0 or r > n:
            raise ValueError("Error: Valores inválidos para combinatoria")
        return math.comb(n, r)

    def permutacion(self, n, r):
        if n < 0 or r < 0 or r > n:
            raise ValueError("Error: Valores inválidos para permutación")
        return math.perm(n, r)

    # Funciones adicionales
    def valor_absoluto(self, a):
        return abs(a)

    def redondear(self, a, decimales=0):
        return round(a, decimales)

    def parte_entera(self, a):
        return math.floor(a)

    def techo(self, a):
        return math.ceil(a)

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Error: Módulo por cero")
        return a % b

    # Conversiones
    def grados_a_radianes(self, grados):
        return math.radians(grados)

    def radianes_a_grados(self, radianes):
        return math.degrees(radianes)

    # Constantes
    def obtener_pi(self):
        return self.PI

    def obtener_e(self):
        return self.E

    def obtener_phi(self):
        return self.PHI
