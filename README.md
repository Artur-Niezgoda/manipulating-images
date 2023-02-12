# manipulating-images
A script that edits images (rotates, resizes and converts) and saves them in the new format in the new directory.

## Requirements

Requires the Python Imaging Library (PIL). The original PIL library hasn't been updated since 2009 and does not support Python 3. Therefore the scripts uses a current fork of PIL called Pillow, that properly supports Python 3 and is kept up-to-date. The Pillow library is packaged with the name pillow, but the module name in Python is still PIL.

The images have to be stored in the folder 'images'. If the directory does not exist it raises an exception. The edited images are stored in the folder opt/icons, if the directory does not exist it is created by the script. 
