maior = 0
menor = 0
soma = 0
media = 0
lista=[]

num = 1
count = 0

while num != 0:
    numeros = int(input("Digite os numeros, qnd quiser parar digite 0:"))

    if numeros == 0:
        break

    lista.append(numeros)

    count = count + 1
    if count == 1:
        maior = numeros
        menor = numeros

    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros

print(lista)

for i in range (len(lista)):
    soma = soma + lista[i]
    media = soma / len(lista)

print(" o maior eh: ", maior, ". E o menor eh: ", menor, ". A soma é: ", soma, ". E a media eh: ", media)

print("a media: ", soma, "dividido por: ", len(lista), " que eh: ", media)