# Eels
## to fill into your hovercraft

This is a small script written in Python that takes an eBook in the
ePub format and feeds it piece by piece through the DeepL translation
service. I have used it successfully to translate a full book from
English to German. The result is not perfect, but certainly usable.

## Usage

    ./eels.py --help
    

## Requirements
* Python3
* pydeepl: https://github.com/EmilioK97/pydeepl


## Disclaimer
This is very simple and I have only tested it with one particular book.
It may work for your book as well, but most likely it won't.

The DeepL API that is used by means of the pydeepl module is public,
but as far as I know it is undocumented and not officially supported.
