#!/usr/bin/python3

from Book import Importer
from Book import Exporter

from Translator import Translator

import argparse


def main():
    parser = argparse.ArgumentParser(description='eels - to fill into your hovercraft',
                                     epilog='Translates an eBook by passing it piece by piece through DeepL (deepl.com)')
    parser.add_argument('-i', '--input', metavar='filename',
                        default ='test.epub',
                        help='ebook to translate')
    parser.add_argument('-il', '--inputLanguage', metavar='language',
                        default='EN',
                        help='input language')
    parser.add_argument('-o', '--output', metavar='filename',
                        default ='output.epub',
                        help='output file')
    parser.add_argument('-ol', '--outputLanguage', metavar='language',
                        default='DE',
                        help='output language')
    parser.add_argument('-t', '--throttle', metavar='seconds',
                        type=int, default=1,
                        help='seconds to wait after each translation request')
    args = parser.parse_args()

    src = Importer(args.input)
    dest = Exporter(args.output)
    translator = Translator(args.outputLanguage, args.inputLanguage, args.throttle)

    for info in src.items:
        with src.open(info) as content:
            if info.filename.endswith('.html'):
                utf8Content = content.read().decode('utf-8')
                translation = translator.translateHTML(utf8Content)
                dest.add(info, translation)
            else:
                dest.add(info, content.read())
        content.close()

    dest.write()


if __name__ == '__main__':
   main()
