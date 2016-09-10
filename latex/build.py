#!/bin/env python3

import os
import datetime

def compress():
  os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -o tex-files/book-compressed.pdf tex-files/book.pdf')

def build():
  os.system('xelatex -output-directory tex-files/ book.tex')
  #os.chdir('tex-files')
  #os.system('makeglossaries book.glo')
  #os.chdir('..')

def dotdate():
  now = datetime.datetime.now()
  return '.'.join([str(now.year), str(now.month).zfill(2), str(now.day).zfill(2)])

if __name__ == '__main__':
  build()
