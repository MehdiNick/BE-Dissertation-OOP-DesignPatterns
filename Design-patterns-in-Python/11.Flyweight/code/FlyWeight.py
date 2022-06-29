import os
import psutil


from termcolor import colored
import time


class Letter:
    def __init__(self, ASCIICode, typography, color, size, coordinate):
        self.ASCIICode = ASCIICode
        self.typography = typography
        self.color = color
        self.size = size
        self.coordinate = coordinate

    def draw(self):
        pass


start_time = time.time()
for i in range(500000):
    globals()[f"object1{i}"] = Letter("69", "A", "black", "12", [i, i])

process = psutil.Process(os.getpid())
print(
    colored(f"CPU TIME \n{(time.time() - start_time)} seconds", "red"))

# in Megabytes
print(
    colored(f"Memory Used \n {process.memory_info().rss/1048576} MB", "red"))


# print(f"koooon\033[94m", end="joon")
# print(colored('hello', 'red'), colored('world', 'green'))
