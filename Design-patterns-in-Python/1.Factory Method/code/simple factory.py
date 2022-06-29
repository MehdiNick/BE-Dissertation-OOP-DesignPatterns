class InstrumentSetter:
    myInstrument = None

    def setInstrument(self, instrumentType):
        if(instrumentType == "Piano"):
            self.myInstrument = Piano()
        elif(instrumentType == "Guitar"):
            self.myInstrument = Guitar()
        elif(instrumentType == "Drums"):
            self.myInstrument = Drums()

        return self.myInstrument


class Piano:
    def order(self):
        print("a piano is ordered!")

    def play(self):
        print("piano ♫♪♪")

    def warranty(self):
        print("drums are warranteed for ten years")


class Guitar:
    def order(self):
        print("a guitar is ordered!")

    def play(self):
        print("guitar ♫♪♪")

    def warranty(self):
        print("drums are warranteed for two years")


class Drums:
    def order(self):
        print("a set of drums is ordered!")

    def play(self):
        print("drums ♫♪♪")

    def warranty(self):
        print("drums are warranteed for one year")


class MusicStore:
    factory = None
    instrument = None

    def __init__(self, factory: InstrumentSetter):
        self.factory = factory

    def order(self, type):
        self.instrument = self.factory.setInstrument(type)
        self.instrument.play()


facotry = InstrumentSetter()
mystore = MusicStore(facotry)
mystore.order("Piano")
