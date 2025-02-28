#Definicion de la clase Calculadora que proporciona
#operaciones matematicas basicas
class Calculadora:
    
    #metodo para sumar dos numeros
    def sumar(self, a, b):
     return a + b
    
	#metodo para restar dos numeros
    def restar(self, a, b):
     return a - b
    
    	#metodo para multiplicar dos numeros
    def multiplicar(self, a, b):
        return a * b

#metodo para dividir el primero entre el segundo e incluye  validacion para evitar division por cero
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b