
from BookImporter import BookImporter

import sys, getopt


def printHelp():
    print('main.py -i <inputfile> -o <outputfile>')


def main(argv):
    inputFile = 'test.epub'
    outputFile = ''
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
    for item in src.items:
        print(item)



if __name__ == "__main__":
   main(sys.argv[1:])
