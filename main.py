
from BookImporter import BookImporter
from BookExporter import BookExporter

import sys, getopt


def printHelp():
    print('main.py -i <inputfile> -o <outputfile>')


def main(argv):
    inputFile = 'test.epub'
    outputFile = 'output.epub'
    try:
        opts, args = getopt.getopt(argv, "hi:o:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt == "-i":
            inputFile = arg
        elif opt == "-o":
            outputFile = arg

    src = BookImporter(inputFile)
    dest = BookExporter(outputFile)
    for item in src.items:
        dest.add(item)
    dest.write()

if __name__ == "__main__":
   main(sys.argv[1:])
