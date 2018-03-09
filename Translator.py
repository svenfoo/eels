from html.parser import HTMLParser
import pydeepl

class Translator:
    def __init__(self, outputLanguage, inputLanguage):
        self.outputLanguage = outputLanguage
        self.inputLanguage = inputLanguage


    def translateSentence(self, sentence):
        return pydeepl.translate(sentence, self.outputLanguage, from_lang=self.inputLanguage)


    def translateHTML(self, content):
        return HTMLTranslator(self).translate(content)


class HTMLTranslator(HTMLParser):
    def __init__(self, translator):
        super.__init__(self)
        self.translator = translator
        self.translation = ""


    def translate(self, content):
        self.feed(content)


    def add(self, str):
        self.translation += str


    def handle_starttag(self, tag, attrs):
        output = "<" + tag
        for name, value in attrs:
            output += " " + name + "=\"" + value + "\""
        output += ">"
        self.add(output)


    def handle_endtag(self, tag):
        output = "</" + tag + ">"
        self.add(output)


    def handle_data(self, data):
        output = self.translator.translateSentence(data)
        self.add(output)

