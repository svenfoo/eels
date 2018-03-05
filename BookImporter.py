import zipfile

class BookImporter:
    def __init__(self, filename):
        self.file = zipfile.ZipFile(filename)

    @property
    def items(self):
        return self.file.infolist()
