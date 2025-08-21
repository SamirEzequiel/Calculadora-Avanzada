import unittest
import math
import sys
import os

# Agregar el directorio src al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.calc = Calculadora()
    
    def test_operaciones_basicas(self):
        """Test de operaciones básicas"""
        # Suma
        self.assertEqual(self.calc.suma(5, 3), 8)
        self.assertEqual(self.calc.suma(-5, 3), -2)
        self.assertEqual(self.calc.suma(0, 0), 0)
        
        # Resta
        self.assertEqual(self.calc.resta(5, 3), 2)
        self.assertEqual(self.calc.resta(-5, 3), -8)
        self.assertEqual(self.calc.resta(0, 0), 0)
        
        # Multiplicación
        self.assertEqual(self.calc.multiplicacion(5, 3), 15)
        self.assertEqual(self.calc.multiplicacion(-5, 3), -15)
        self.assertEqual(self.calc.multiplicacion(0, 5), 0)
        
        # División
        self.assertEqual(self.calc.division(6, 2), 3)
        self.assertEqual(self.calc.division(-6, 2), -3)
        self.assertEqual(self.calc.division(0, 5), 0)
    
    def test_division_por_cero(self):
        """Test de división por cero"""
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)
    
    def test_potencia(self):
        """Test de potencia"""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(2, -1), 0.5)
    
    def test_raiz_cuadrada(self):
        """Test de raíz cuadrada"""
        self.assertEqual(self.calc.raiz_cuadrada(4), 2)
        self.assertEqual(self.calc.raiz_cuadrada(0), 0)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), math.sqrt(2), places=10)
    
    def test_raiz_cuadrada_negativa(self):
        """Test de raíz cuadrada de número negativo"""
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-4)
    
    def test_raiz_n_esima(self):
        """Test de raíz n-ésima"""
        self.assertEqual(self.calc.raiz_n_esima(8, 3), 2)
        self.assertEqual(self.calc.raiz_n_esima(16, 4), 2)
        self.assertAlmostEqual(self.calc.raiz_n_esima(2, 2), math.sqrt(2), places=10)
    
    def test_funciones_trigonometricas(self):
        """Test de funciones trigonométricas"""
        # Seno
        self.assertAlmostEqual(self.calc.seno(30), 0.5, places=3)
        self.assertAlmostEqual(self.calc.seno(90), 1.0, places=3)
        self.assertAlmostEqual(self.calc.seno(0), 0.0, places=3)
        
        # Coseno
        self.assertAlmostEqual(self.calc.coseno(60), 0.5, places=3)
        self.assertAlmostEqual(self.calc.coseno(0), 1.0, places=3)
        self.assertAlmostEqual(self.calc.coseno(90), 0.0, places=3)
        
        # Tangente
        self.assertAlmostEqual(self.calc.tangente(45), 1.0, places=3)
        self.assertAlmostEqual(self.calc.tangente(0), 0.0, places=3)
    
    def test_funciones_trigonometricas_inversas(self):
        """Test de funciones trigonométricas inversas"""
        # Arcoseno
        self.assertAlmostEqual(self.calc.arcoseno(0.5), 30.0, places=1)
        self.assertAlmostEqual(self.calc.arcoseno(1.0), 90.0, places=1)
        self.assertAlmostEqual(self.calc.arcoseno(0.0), 0.0, places=1)
        
        # Arcocoseno
        self.assertAlmostEqual(self.calc.arcocoseno(0.5), 60.0, places=1)
        self.assertAlmostEqual(self.calc.arcocoseno(1.0), 0.0, places=1)
        self.assertAlmostEqual(self.calc.arcocoseno(0.0), 90.0, places=1)
        
        # Arcotangente
        self.assertAlmostEqual(self.calc.arcotangente(1.0), 45.0, places=1)
        self.assertAlmostEqual(self.calc.arcotangente(0.0), 0.0, places=1)
    
    def test_dominio_funciones_inversas(self):
        """Test de dominio de funciones trigonométricas inversas"""
        with self.assertRaises(ValueError):
            self.calc.arcoseno(1.5)  # Fuera del dominio [-1, 1]
        
        with self.assertRaises(ValueError):
            self.calc.arcocoseno(-1.5)  # Fuera del dominio [-1, 1]
    
    def test_funciones_hiperbolicas(self):
        """Test de funciones hiperbólicas"""
        # Seno hiperbólico
        self.assertAlmostEqual(self.calc.seno_hiperbolico(0), 0.0, places=3)
        self.assertAlmostEqual(self.calc.seno_hiperbolico(1), math.sinh(1), places=3)
        
        # Coseno hiperbólico
        self.assertAlmostEqual(self.calc.coseno_hiperbolico(0), 1.0, places=3)
        self.assertAlmostEqual(self.calc.coseno_hiperbolico(1), math.cosh(1), places=3)
        
        # Tangente hiperbólica
        self.assertAlmostEqual(self.calc.tangente_hiperbolica(0), 0.0, places=3)
        self.assertAlmostEqual(self.calc.tangente_hiperbolica(1), math.tanh(1), places=3)
    
    def test_logaritmos(self):
        """Test de logaritmos"""
        # Logaritmo natural
        self.assertAlmostEqual(self.calc.logaritmo_natural(math.e), 1.0, places=3)
        self.assertAlmostEqual(self.calc.logaritmo_natural(1), 0.0, places=3)
        
        # Logaritmo base 10
        self.assertAlmostEqual(self.calc.logaritmo_base_10(100), 2.0, places=3)
        self.assertAlmostEqual(self.calc.logaritmo_base_10(1), 0.0, places=3)
        
        # Logaritmo base 2
        self.assertAlmostEqual(self.calc.logaritmo_base_2(8), 3.0, places=3)
        self.assertAlmostEqual(self.calc.logaritmo_base_2(1), 0.0, places=3)
        
        # Logaritmo base personalizada
        self.assertAlmostEqual(self.calc.logaritmo_base(8, 2), 3.0, places=3)
        self.assertAlmostEqual(self.calc.logaritmo_base(27, 3), 3.0, places=3)
    
    def test_logaritmos_invalidos(self):
        """Test de logaritmos con argumentos inválidos"""
        with self.assertRaises(ValueError):
            self.calc.logaritmo_natural(0)  # log(0) no está definido
        
        with self.assertRaises(ValueError):
            self.calc.logaritmo_natural(-1)  # log(-1) no está definido
        
        with self.assertRaises(ValueError):
            self.calc.logaritmo_base(5, 1)  # Base 1 no válida
    
    def test_funciones_estadisticas(self):
        """Test de funciones estadísticas"""
        # Factorial
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        
        # Combinatoria
        self.assertEqual(self.calc.combinatoria(5, 2), 10)
        self.assertEqual(self.calc.combinatoria(5, 0), 1)
        self.assertEqual(self.calc.combinatoria(5, 5), 1)
        
        # Permutación
        self.assertEqual(self.calc.permutacion(5, 2), 20)
        self.assertEqual(self.calc.permutacion(5, 0), 1)
        self.assertEqual(self.calc.permutacion(5, 5), 120)
    
    def test_factorial_invalido(self):
        """Test de factorial con argumentos inválidos"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)  # Factorial de negativo
        
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)  # Factorial de decimal
    
    def test_combinatoria_invalida(self):
        """Test de combinatoria con argumentos inválidos"""
        with self.assertRaises(ValueError):
            self.calc.combinatoria(5, 6)  # r > n
        
        with self.assertRaises(ValueError):
            self.calc.combinatoria(-1, 2)  # n negativo
    
    def test_funciones_adicionales(self):
        """Test de funciones adicionales"""
        # Valor absoluto
        self.assertEqual(self.calc.valor_absoluto(-5), 5)
        self.assertEqual(self.calc.valor_absoluto(5), 5)
        self.assertEqual(self.calc.valor_absoluto(0), 0)
        
        # Redondear
        self.assertEqual(self.calc.redondear(3.14159, 2), 3.14)
        self.assertEqual(self.calc.redondear(3.14159), 3)
        
        # Parte entera
        self.assertEqual(self.calc.parte_entera(3.7), 3)
        self.assertEqual(self.calc.parte_entera(-3.7), -4)
        
        # Techo
        self.assertEqual(self.calc.techo(3.1), 4)
        self.assertEqual(self.calc.techo(-3.1), -3)
        
        # Módulo
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(-7, 3), 2)
    
    def test_modulo_por_cero(self):
        """Test de módulo por cero"""
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)
    
    def test_conversiones(self):
        """Test de conversiones"""
        # Grados a radianes
        self.assertAlmostEqual(self.calc.grados_a_radianes(180), math.pi, places=3)
        self.assertAlmostEqual(self.calc.grados_a_radianes(90), math.pi/2, places=3)
        
        # Radianes a grados
        self.assertAlmostEqual(self.calc.radianes_a_grados(math.pi), 180.0, places=1)
        self.assertAlmostEqual(self.calc.radianes_a_grados(math.pi/2), 90.0, places=1)
    
    def test_constantes(self):
        """Test de constantes matemáticas"""
        self.assertEqual(self.calc.obtener_pi(), math.pi)
        self.assertEqual(self.calc.obtener_e(), math.e)
        self.assertAlmostEqual(self.calc.obtener_phi(), (1 + math.sqrt(5)) / 2, places=10)

if __name__ == '__main__':
    unittest.main()
