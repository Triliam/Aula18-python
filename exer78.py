maior = 0
menor = 0
soma = 0
media = 0

num = 1
count = 0
qtdNumeros = 0

while num != 0:
    numeros = int(input("Digite os numeros, qnd quiser parar digite 0:"))

    if numeros == 0: #coloca essa condicao no inicio do loop, pro numero 0 nao entrar nas operacoes matematicas
        break

    count = count + 1
    if count == 1:
        maior = numeros
        menor = numeros

    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    
    qtdNumeros = qtdNumeros + 1
    soma = soma + numeros
    media = soma / qtdNumeros

print(" o maior eh: ", maior, ". E o menor eh: ", menor, ". A soma é: ", soma, ". E a media eh: ", media)

print("a media de : ", soma, "dividido por: ", qtdNumeros, " que eh: ", media)