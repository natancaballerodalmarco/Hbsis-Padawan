import time
import random

class Forca:
    def __init__(self):
        frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
        self.nova_jogada(frutas)


    def nova_jogada(self, frutas:list):
        verificar_erros = 0
        fruta_selecionada = random.choice(frutas)
        self.letras_escolhidas = ['_' for i in fruta_selecionada]

        while True:
            letra_escolhida = self.escolher_letra()
            verificar_acerto = self.verificar_letra_existente(letra_escolhida, fruta_selecionada)
            if verificar_acerto:
                print(f'Você acertou, a palavra ficou: {self.letras_escolhidas}')
                if not '_' in self.letras_escolhidas:
                    print('Voce Ganhou!!')
                    break
                continue
            else:
                verificar_erros += 1
                if verificar_erros == 5:
                    print('Voce Perdeu!!')
                    print(f'A palavra era {fruta_selecionada}')
                    break
                print('Você errou a letra!!')
    def escolher_letra(self):
        letra = str(input('Digite uma letra: '))
        return letra

    def verificar_letra_existente(self, letra:str, fruta_string:str):
        fruta = [i for i in fruta_string]
        if fruta.count(letra) > 0:
            for i in fruta:
                if i == letra:
                    index = fruta.index(i)
                    self.letras_escolhidas[index] = letra
                    fruta[index] = ''

            return True

        return False

f = Forca()
