import zipfile

class BookExporter:
    def __init__(self, filename):
        self.file = zipfile.ZipFile(filename, "w")

    def add(self, info, content):
        print('writing', info)
        self.file.writestr(info, content.read())

    def write(self):
        self.file.close()
