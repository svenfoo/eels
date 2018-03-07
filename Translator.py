import nltk.data
import pydeepl

class Translator:
    def __init__(self, dest, outputLanguage, inputLanguage):
        self.dest = dest
        self.outputLanguage = outputLanguage
        self.inputLanguage = inputLanguage

        # TODO: assumes english as input language
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def translate(self, info, content):
        translation = ""
        for sentence in self.tokenizer.tokenize(content.read()):
            translation += self.translateSentence(sentence);
        self.dest.add(info, translation)

    def translateSentence(self, sentence):
        return pydeepl.translate(sentence, self.outputLanguage, from_lang=self.inputLanguage)
