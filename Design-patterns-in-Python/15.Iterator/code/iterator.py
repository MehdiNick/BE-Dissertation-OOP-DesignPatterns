from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class SkipTraverse(Iterator):
    _position = 0

    def __init__(self, collections):
        self.collections = collections

    def __next__(self):
        try:
            value = self.collections[self._position]
            self._position += 2
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[str]):
        self._collection = collection

    def __iter__(self):
        return SkipTraverse(self._collection)


words = WordsCollection(["this", "doesn't", "make", "any", "sense"])
print("\n".join(words))
