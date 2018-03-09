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
        HTMLParser.__init__(self)
        self.translator = translator
        self.output = ""
        self.paragraph = ""


    def translate(self, content):
        self.feed(content)
        self.close()
        self.flush
        print(self.output)
        return self.output


    def flush(self):
        if self.paragraph:
            translation = self.translator.translateSentence(self.paragraph)
            self.output += translation
            self.paragraph = ""


    def add(self, str):
        self.flush()
        self.output += str


    def decl(self, decl):
        self.add(output = "<!" + decl + ">")


    def startTag(self, tag, attrs):
        output = "<" + tag
        for name, value in attrs:
            output += " " + name + "=\"" + value + "\""
        output += ">"
        self.add(output)


    def endTag(self, tag):
        output = "</" + tag + ">"
        self.add(output)


    def data(self, data):
        self.paragraph += data


    def handle_decl(self, decl):
        self.decl(decl)


    def handle_starttag(self, tag, attrs):
        if tag != "span":
            self.startTag(tag, attrs)


    def handle_endtag(self, tag):
        if tag != "span":
            self.endTag(tag)


    def handle_data(self, data):
        self.data(data)

