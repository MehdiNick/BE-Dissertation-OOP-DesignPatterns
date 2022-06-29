from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def refresh(self):
        pass


class Tab(Component):
    def __init__(self, tabName, modules: list[Component]):
        self.tabName = tabName
        self.modules = modules

    def add(self, module: Component):
        self.modules.append(module)

    def remove(self, module: Component):
        self.modules.remove(module)

    def refresh(self):
        list(map(lambda module: module.refresh(), self.modules))


class GoalsStats(Component):
    def refresh(self):
        print("Update Goals ⚽")


class FoulsStats(Component):
    def refresh(self):
        print("Update Fouls 🔴")


class HighlightVideo(Component):
    def refresh(self):
        print("Update Highlight videos 💥⚽")


print("LiveScore - Juventus vs Inter ")
goalModule = GoalsStats()
fouldModule = FoulsStats()
highlight = HighlightVideo()
StatsTab = Tab("StatsTab", [goalModule, fouldModule])

StatsTab.refresh()
highlight.refresh()
