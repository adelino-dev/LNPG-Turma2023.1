n = float(input("Digite um número:"))

if n % 10 == 0:
  print("É divisível por 10.")

elif n % 5 == 0:
  print("É divisível por 5.")

elif n % 2 == 0:
  print("É divisível por 2.")

else:
  print("Não é divisível por 10, por 5 nem por 2.")
