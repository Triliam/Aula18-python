qtdPares = 0
somaImpares = 0
num = 1

while num != 0: #forma menos elegante de criar uma condicao pro loop acontecer
    numeros = int(input("Digite os numeros, quando quiser parar aperte 0: "))
    if numeros == 0:
        #num = numeros # num recebe numeros, ou seja num recebe 0,  eh uma forma de sair do loop, e vai terminar de ler as linhas dentro do escopo do loop
        break # o break pra encerrar o loop nessa linha e n ler as de baixo (que estao no escopo do loop), usa o break pq a condicao nao esta na variavel numeros e sim em num
    if numeros % 2 == 0:
        qtdPares = qtdPares +1
    else:
        somaImpares = somaImpares + numeros

print("A quantidade de numeros pares é: ", qtdPares, ". E a soma dos numeros impares eh: ", somaImpares)