class Fila:
    def __init__(self):
        self.elementos = []

    def vazio(self):
        return len(self.elementos) == 0

    def enfilera(self, elemento):
        self.elementos.append(elemento)

    def desenfilera(self):
        if self.vazio():
            return None
        return self.elementos.pop(0)
