#!/bin/env python3

import build

build.build()
build.build()
build.build()
build.compress()

output_prefix = '../book/'
output_filenames = [
  output_prefix + 'OrbitalVehicleOperationsHandbook.' + dotdate() + '.pdf',
  output_prefix + 'OrbitalVehicleOperationsHandbook.pdf'
]

for filename in output_filenames:
  shutil.copyfile('./book-compressed.pdf', filename)
