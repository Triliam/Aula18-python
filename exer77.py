qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0

num = 1

while num != 0:
    numeros = int(input("Digite os numeros, quando quiser parar aperte 0: "))
    if numeros == 0:
        break
    if numeros >= 0 and numeros <=25:
        qtd1 = qtd1 + 1
    if numeros >= 26 and numeros <= 50:
        qtd2 = qtd2 + 1
    if numeros >= 51 and numeros <= 75:
        qtd3 = qtd3 + 1
    if numeros >= 76 and numeros <= 100:
        qtd4 = qtd4 + 1
   

print("A qtd de numeros entre 0 - 25 eh: ", qtd1, ". A qtd de numeros entre 26 - 50 eh: ", qtd2, ". A qtd de numeros entre 51 - 75 eh: ", qtd3, ". A qtd de numeros entre 76 - 100 eh: ", qtd4)
