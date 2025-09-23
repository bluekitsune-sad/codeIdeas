from PIL import Image

def image_to_characters(image_path, white_char='c', black_char='b'):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to grayscale
    grayscale_img = img.convert("L")
    
    # Get the pixel data
    pixels = grayscale_img.load()
    
    # Get the dimensions of the image
    width, height = grayscale_img.size
    
    # Loop through each pixel and convert it to a character
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = pixels[x, y]
            
            # If pixel is closer to white, set it to 'c', else 'b'
            if pixel_value > 128:  # Pixel value ranges from 0 (black) to 255 (white)
                row.append(white_char)  # White
            else:
                row.append(black_char)  # Black
        result.append(''.join(row))
    
    # Print the resulting character art
    return '\n'.join(result)

image_path = 'C:/Users/HuTa0710/Desktop/dontknowbutcute.jpeg'  # Replace with the path to your image
ascii_art = image_to_characters(image_path)
print(ascii_art)
