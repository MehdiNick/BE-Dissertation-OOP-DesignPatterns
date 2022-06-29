from abc import ABC, abstractmethod


class TargetLanguage(ABC):
    @abstractmethod
    def translate():
        pass

    @abstractmethod
    def narrate():
        pass


class Text:
    text: str

    def __init__(self, txt):
        self.text = txt

    def download(self):
        return self.text


class Audio:
    filename: str
    fileformat: str
    narrator: str

    def __init__(self, name, fileformat, narrator):
        self.filename = name
        self.fileformat = fileormat
        self.narrator = narrator

    def download(self):
        return self.text + self.fileformat + "\n Narration by:" + self.narrator


class ToFarsi(TargetLanguage):
    def translate(self, txt):
        self.translation = Text("متن ترجمه شده!")
        return self.translation.download()

    def narrate():
        pasself.narration = Audio("Farsi-narration", "mp3", "Hootan Shakiba")
        return self.narration.download()


class ToItalian(TargetLanguage):
    def translate(self, txt):
        self.translation = Text("testo tradotto")
        return self.translation.download()

    def narrate():
        pasself.narration = Audio("Italian-narration", "mp3", "Carlo Sabatini")
        return self.narration.download()


class TranslatorApp:
    builder: TargetLanguage

    def __init__(self, builder):
        self.builder = builder

    def translate(self, txt):
        print(self.builder.translate(txt))

    def narrate(self, txt):
        print(self.builder.narrate(txt))

    def changeBuilder(self, builder):
        self.builder = builder


FarsiTranslationBuilder = ToItalian()
translationDirector = TranslatorApp(FarsiTranslationBuilder)
translationDirector.translate("translated text")
