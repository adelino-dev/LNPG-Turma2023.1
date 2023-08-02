import math

n1 = int(input("Número 01:"))
n2 = int(input("Número 02:"))

if n1 < n2:
  menor = n1
  maior = n2
else:
  menor = n2
  maior = n1

print("O quadrado de %i é: %i" % (menor, menor**2))
print("A raíz quadrada de %i é: %f" % (maior, math.sqrt(maior)))