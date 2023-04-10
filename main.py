a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Não é triangulo")
elif (a == b) and (b == c):
    print("Equilatero")
elif (a == b) or (a == c) or (b == c):
    print("Isoceles")
else:
    print("Escaleno")
