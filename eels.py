#!/usr/bin/python3

from Book import Importer
from Book import Exporter

from Translator import Translator

import sys, getopt


def printHelp():
    print("eels - to fill into your hovercraft")
    print()
    print("Translates an eBook by passing it piece by piece through DeepL (deepl.com).")
    print()
    print("Options:")
    print("   -i <filename>       ebook to translate (default: test.epub)")
    print("   -il <language>      input language (default: EN)")
    print("   -o <filename>       output file (default: output.epub)")
    print("   -ol <language>      output language (default: DE)")
    print("   -t <seconds>        seconds to wait after each translation request (default: 1)")

def main(argv):
    inputFile = "test.epub"
    inputLanguage = "EN"
    outputFile = "output.epub"
    outputLanguage = "DE"
    throttle = 1

    try:
        opts, args = getopt.getopt(argv, "hi:il:o:ol:t:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            printHelp()
            sys.exit()
        elif opt == "-i":
            inputFile = arg
        elif opt == "-il":
            inputLanguage = arg;
        elif opt == "-o":
            outputFile = arg
        elif opt == "-ol":
            outputLanguage = arg
        elif opt == "-t":
            throttle = int(arg)

    src = Importer(inputFile)
    dest = Exporter(outputFile)
    translator = Translator(outputLanguage, inputLanguage, throttle)

    for info in src.items:
        with src.open(info) as content:
            if info.filename.endswith(".html"):
                utf8Content = content.read().decode("utf-8")
                translation = translator.translateHTML(utf8Content)
                dest.add(info, translation)
            else:
                dest.add(info, content.read())
        content.close()

    dest.write()


if __name__ == "__main__":
   main(sys.argv[1:])
