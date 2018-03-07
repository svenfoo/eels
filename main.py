
from BookImporter import BookImporter
from BookExporter import BookExporter
from Translator import Translator

import sys, getopt


def printHelp():
    print('main.py -i <inputfile> -o <outputfile>')


def main(argv):
    inputFile = "test.epub"
    inputLanguage = "EN"

    outputFile = "output.epub"
    outputLanguage = "DE"

    try:
        opts, args = getopt.getopt(argv, "hi:o:")
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

    src = BookImporter(inputFile)
    dest = BookExporter(outputFile)
    translator = Translator(dest, outputLanguage, inputLanguage)

    for info in src.items:
        with src.open(info) as content:
            if info.filename.endswith(".html"):
                translator.translate(info, content)
            else:
                dest.add(info, content)
        content.close()

    dest.write()

if __name__ == "__main__":
   main(sys.argv[1:])
