def equacaoQuadratica():
    a = int(input("Informe o valor de \"a\": "))
    b = int(input("Informe o valor de \"b\": "))
    c = int(input("Informe o valor de \"c\": "))

    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        print("A equação não tem raiz real.")
    else:
        primeiraRaiz = (-b + (delta ** 0.5)) / (2 * a)
        segundaRaiz = (-b - (delta ** 0.5)) / (2 * a)    
    
        print("A primeira raiz da equação é: ", primeiraRaiz)
        print("A segunda raiz da equação é: ", segundaRaiz)
    
    
print(equacaoQuadratica())
