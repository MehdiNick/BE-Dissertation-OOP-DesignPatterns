from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, narrator, fCover, bCover):
        self.title = title
        self.author = author
        self.narrator = narrator
        self.fCover = fCover
        self.bCover = bCover


class Album:
    def __init__(self, title, singer, composer):
        self.title = title
        self.singer = singer
        self.composer = composer


class Podcast:
    def __init__(self, title, hostess, episode, sponser):
        self.title = title
        self.hostess = hostess
        self.episode = episode
        self.sponser = sponser


class PageInfo:
    def title():
        pass

    def creator():
        pass

    def metaInfo():
        pass

    def cover():
        pass


class BookPageInfo(PageInfo):
    def __init__(self, book: Book):
        self.book = book

    def title(self):
        print(f"***{self.book.title}***")

    def creator(self):
        print(f"Author:{self.book.author}")

    def metaInfo(self):
        self.narrator()
        self.biography()

    def cover(self):
        print(
            f"front cover:{self.book.fCover} | back cover: {self.book.bCover}")

    def biography(self):
        print("Here comes the biography!")

    def narrator(self):
        print(f"The narrator is {self.book.narrator}")


class AlbumPageInfo(PageInfo):
    def __init__(self, album: Album):
        self.album = album

    def title(self):
        print(f"***{self.album.title}***")

    def creator(self):
        print(f"Singer:{self.album.singer}")

    def metaInfo(self):
        self.discography()
        self.composer()

    def cover(self):
        print(f"Album cover:{self.album.cover} ")

    def discography(self):
        print("Here comes the discography!")

    def composer(self):
        print(f"The composer is {self.album.composer}")


class PodcastPageInfo(PageInfo):
    def __init__(self, podcast: Podcast):
        self.podcast = podcast

    def title(self):
        print(f"***{self.podcast.title}***")

    def creator(self):
        print(f"Hostess:{self.book.hostess}")

    def metaInfo(self):
        self.sponser()
        self.episode()

    def cover(self):
        print(f"Podcast cover:{self.podcast.cover} ")

    def sponser(self):
        print(f"Today's podcast's sponser is {self.podcast.sponser}")

    def episode(self):
        print(f"Today's episode is about {self.podcast.episode}")


class View(ABC):
    def __init__(self, pageInfo: PageInfo):
        self.pageInfo = pageInfo

    @abstractmethod
    def show(self):
        pass


class ComprehensiveView(View):
    def show(self):
        self.pageInfo.title()
        self.pageInfo.creator()
        self.pageInfo.cover()
        self.pageInfo.metaInfo()


class SimpleView(View):
    def show(self):
        self.pageInfo.title()
        self.pageInfo.creator()
        self.pageInfo.cover()


class MinimalView(View):
    def show(self):
        self.pageInfo.title()
        self.pageInfo.creator()


myBook = BookPageInfo(Book("Book Title", "Book Author",
                           "Book Narrator", "Front Cover", "Back Cover"))
bigscreen = ComprehensiveView(myBook)
print("\nComprehensive View----------------------------------")
bigscreen.show()
smallscreen = SimpleView(myBook)
print("\nSimple View----------------------------------")
smallscreen.show()
myAlbum = AlbumPageInfo(Album("Album Title", "Album Singer", "Song Composer"))
minimalistic = MinimalView(myAlbum)
print("\nMinimal View----------------------------------")
minimalistic.show()
