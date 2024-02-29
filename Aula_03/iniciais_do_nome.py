def iniciais(nome):
    palavras = nome.split()
    iniciais = ""
    for palavra in palavras:
        iniciais += palavra[0]
    return(iniciais)

nome = input("Digite seu nome: \n")
print(iniciais(nome))
