import os
import psutil
from termcolor import colored
import time
from abc import ABC, abstractmethod
import json
from typing import Dict


class Glyph(ABC):
    def __init__(self, ASCIICode, typography, color, size):
        self.ASCIICode = ASCIICode
        self.typography = typography
        self.color = color
        self.size = size

    @abstractmethod
    def draw(self, coordinate):
        pass


class Charcater(Glyph):
    def draw(self, coordinate):
        #print(f"{chr(int(self.ASCIICode))} at {coordinate} ({self.typography})")
        pass


class GlyphFactory:
    _glyphContext: Dict[str, Charcater] = {}

    def getCharacter(self, ASCIICode, typography, color, size):

        if self._glyphContext.get(f"{ASCIICode}{typography}{color}{size}"):
            return self._glyphContext.get(f"{ASCIICode}{typography}{color}{size}")
        else:
            newCharacter = Charcater(ASCIICode, typography, color, size)
            self._glyphContext[f"{ASCIICode}{typography}{color}{size}"] = newCharacter
            return newCharacter


glyphFactory = GlyphFactory()


def draw(ASCIICode, typography, color, size, coordinate, i):
    globals()[f"object1{i}"] = glyphFactory.getCharacter(
        ASCIICode, typography, color, size)
    globals()[f"object1{i}"].draw(coordinate)


start_time = time.time()
for i in range(500000):
    draw("69", "Times", "black", "14", (i, i), i)

process = psutil.Process(os.getpid())
print(
    colored(f"CPU TIME \n{(time.time() - start_time)} seconds", "red"))

# in Megabytes
print(
    colored(f"Memory Used \n {process.memory_info().rss/1048576} MB", "red"))


# print(f"koooon\033[94m", end="joon")
# print(colored('hello', 'red'), colored('world', 'green'))
