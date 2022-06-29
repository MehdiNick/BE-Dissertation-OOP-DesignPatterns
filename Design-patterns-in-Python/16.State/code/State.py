from abc import ABC, abstractmethod


class ConnectionState(ABC):
    @abstractmethod
    def loadImages(self):
        pass

    @abstractmethod
    def loadVideos(self):
        pass


class Offline(ConnectionState):
    def loadImages(self):
        print("don't even try")

    def loadVideos(self):
        print("don't even try")


class Wifi(ConnectionState):
    def loadImages(self):
        print("download all images ")

    def loadVideos(self):
        print("download all videos ")


class Data(ConnectionState):
    def loadImages(self):
        print("download half of images ")

    def loadVideos(self):
        print("download no videos ")


class Connection:
    _connectionState = Offline()

    def setConnectionState(self, connectionState: ConnectionState):
        self._connectionState = connectionState

    def load(self):
        self._connectionState.loadImages()
        self._connectionState.loadVideos()


connection = Connection()
connection.load()
data = Data()

connection.setConnectionState(data)
connection.load()
