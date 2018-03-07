import pydeepl

class Translator:
    def __init__(self, dest, outputLanguage, inputLanguage):
        self.dest = dest
        self.outputLanguage = outputLanguage
        self.inputLanguage = inputLanguage

    def translate(self, info, content):
        self.dest.add(info, content)



