from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class State(ABC):

    @abstractmethod
    def action1(self, states):
        pass

    @abstractmethod
    def action2(self, states):
        pass


class A(State):
    def action1(self, states):
        return states["B"]

    def action2(self, states):
        return states["C"]


class B(State):
    def action1(self, states):
        return states["B"]

    def action2(self, states):
        return states["C"]


class C(State):
    def action1(self, states):
        return states["A"]

    def action2(self, states):
        return states["C"]


class StateMachine():
    _states: Dict[State]
    _state: State = None

    def __init__(self, states: Dict[State], initalStateKey: str):
        self._states = states
        self._state = states[initalStateKey]

    def action1(self):
        print(self.getNameofState()+"----action1---->", end="")
        self._state = self._state.action1(self._states)
        print(self.getNameofState())

    def action2(self):
        print(self.getNameofState()+"----action2---->", end="")
        self._state = self._state.action2(self._states)
        print(self.getNameofState())

    def getNameofState(self):
        name = str(type(self._state))
        return (name[name.find(".")+1:name.find(".")+2])


myStateMachine = StateMachine({"A": A(), "B": B(), "C": C()}, "A")

myStateMachine.action1()
myStateMachine.action1()
myStateMachine.action2()
myStateMachine.action2()
myStateMachine.action1()
myStateMachine.action2()
