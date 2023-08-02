def isTriangle(a, b, c):
  if (a + b > c) and (a + c > b) and (c + b > a):
    return "É um triângulo."
  else:
    return "Não é um triângulo"


a = float(input("Lado de A:"))
b = float(input("Lado de B:"))
c = float(input("Lado de C:"))
print(f"Resultado {isTriangle(a,b, c)}")
