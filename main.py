
from BookImporter import BookImporter
from BookExporter import BookExporter
from Translator import Translator

import sys, getopt


def printHelp():
    print("main.py")
    print("   -i <inputfile>       ebook to translate (default: test.epub)")
    print("   -o <outputfile>      output file (default: output.epub")
    print("   -t <seconds>         seconds to wait after each translation request (default: 1)")

def main(argv):
    inputFile = "test.epub"
    inputLanguage = "EN"

    outputFile = "output.epub"
    outputLanguage = "DE"

    throttle = 1

    try:
        opts, args = getopt.getopt(argv, "hi:o:t:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            printHelp()
            sys.exit()
        elif opt == "-i":
            inputFile = arg
        elif opt == "-o":
            outputFile = arg
        elif opt == "-t":
            throttle = int(arg)

    src = BookImporter(inputFile)
    dest = BookExporter(outputFile)
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
