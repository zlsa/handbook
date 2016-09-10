#!/bin/env python3

import os
import datetime
import shutil

def compress():
  os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -o book-compressed.pdf book.pdf')

def build():
  os.system('xelatex book.tex')

def dotdate():
  now = datetime.datetime.now()
  return '.'.join([str(now.year), str(now.month).zfill(2), str(now.day).zfill(2)])

output_prefix = '../book/'
output_filenames = [
  output_prefix + 'OrbitalVehicleOperationsHandbook.' + dotdate() + '.pdf',
  output_prefix + 'OrbitalVehicleOperationsHandbook.pdf'
]

build()
build()
build()
compress()

for filename in output_filenames:
  shutil.copyfile('./book-compressed.pdf', filename)
