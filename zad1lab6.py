class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Elektryczny(Samochod):
    def __init__(self, marka, model, zasieg):
        super().__init__(marka, model)
        self.zasieg = zasieg

class Sportowy(Samochod):
    def __init__(self, marka, model, vmax):
        super().__init__(marka, model)
        self.vmax = vmax
class ElektrycznySportowy(Elektryczny, Sportowy):
    def __init__(self, marka, model, zasieg, vmax):
        Elektryczny.__init__(self, marka, model, zasieg)
        Sportowy.__init__(self, marka, model, vmax)

    def info(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Zasięg: {self.zasieg}")
        print(f"Maksymalna prędkość: {self.vmax}")

car = ElektrycznySportowy("BMW", "M3", 200, 300)
car.info()
