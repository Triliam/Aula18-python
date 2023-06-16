qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0

num = 1

while True:
    numeros = int(input("Digite os numeros, quando quiser parar aperte 0: "))
    
    if numeros >= 0 and numeros <=25: # o 0 entra na contagem, mas o loop encerra, melhor se fosse de 1 ate 25, ou outra condicao pra quebrar o loop
        qtd1 = qtd1 + 1
    if numeros >= 26 and numeros <= 50:
        qtd2 = qtd2 + 1
    if numeros >= 51 and numeros <= 75:
        qtd3 = qtd3 + 1
    if numeros >= 76 and numeros <= 100:
        qtd4 = qtd4 + 1
    if numeros == 0: #nesse a condicao de quebrar o loop vem por ultimo, pq o 0 precisa entrar 
        break #nesse caso precisa do break pra quebrar o loop
print("A qtd de numeros entre 0 - 25 eh: ", qtd1, ". A qtd de numeros entre 26 - 50 eh: ", qtd2, ". A qtd de numeros entre 51 - 75 eh: ", qtd3, ". A qtd de numeros entre 76 - 100 eh: ", qtd4)
