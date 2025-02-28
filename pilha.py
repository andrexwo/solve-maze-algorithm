# criação da classe pilha, implementada em python para a disciplina de Estrutura de Dados



class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar (self, dado):
        novo_no = No(dado)
        novo_no.prox = self.topo
        self.topo = novo_no

    def vazia(self):
        return self.topo is None

    def desempilhar(self):
        if self.vazia():
            raise IndexError("a pilha está vazia!")
        dado = self.topo.dado
        self.topo = self.topo.prox
        return dado

    def get_topo(self):  # mudei o nome para evitar conflitos
        if self.vazia():
            raise IndexError("a pilha está vazia!")
        return self.topo.dado  # acesso diretamente o dado

    def imprimeLista(self):
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(atual.dado)
            atual = atual.prox
        print(" -> ".join(map(str, elementos)))
