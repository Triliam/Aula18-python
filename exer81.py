num1 = 0
num2 = 0
resultado = 0
escolha = ""
#com funções e cmo validaçoes, sem funçoes e com validaçoes esta no exer82
def somar(num1, num2):
    return num1 + num2

def subs(num1, num2):
    if num1 == 0 or num2 == 0:
        print("num invalidos, escolha outros: ")
        num1 = float(input("escolha um numero diferente de zero: "))
        num2 = float(input("escolha um numero diferente de zero: "))
    return num1/num2


while escolha != "soma" and escolha != "sub" and escolha != "div" and escolha != "mult":
    escolha = str(input("Escolha uma operacao aritimetica, soma, sub, div, mult: "))
    if escolha != "soma" and escolha != "sub" and escolha != "div" and escolha != "mult":
        print("opcao inválida! Faça uma escolha válida")
    else:
        print("a opçao escolhida eh: ", escolha)

num1 = float(input("Escolha um numero: "))
num2 = float(input("Escolha outro numero: "))
if escolha == "soma":
    resultado = somar(num1, num2)
    #resultado = num1 + num2
if escolha == "sub":
    resultado =  num1 - num2
if escolha == "div":
    resultado = subs(num1, num2)
    # if num1 == 0 or num2 == 0:
    #     print("num invalidos, escolha outros: ")
    #     num1 = float(input("escolha um numero diferente de zero: "))
    #     num2 = float(input("escolha um numero diferente de zero: "))
    #     resultado = num1 / num2
if escolha == "mult":
    resultado = num1 * num2

print(resultado)

