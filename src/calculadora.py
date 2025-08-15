import math

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: Raíz de número negativo"
        return math.sqrt(a)

    def seno(self, a):
        return math.sin(math.radians(a))

    def coseno(self, a):
        return math.cos(math.radians(a))

    def tangente(self, a):
        return math.tan(math.radians(a))

    def logaritmo(self, a):
        if a <= 0:
            return "Error: Logaritmo no definido para valores <= 0"
        return math.log(a)
