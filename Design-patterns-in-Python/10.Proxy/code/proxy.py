from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def render():
        pass


class Text(Element):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(f"Rendered Text: **** \n {self.text}")


class Picture(Element):
    def __init__(self, pic, height, width):
        self.pic = pic
        self.height = height
        self.width = width

    def render(self):
        print(
            f"\nRendered Picture:***  \n {self.pic}  -{self.height} * {self.width}")


class PicutreProxy(Element):
    def __init__(self, picture):
        self.picture = picture

    def render(self, xFactor):
        if(self.check_access(xFactor)):
            self.picture.render()
        else:
            print(
                f"\nProxy ! : \n there's a picture with the title {self.picture.pic} and the dimentions of {self.picture.height} * {self.picture.width} ")

    def check_access(self, xFactor):
       # Proxy: Checking access prior to firing a real request
        if(xFactor):
            return True
        else:
            return False


someText = Text(
    "hey this sis a sample text. you can ignore it but i wouldn't recommend ou to do so.")

aPicture = Picture("Picture of a Cow", 1080, 720)

aPictureProxy = PicutreProxy(aPicture)

someText.render()
aPictureProxy.render(False)
aPictureProxy.render(True)
