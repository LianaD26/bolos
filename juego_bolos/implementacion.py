class Game:
    def _init_(self):
        self.frames = []  # frames

    def score(self):   # puntaje
        total = 0
        for frame in self.frames:
            total += frame.score()
        return total


class Frame:
    def _init_(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(Roll(pins))

    def score(self):
        total = 0
        for roll in self.rolls:
            total += roll.score()
        # Si el frame es un spare, se suma el puntaje del primer roll del siguiente frame
        if self.is_spare():
            next_frame = self.frames[self.frames.index(self) + 1]
            total += next_frame.rolls[0].score()
        return total

    def is_spare(self):
        return len(self.rolls) == 2 and self.score() == 10


class Roll:
    def _init_(self, pins):
        self.pins = pins

    def score(self):
        return self.pins