import random
import time

class BlackJack:
    def __init__(self):
        self.lista_possiveis_ganhadores = []
        self.lista_jogadores = []
        self.baralho = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J'] * 4
        for i in range(5):
            print('Virando carta para descartar...')
            time.sleep(1)
            print(f'A carta descartada é: {self.sortear_carta()}')
            time.sleep(0.5)
        self.numero_jogadores = int(input('Quantia de Jogadores: '))
        for i in range(self.numero_jogadores):
            self.lista_jogadores.append(input('Nome de jogador: '))
            print(f'Vez de {self.lista_jogadores[i]}')
            self.rodadas()
        self.resultado_ganhador()


    def rodadas(self):
        mao_jogador = []
        soma_mao_jogador = 0

        carta_sorteada = self.sortear_carta()
        soma_mao_jogador += self.verificacao_soma(mao_jogador, carta_sorteada)
        mao_jogador.append(carta_sorteada)

        resposta = True
        while resposta:
            carta_sorteada = self.sortear_carta()
            soma_mao_jogador += self.verificacao_soma(mao_jogador, carta_sorteada)
            mao_jogador.append(carta_sorteada)
            print(mao_jogador)
            print(soma_mao_jogador)
            resposta = self.verificar_vitoria(soma_mao_jogador)
            if resposta == 'Perdeu':
                break
            resposta = self.verificar_resposta(input('responda: '))
        self.lista_possiveis_ganhadores.append(soma_mao_jogador)


    def sortear_carta(self):
        carta_descarte = random.choice(self.baralho)
        self.baralho.pop(self.baralho.index(carta_descarte))
        return carta_descarte


    def verificacao_soma(self, mao, carta):
        if type(carta) == str:
            if carta == 'A':
                for i in mao:
                    if type(i) == int:
                        return 1
            if carta == 'Q' or carta == 'J' or carta == 'K':
                return 10
            return 11

        a = mao.count('A')
        for i in mao:
            if type(i) == int:
                return carta

        return carta - (10*a)

    def verificar_resposta(self, resposta):
        if resposta.lower() == 'hit':
            return True

        return False


    def verificar_vitoria(self, soma):
        if soma < 21:
            return True
        elif soma == 21:
            print('Você Ganhou')
        else:
            print('Você Perdeu')
            return 'Perdeu'


    def resultado_ganhador(self):
        a = 0
        lista_ganhadores = []
        for i, j in enumerate(self.lista_possiveis_ganhadores):
            if a < j < 22:
                lista_ganhadores.clear()
                lista_ganhadores.append(self.lista_jogadores[i])
            elif a == j:
                lista_ganhadores.append(self.lista_jogadores[i])
            else:
                continue
        print(lista_ganhadores)

b = BlackJack()
