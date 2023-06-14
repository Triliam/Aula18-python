#se o ano for divisivel por 4 e restar 0, o ano eh bissexto - e tem 366 dias


ano = int(input("Qual ano? "))

if ano % 4 == 0:
    print("ano bissexto!")
else:
    print("ano n bissexto")

