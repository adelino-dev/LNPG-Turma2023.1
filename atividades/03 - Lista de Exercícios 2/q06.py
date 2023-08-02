n = float(input("Digite um número:"))

if n % 3 == 0 and n % 7 == 0:
  print("É divisível por 3 e por 7")

elif n % 3 == 0 and n % 7 != 0:
  print("É divisível por 3, mas não por 7")

elif n % 3 != 0 and n % 7 == 0:
  print("É divisível por 7, mas não por 3")

else:
  print("Não é divisível por 3 nem por 7.")