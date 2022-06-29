from __future__ import annotations
from abc import ABC, abstractmethod
from pprint import pprint


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer: Observer):
        return

    @abstractmethod
    def removeObserver(self, observer: Observer):
        return

    @abstractmethod
    def notifyObserver(self, observer: Observer):
        return


class WeatherStation(Subject):
    __temperature: float
    __barometricPressure: float
    __humidity: float

    def __init__(self):
        self.__observers = []

    def registerObserver(self, observer: Observer):
        self.__observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.__observers.remove(observer)

    def notifyObserver(self):
        for obj in self.__observers:
            obj.update()

    def setData(self, temperature: float, barometricPressure: float, humidity: float):
        self.__temperature = temperature
        self.__barometricPressure = barometricPressure
        self.__humidity = humidity
        self.notifyObserver()

    def getTemperature(self):
        return self.__temperature

    def getPressure(self):
        return self.__barometricPressure

    def getHumidity(self):
        return self.__humidity


class Observer(ABC):
    @abstractmethod
    def update():
        return


class displayPage(ABC):
    @abstractmethod
    def display():
        pass


class CurrentWeatherSoftware(Observer, displayPage):
    __temperature: float
    __barometricPressure: float
    __humidity: float
    __weatherStation: WeatherStation

    def __init__(self, weatherStationObj):
        self.__weatherStation = weatherStationObj
        self.__weatherStation.registerObserver(self)

    def update(self):
        self.__temperature = self.__weatherStation.getTemperature()
        self.__barometricPressure = self.__weatherStation.getPressure()
        self.__humidity = self.__weatherStation.getHumidity()

    def display(self):
        print("The current Weather Info: \nTemperature:{0} \nPressure:{1} \nHumidity:%{2}".format(
            self.__temperature, self.__barometricPressure, self.__humidity))


class AverageWeatherSoftware(Observer, displayPage):
    __temperature: float
    __barometricPressure: float
    __humidity: float
    __weatherStation: WeatherStation

    def __init__(self, weatherStationObj):
        self.__weatherStation = weatherStationObj
        self.__weatherStation.registerObserver(self)

    def update(self):
        self.__temperature = self.__weatherStation.getTemperature()
        self.__barometricPressure = self.__weatherStation.getPressure()
        self.__humidity = self.__weatherStation.getHumidity()

    def display(self):
        print("displays the average Temperature, Pressure and Humidity")


class WeatherForecast(Observer, displayPage):
    __temperature: float
    __barometricPressure: float
    __humidity: float
    __weatherStation: WeatherStation

    def __init__(self, weatherStationObj):
        self.__weatherStation = weatherStationObj
        self.__weatherStation.registerObserver(self)

    def update(self):
        self.__temperature = self.__weatherStation.getTemperature()
        self.__barometricPressure = self.__weatherStation.getPressure()
        self.__humidity = self.__weatherStation.getHumidity()

    def display(self):
        print("displays the weather forecast")


RashtWeatherStation = WeatherStation()
CurrentWeatherSoftware = CurrentWeatherSoftware(RashtWeatherStation)
RashtWeatherStation.setData(9, 1021, 70)
CurrentWeatherSoftware.display()
RashtWeatherStation.setData(7, 1018.5, 80)
CurrentWeatherSoftware.display()
