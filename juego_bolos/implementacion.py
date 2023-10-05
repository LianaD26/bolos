from abc import ABC, abstractmethod

class ElementoJuego(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def puntaje(self):
        pass

class Juego(ElementoJuego):
    def __init__(self):
        super().__init__()
        self.fichas = []

    def puntaje(self):
        total = 0
        for ficha in self.fichas:
            total += ficha.puntaje()
        return total

class Ficha(ElementoJuego):
    def __init__(self):
        super().__init__()
        self.tiros = []

    def agregar_tiro(self, bolos):
        self.tiros.append(Tiro(bolos))

    def puntaje(self):
        total = 0
        for tiro in self.tiros:
            total += tiro.puntaje()
        if self.es_spare():
            total += self.siguiente_ficha().primer_tiro().puntaje()
        return total

    def es_spare(self):
        return len(self.tiros) == 2 and self.puntaje() == 10

    def siguiente_ficha(self):
        if self.juego() is not None:
            indice_actual = self.juego().fichas.index(self)
            if indice_actual < len(self.juego().fichas) - 1:
                return self.juego().fichas[indice_actual + 1]
        return None

    def juego(self):
        if isinstance(self, Juego):
            return self
        return None

class Tiro(ElementoJuego):
    def __init__(self, bolos):
        super().__init__()
        self.bolos = bolos

    def puntaje(self):
        return self.bolos

