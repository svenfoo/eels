import pydeepl

class Translator:
    def __init__(self, dest, outputLanguage, inputLanguage):
        self.dest = dest
        self.outputLanguage = outputLanguage
        self.inputLanguage = inputLanguage

    def translate(self, info, content):
        translation = ""
        for bytesLine in content.read().split(b"\n"):
            line = bytesLine.decode("utf-8")
            translatedLine = self.translateSentence(line);
            print(translatedLine)
            translation += translatedLine
        self.dest.add(info, translation)

    def translateSentence(self, sentence):
        return pydeepl.translate(sentence, self.outputLanguage, from_lang=self.inputLanguage)
