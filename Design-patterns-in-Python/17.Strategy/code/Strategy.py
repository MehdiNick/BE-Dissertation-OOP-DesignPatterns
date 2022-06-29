from abc import ABC, abstractmethod


class EqualizerGenre(ABC):
    @abstractmethod
    def adjust(self):
        pass


class Classical(EqualizerGenre):
    def adjust(self):
        print("Tuned for classical genre")


class Rock(EqualizerGenre):
    def adjust(self):
        print("Tuned for Rock genre")


class Pop(EqualizerGenre):
    def adjust(self):
        print("Tuned for Pop genre")


class EqualizerApp():
    equalizerGenre: EqualizerGenre = None

    def __init__(self, defaultGenre: EqualizerGenre):
        self.equalizerGenre = defaultGenre

    def play(self):
        self.equalizerGenre.adjust()
        name = str(type(self.equalizerGenre))
        name = name[name.find(".")+1:name.rfind("'")]
        print(f"the music is playing. Equalizer On:{name}\n")

    def changeGenre(self, genre: EqualizerGenre):
        self.equalizerGenre = genre
        self.play()


rock = Rock()
classical = Classical()
pop = Pop()
app = EqualizerApp(pop)
app.play()
app.changeGenre(rock)
