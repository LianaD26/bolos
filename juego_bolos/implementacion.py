class Juego:
    def __init__(self):
        self.fichas = []  # fichas

    def puntaje(self):   # puntaje
        total = 0
        for ficha in self.fichas:
            total += ficha.puntaje()
        return total


class Ficha:
    def __init__(self):
        self.tiros = []

    def agregar_tiro(self, bolos):
        self.tiros.append(Tiro(bolos))

    def puntaje(self):
        total = 0
        for tiro in self.tiros:
            total += tiro.puntaje()

        if self.es_spare(): # Si la ficha is_spare, se suma el puntaje del primer tiro de la siguiente ficha
            siguiente_ficha = self.fichas[self.fichas.index(self) + 1]
            total += siguiente_ficha.tiros[0].puntaje()
        return total

    def es_spare(self):
        return len(self.tiros) == 2 and self.puntaje() == 10


class Tiro:
    def __init__(self, bolos):
        self.bolos = bolos

    def puntaje(self):
        return self.bolos
