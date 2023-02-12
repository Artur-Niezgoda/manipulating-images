from PIL import Image
import os

# Define paths for images and newly saved images
directory = "./images/"
output_directory = "./opt/icons/"

# Check if opt/icons exists and creates folders if not
if not os.path.exists(output_directory):
   os.makedirs(output_directory)

# Check if directory with images exists:
if not os.path.exists(directory):
    raise Exception("The folder images does not exist")

for image in os.listdir(directory):
    if image != ".DS_Store":
        im = Image.open(os.path.join(directory, image))
        im = im.rotate(-90).resize((128, 128)).convert("RGB")
        im.save(os.path.join(output_directory, image+'.jpeg'))
