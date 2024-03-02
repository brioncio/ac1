def anoBissexto():
    ano = int(input("Informe um ano para saber se é bissexto: "))
    
    if ano % 4 == 0 or ano % 100 == 0 and ano % 400 != 0:
        return True
    else:
        return False

print(anoBissexto())