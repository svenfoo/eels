import zipfile

class Importer:
    def __init__(self, filename):
        self.file = zipfile.ZipFile(filename)

    @property
    def items(self):
        return self.file.infolist()

    def open(self, info):
        return self.file.open(info)

class Exporter:
    def __init__(self, filename):
        self.file = zipfile.ZipFile(filename, "w")

    def add(self, info, content):
        self.file.writestr(info, content)

    def write(self):
        self.file.close()
