#CALCULADORA
nome = str(input("Digite seu nome: "))
print ("Seja bem vindo", nome, "Vamos calcular" )

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print("Operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = int(input("Escolha uma operação: "))
if op == 1:
  resultado = num1 + num2
elif op == 2:
  resultado = num1 - num2
elif op == 3:
  resultado = num1 * num2 
elif op == 4:
  resultado = num1 / num2
else:
    print("Operação invalida")

print("O resultado é: ", resultado)
