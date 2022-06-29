class CameraApp:
    def __init__(self, data):
        self.data = data

    def takePicture(self):
        self.facade = ProcessingFacade(self.data)
        print(self.facade.output())


class ImageProcessing:
    def __init__(self, rawData):
        self.rawData = rawData

    def process(self):
        self.result = f"Processed Data+-{self.rawData}"
        return self


class Modification:
    def __init__(self, imageProcessing):
        self.imageProcessing = imageProcessing

    def modify(self):
        self.result = f"Modified Data**{self.imageProcessing.result}"
        return self


class Output:
    def __init__(self, finalData):
        self.finalData = finalData

    def export(self):
        return "Image Ready! output.jpg"


class ProcessingFacade:
    def __init__(self, rawData):
        self.processed = ImageProcessing(rawData).process()
        self.modified = Modification(self.processed).modify()
        self.result = Output(self.modified).export()

    def output(self):
        return self.result


camera = CameraApp("101010011111011100111101100101101111010110")
camera.takePicture()


onlyProcessedImage = ImageProcessing(
    "101010011111011100111101100101101111010110").process().result

print(onlyProcessedImage)
