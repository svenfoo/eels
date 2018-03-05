import zipfile

class BookExporter:
    def __init__(self, filename):
        self.file = zipfile.ZipFile(filename, "w")

    def add(self, item):
        print(item)

    def write(self):
        self.file.close()
