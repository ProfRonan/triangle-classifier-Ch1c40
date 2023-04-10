a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Não é um triângulo")
elif (a == b) and (b == c):
    print("Equilátero")
elif (a == b) or (a == c) or (b == c):
    print("Isósceles")
else:
    print("Escaleno")
