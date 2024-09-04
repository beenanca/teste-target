def pertence_fibonacci(numero):

  a, b = 0, 1
  while a <= numero:
    if a == numero:
      return True
    a, b = b, a + b
  return False

# Entrada do usuário
numero = int(input("Informe um número: "))

# Verificação e saída
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
