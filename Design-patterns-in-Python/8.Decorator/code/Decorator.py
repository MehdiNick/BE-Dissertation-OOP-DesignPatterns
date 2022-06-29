from abc import ABC, abstractmethod


class ElementView(ABC):
    @abstractmethod
    def show(self):
        pass


class TextView(ElementView):
    def show(self):
        print("Text is being shown")


class PictureView(ElementView):
    def show(self):
        print("Picture is being shown")


class Decorator(ElementView, ABC):
    def __init__(self, elementView):
        self.elementView = elementView


class Border(Decorator):
    def show(self):
        self.border()

    def border(self):
        print("----------------------------------------------")
        self.elementView.show()
        print("---------------------------------------------- \n")


class Scroll(Decorator):
    def show(self):
        self.scroll()

    def scroll(self):
        print("Scroller Added +++++++++++++++++++++++++++++++++")
        self.elementView.show()
        print("\n")


textWithBorder = Border(TextView())
textWithBorder.show()

textwithScroll = Scroll(TextView())
textwithScroll.show()

pictureWithBorderAndScroll = Scroll(Border(PictureView()))
pictureWithBorderAndScroll.show()
