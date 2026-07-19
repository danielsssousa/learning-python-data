# O *args sera uma exelente ferramentas para auxiliar na criacao deuma funcao na qual nao se sabe quantos argumentos sera solicitada pelo usuario.

#def testar_arg(*args):
   # print(args)
   # print(type(args))
    
def somar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
    
#testar_arg('nome', 13, True)


print(somar(20, 20, 20, 7))