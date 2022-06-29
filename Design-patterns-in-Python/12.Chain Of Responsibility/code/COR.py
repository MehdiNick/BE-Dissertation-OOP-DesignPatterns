from __future__ import annotations

from abc import ABC, abstractmethod


class HelpHandler(ABC):
    _successor: HelpHandler

    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def showInfo(self):
        pass

    def handleHelpInfo(self):
        if(self.condition()):
            self.showInfo()
        else:
            if(self._successor):
                self._successor.showInfo()
            return False

    def condition(self):
        if(hasattr(self, 'info')):
            return True
        else:
            return False

    def setInfo(self, info):
        self.info = info


class Application(HelpHandler):

    def showInfo(self):
        print(f"Application: {self.info}")


class CommentPage(HelpHandler):
    def showInfo(self):
        print(f"CommentPage: {self.info}")


class Button(HelpHandler):
    def showInfo(self):
        print(f"Button: {self.info}")


application = Application()
application.setInfo("This is just a test application")
commentPage = CommentPage(application)
commentPage.setInfo("You can send your comment in this page")
button1 = Button(commentPage)
button2 = Button(commentPage)
button2.setInfo("this is the second button which includes help info")
button1.handleHelpInfo()
button2.handleHelpInfo()
