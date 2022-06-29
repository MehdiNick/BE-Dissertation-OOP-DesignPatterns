from __future__ import annotations
import copy
from typing import Any, List


class Prototype():
    def clone(self):
        return copy.copy(self)


class ScreenSaver(Prototype):
    _design = None
    _colors: List[str] = None

    def __init__(self, designFunction, colors):
        self._design = designFunction
        self._colors = colors

    def addColor(self, color):
        self._colors.append(color)

    def draw(self):
        self._design(self._colors)


screenSaver1 = ScreenSaver(lambda colors: [print(
    f"The design is made with the color {i}") for i in colors], ["green", "yellow"])
screenSaver1.draw()
print("-------------")
screenSaver2 = screenSaver1.clone()
screenSaver2.addColor("blue")
screenSaver2.draw()
