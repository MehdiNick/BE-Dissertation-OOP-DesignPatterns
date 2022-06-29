from abc import ABC, abstractmethod


class MediCarFactory(ABC):
    @abstractmethod
    def createCar(self, carName):
        return


class CanadaFactory(MediCarFactory):
    def createCar(self, carName):
        if(carName == "M1"):
            return M1(2, 252, 180, 26000)
        elif(carName == "M2"):
            return M2(1.5, 150, 140, 20000)
        else:
            return M2X(1.5, 150, 140, 22000)


class IranFactory(MediCarFactory):
    def createCar(self, carName):
        if(carName == "M1"):
            return M1(1.5, 180, 140, 56000000)
        elif(carName == "M2"):
            return M2(1.5, 150, 100, 46000000)
        else:
            return M2X(1.5, 135, 150, 50000000)


class Medi:
    registerationNumber = 598632
    name = "Medi Motors .Co"

    def __init__(self, factory: MediCarFactory):
        self.factory = factory

    def order(self, carName):
        self.car = self.factory.createCar(carName)
        self.car.build()
        self.car.deliver()
        self.car.specs()


class MediCars(ABC):
    type: str
    engineSize: float
    torque: int
    horsepower: int
    price: int

    def __init__(self, engineSize: float, torque: int, horsepower: int, price: int):
        self.engineSize = engineSize
        self.torque = engineSize
        self.horsepower = horsepower
        self.price = price

    def specs(self):
        print("Specs: \n engineSize:{0} \n horsepower:{1} \n torque:{2} \n price:{3}".format(
            self.engineSize, self.horsepower, self.torque, self.price))

    @abstractmethod
    def build(self):
        return

    @abstractmethod
    def deliver(self):
        return


class M1(MediCars):
    type: "Crossover"

    def build(self):
        print("Your M1 is being built")

    def deliver(self):
        print("Here's your brand new M1 ^^")


class M2(MediCars):
    type: "Sedan"

    def build(self):
        print("M2 is being built")

    def deliver(self):
        print("Here's your brand new M2 ^^")


class M2X(MediCars):
    type: "Hatchback"

    def build(self):
        print("M2X is being built")

    def deliver(self):
        print("Here's your brand new M2X ^^")


IranFactory = Medi(IranFactory())
IranFactory.order("M1")
