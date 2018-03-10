from html.parser import HTMLParser

import pydeepl
from pydeepl import TranslationError

import time

class Translator:
    def __init__(self, outputLanguage, inputLanguage, throttle = 0):
        self.outputLanguage = outputLanguage
        self.inputLanguage = inputLanguage
        if throttle > 0:
            self.throttle = lambda : time.sleep(throttle)


    def translateWithErrorHandling(self, sentence):
        try:
            self.throttle()
            return pydeepl.translate(sentence, self.outputLanguage, from_lang=self.inputLanguage)
        except (TranslationError, IndexError) as error:
            print("Error trying to translate", "\""+ sentence + "\"")
            print(format(error))
            raise pydeepl.TranslationError(error)


    def translateSentence(self, sentence):
        sentence = sentence.strip()
        if (sentence):
            return self.translateWithErrorHandling(sentence)
        else:
            return ""


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
            try:
                translation = self.translator.translateSentence(self.paragraph)
            except TranslationError:
                translation = "<span class=\"italic\">" + self.paragraph + "</span>"
            self.paragraph = ""
            self.output += translation


    def add(self, str):
        self.flush()
        self.output += str


    def decl(self, decl):
        self.add(output = "<!" + decl + ">")


    def formatAttr(self, name, value):
        if name == "title":
            try:
                value = self.translator.translateSentence(value)
            except TranslationError:
                pass
        return name + "=\"" + value + "\""


    def startTag(self, tag, attrs):
        output = "<" + tag
        for name, value in attrs:
            output += " " + self.formatAttr(name, value)
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

