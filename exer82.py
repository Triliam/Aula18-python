num1 = 0
num2 = 0
resultado = 0

escolha = str(input("Escolha uma operacao aritimetica, soma, sub, div, mult: "))

if escolha != "soma" and escolha != "sub" and escolha != "div" and escolha != "mult":
    print("opcao inválida")
    escolha = str(input("Escolha uma operacao aritimetica, soma, sub, div, mult: "))

num1 = float(input("Escolha um numero: "))
num2 = float(input("Escolha outro numero: "))
if escolha == "soma":
    resultado = num1 + num2
if escolha == "sub":
    resultado =  num1 - num2
if escolha == "div":
    if num1 == 0 or num2 == 0:
        print("num invalidos, escolha outros: ")
        num1 = float(input("escolha um numero diferente de zero: "))
        num2 = float(input("escolha um numero diferente de zero: "))
        resultado = num1 / num2
if escolha == "mult":
    resultado = num1 * num2

print(resultado)
