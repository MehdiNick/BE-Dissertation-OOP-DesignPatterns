from abc import ABC, abstractmethod


class SurveyForm(ABC):

    def create(self):
        self.anotherTextBox()
        self.reviewBox()
        self.submitButton()

    def reviewBox(self):
        print("a review box⬜")

    def submitButton(self):
        print("a submit button🅾")

    @abstractmethod
    def anotherTextBox(self):
        pass


class MySurvey(SurveyForm):
    def anotherTextBox(self):
        print("name box 🆎")


mySurvey = MySurvey()
mySurvey.create()
