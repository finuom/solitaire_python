import random

# Definição da carta
class Carta:
    naipes = ['♥', '♦', '♣', '♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f'{self.valor}{self.naipe}'

# Classe para o baralho
class Baralho:
    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in Carta.naipes for valor in Carta.valores]
        random.shuffle(self.cartas)

    def distribuir(self):
        tableau = [Pilha('tableau') for _ in range(7)]
        for i in range(7):
            for j in range(i, 7):
                tableau[j].empilhar(self.cartas.pop())
        estoque = self.cartas
        return tableau, estoque

# Classe para pilhas (pilhas de base, tableau e estoque)
class Pilha:
    def __init__(self, tipo):
        self.cartas = []
        self.tipo = tipo  # 'tableau', 'base', 'estoque', etc.

    def empilhar(self, carta):
        self.cartas.append(carta)

    def desempilhar(self):
        return self.cartas.pop() if self.cartas else None

    def topo(self):
        return self.cartas[-1] if self.cartas else None

# Classe principal do jogo
class JogoPaciência:
    def __init__(self):
        self.baralho = Baralho()
        self.tableau, self.estoque = self.baralho.distribuir()

        # Pilhas de base para cada naipe
        self.base = {naipe: Pilha('base') for naipe in Carta.naipes}

        # Pilha de estoque
        self.estoque_pilha = Pilha('estoque')
        for carta in self.estoque:
            self.estoque_pilha.empilhar(carta)

    def mover_carta(self, origem, destino):
        carta = origem.desempilhar()
        if carta:
            destino.empilhar(carta)
            return True
        return False

    def jogar(self):
        while True:
            self.exibir_jogo()

            # Aqui, você pode adicionar a lógica para capturar entradas do usuário e processá-las.
            acao = input("Escolha uma ação (mover, pegar, sair): ")

            if acao == 'mover':
                # Exemplo de movimento de cartas entre pilhas.
                origem = int(input("Escolha a pilha de origem (1-7): ")) - 1
                destino = int(input("Escolha a pilha de destino (1-7 ou 0 para estoque): ")) - 1

                if origem >= 0 and origem < 7 and destino >= 0 and destino < 7:
                    if not self.mover_carta(self.tableau[origem], self.tableau[destino]):
                        print("Movimento inválido.")
                else:
                    print("Entrada inválida.")
            elif acao == 'pegar':
                carta = self.estoque_pilha.desempilhar()
                if carta:
                    print(f"Você pegou a carta {carta}")
                else:
                    print("Sem cartas no estoque.")
            elif acao == 'sair':
                print("Saindo do jogo...")
                break
            else:
                print("Comando inválido.")

    def exibir_jogo(self):
        print("\n--- Jogo de Paciência ---")
        for i, pilha in enumerate(self.tableau):
            print(f"Pilha {i+1}: {', '.join(str(carta) for carta in pilha.cartas)}")

        print("\nEstoque:")
        if self.estoque_pilha.cartas:
            print(f"Topo do estoque: {self.estoque_pilha.topo()}")
        else:
            print("Sem cartas no estoque.")

        print("\nBases:")
        for naipe, pilha in self.base.items():
            print(f"{naipe}: {' '.join(str(carta) for carta in pilha.cartas)}")

# Rodando o jogo
if __name__ == "__main__":
    jogo = JogoPaciência()
    jogo.jogar()