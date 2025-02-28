#importacion de modulo unittest para realizar pruebas unitarias
import unittest

#importacion de la clase calculadora desde el archivo calculadora
from Calculadora import Calculadora

#definicion de la clase de pruebas que hereda de unittest.TestCase
class TestCalculadora(unittest.TestCase):
 
	#metodo que se ejecuta antes de cada prueba individual
	def setUp(self):
		#creamos una instancia de calculadora para usar en las pruebas
		self.calc = Calculadora()
		
	#prueba del metodo suma
	def test_sumar(self):
		#prueba la resta de dos numeros positivos
		self.assertEqual(self.calc.sumar(5, 4), 9)
		#prueba la resta de dos numeros iguales
		self.assertEqual(self.calc.sumar(8, 8), 16)
		#prueba la resta de dos numeros negativos
		self.assertEqual(self.calc.sumar(-4, -6), -10)
		
	#prueba del metodo resta
	def test_restar(self):
		#prueba la resta de dos numeros positivos
		self.assertEqual(self.calc.restar(5, 4), 1)
		#prueba la resta de dos numeros iguales
		self.assertEqual(self.calc.restar(8, 8), 0)
		#prueba la resta de dos numeros negativos
		self.assertEqual(self.calc.restar(-4, -6), 2)
		
	#prueba del metodo multiplicacion
	def test_multiplicar(self):
		#prueba multiplicacion de dos numeros positivos
		self.assertEqual(self.calc.multiplicar(5, 8), 40)
		#prueba multiplicacion de dos numeros iguales
		self.assertEqual(self.calc.multiplicar(8, 0), 0)
		#prueba multiplicacion de un numero positivo y uno negativo
		self.assertEqual(self.calc.multiplicar(-4, 6), -24)
		
	#Prueba del metodo dividir
	def test_dividir(self): 
		#prueba division de dos numeros positivos
		self.assertEqual(self.calc.dividir(10, 2), 5)
		#prueba division con resultado decimal
		self.assertEqual(self.calc.dividir(10, 3), 3.3333333333333335)
		#prueba division periodica usando assertAlmostEqual para comparar con precision limitada
		self.assertAlmostEqual(self.calc.dividir(29, 6), 4.833333333333333)
		#prueba division por cero
		with self.assertRaises(ValueError):
			self.calc.dividir(10, 0)
			
#bloque condicional que permite ejecutar las pruebas directamente
if __name__ == '__main__':    
#inicializar la ejecucioin de todas las pruebas definidas en la clase
	unittest.main()
		