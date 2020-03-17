import random
#
# lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# a = random.choice(lista)
#
# a = lista.index(a)
#
# b = lista.pop(a)
#
# print(lista)
# print(b)
# print(a)


frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
fruta_selecionada = random.choice(frutas)
lista_fruta_selecionada = ['-' for i in fruta_selecionada]
print(lista_fruta_selecionada)
print()