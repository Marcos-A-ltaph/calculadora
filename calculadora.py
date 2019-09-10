#Complete as funcoes a seguir

def soma(a,b):
	#Insira o codigo aqui
	c=a+b
	print("o resultado da soma é",c)
def subtrai(a,b):
	#Insira o codigo aqui
	c=a-b
	print("o resultado da subtração é",c)
def multiplica(a,b):
	#Insira o codigo aqui
        c=a*b
        print("o resultado da multiplicação é",c)
def divide(a,b):
	#Insira o codigo aqui
        if(b!=0):
                c=a/b
                print("o resultado da multiplicação é",c)
        else:
                print("Não é possível dividir por zero.")
        
#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1,num2)
subtrai(num1,num2)
multiplica(num1,num2)
divide(num1,num2)

