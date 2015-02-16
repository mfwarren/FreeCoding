#!/usr/bin/env python3
# imports go here
import os
import sys
from subprocess import call
import shutil
from zipfile import ZipFile
from pathlib import Path


#
# Free Coding session for 2015-02-15
# Written by Matt Warren
#

pngcrush = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/pngcrush'

destination = os.path.join(os.getenv('HOME'), 'Desktop')

for ipa in sys.argv:
    if ipa.endswith('.ipa'):

        app_name, _ = os.path.splitext(ipa)
        expanded_dir = ipa.sub(os.path.basename(ipa), '')

        shutil.rmtree(expanded_dir)

        ipaZip = ZipFile(ipa)
        ipaZip.extractAll(expanded_dir)

        images_dir_path = os.path.join(destination, "%s Images" % app_name)

        shutil.rmtree(images_dir_path)
        os.makedirs(images_dir_path)

        p = Path('.')
        for png_file in list(p.glob(os.path.join(expanded_dir, 'Payload', '*.app', '*.png'))):
            call([pngcrush, '-q', '-revert-iphone-optimizations', '-d', images_dir_path, png_file])

        for jpg_file in list(p.glob(os.path.join(expanded_dir, 'Payload', '*.app', '*.jpg'))):
            shutil.move(jpg_file, images_dir_path)

        shutil.rmtree(expanded_dir)
