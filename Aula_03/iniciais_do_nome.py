- SOLUÇÃO_01:

def iniciais(nome):
    palavras = nome.split()
    iniciais = ""
    for palavra in palavras:
        iniciais += palavra[0]
    return(iniciais)

nome = input("Digite seu nome: \n")
print(iniciais(nome))

- SOLUÇÃO_02:

def iniciais(nome):
    palavras = nome.split()
    iniciais = [palavra[0] for palavra in palavras]
    return (iniciais)

nome = input("Digite seu nome: ")
print(iniciais(nome))
