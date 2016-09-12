#!/bin/env python3

import shutil
import build

build.build()
build.glossaries()
build.build()
build.build()
build.compress()

output_prefix = '../book/'
output_filenames = [
  output_prefix + 'OrbitalVehicleOperationsHandbook.' + build.dotdate() + '.pdf',
  output_prefix + 'OrbitalVehicleOperationsHandbook.pdf'
]

for filename in output_filenames:
  shutil.copyfile('./tex-files/book-compressed.pdf', filename)
