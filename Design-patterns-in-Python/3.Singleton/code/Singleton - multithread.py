import os
import time
from multiprocessing import Process
from threading import Thread, current_thread, Lock
import random


class SingletonMeta(type):
    _classInstances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if(cls not in cls._classInstances):
                instance = super().__call__(*args, **kwargs)
                cls._classInstances[cls] = instance

        return cls._classInstances[cls]


class OpticalDrive(metaclass=SingletonMeta):
    isEmpty = True

    def read(self, CD):
        if(self.isEmpty):
            self.isEmpty = False
            print(CD)
        else:
            print("The drive is full.")

    def eject():
        self.isEmpty = True


def createObject():
    drive = OpticalDrive()
    print(f"\n{drive}")


if(__name__ == "__main__"):
    thread1 = Thread(target=createObject, args=())
    thread2 = Thread(target=createObject, args=())
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
