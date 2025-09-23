## Image to ASCII Art Converter

This project converts an image to an ASCII art representation using Python. The image is resized to 256x256 pixels, converted to grayscale, and then the pixel values are translated into ASCII characters (with black pixels as 'b' and white pixels as 'c'). The resulting ASCII art is saved in a text file.

## Files Overview

image_to_ascii.py: Contains the ImageToAscii class with methods to load, process, and convert the image to ASCII art.

main.py: The main script that imports and uses the ImageToAscii class to perform the image conversion.

output_image.txt: The output file where the ASCII art is saved (this file is generated after running the program).


## How to run

pip install pillow

py main.py



<!-- 
    git checkout -b <new-branch-name>
    git add .
    git commit -m "Your commit message"
    git push -u origin <new-branch-name>

-->
