from __future__ import annotations
from abc import ABC, abstractmethod


class DatePickerFactory(ABC):
    @abstractmethod
    def createDateBox(self):
        return

    @abstractmethod
    def createDateScroller(self):
        return


class DateBox(ABC):
    @abstractmethod
    def dateBox(self):
        return


class DateScroller(ABC):
    @abstractmethod
    def dateScroller(self):
        return


class JSDateBox(DateBox):
    def dateBox(self):
        print("a datebox is created in javascript")


class JavaDateBox(DateBox):
    def dateBox(self):
        print("a datebox is created in java")


class JSDateScroller(DateScroller):
    def dateScroller(self):
        print("a date Scroller is created in javascript")


class JavaDateScroller(DateScroller):
    def dateScroller(self):
        print("a date Scroller is created in java")


class JSDatePickerFactory(DatePickerFactory):

    def createDateBox(self):
        self.DateBox = JSDateBox()

    def createDateScroller(self):
        self.DateBox = JSDateScroller()


class JavaDatePickerFactory(DatePickerFactory):

    def createDateBox(self):
        self.DateBox = JavaDateBox()
        self.DateBox.dateBox()

    def createDateScroller(self):
        self.DateBox = JavaDateScroller()
        self.DateBox.dateScroller()


javadatepicker = JavaDatePickerFactory()
javadatepicker.createDateBox()
javadatepicker.createDateScroller()
