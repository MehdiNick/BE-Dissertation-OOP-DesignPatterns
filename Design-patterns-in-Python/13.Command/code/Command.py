from abc import ABC, abstractmethod
from termcolor import colored


class PageElement(ABC):
    @abstractmethod
    def zoomIn(self):
        pass

    @abstractmethod
    def zoomIn(self):
        pass


class Command(ABC):
    def __init__(self, receiver: PageElement):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class TextBox(PageElement):

    def zoomIn(self):
        print("font size ++ ")

    def zoomOut(self):
        print("font size -- ")


class Image(PageElement):
    def zoomIn(self):
        print("Zoomed In ")

    def zoomOut(self):
        print("Zoomed Out ")


class Button():
    do = True

    def setAction(self, operation: Command):
        self.operation = operation

    def click(self):
        if(self.do):
            self.operation.execute()
        else:
            self.operation.unexecute()

        self.do = not(self.do)


class ZoomCommand(Command):
    def execute(self):
        self.receiver.zoomIn()

    def unexecute(self):
        self.receiver.zoomOut()


textBox = TextBox()
image = Image()
imageZoom = ZoomCommand(image)
textZoom = ZoomCommand(textBox)
btn1 = Button()
btn2 = Button()
btn1.setAction(imageZoom)
btn2.setAction(textZoom)
btn1.click()
btn1.click()
btn2.click()
btn2.click()
