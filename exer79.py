valorTotal = 0
valorPorPessoa = 0
valorCombusLitro = 0
qtdKm = 0
valorPedagios = 0
qtdPessoas = 0



valorCombusLitro = float(input("Qual valor do combutivel por litro?: "))

qtdKm = float(input("Quantos kilometros sera percorrido?: "))

valorPedagios = float(input("Qual valor total dos pedagios?: "))

qtdPessoas = float(input("Quantas pessoas?: "))

valorTotal = (valorCombusLitro * qtdKm) + valorPedagios
valorPorPessoa = valorTotal/qtdPessoas

print("custo total: ", valorTotal, ". custo por passageiro: ", valorPorPessoa)