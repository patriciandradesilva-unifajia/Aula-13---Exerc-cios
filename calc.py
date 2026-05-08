def soma (a, b):
    return (a+b)

def subtracao (a, b):
    return (a-b)    

def multiplicacao (a, b):
    return (a*b)

def divisao (a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    else:
        return (a/b)

def potencia (a, b):
    return (a**b)

def raiz (a, b):
    if a < 0:
        return "Não é possível calcular a raiz de um número negativo"
    else:
        return (a**(1/b))
       