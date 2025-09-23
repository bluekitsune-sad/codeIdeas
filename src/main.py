from PIL import Image

def image_to_characters(image_path, white_char='c', black_char='b', output_file='output.txt'):
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
    
    # Join all rows into one string
    ascii_art = '\n'.join(result)
    
    # Save the ASCII art into a text file
    with open(output_file, 'w') as f:
        f.write(ascii_art)
    
    print(f"ASCII art saved to {output_file}")

# Example usage:
image_path = 'C:/Users/HuTa0710/Desktop/dontknowbutcute.jpeg'  # Replace with the path to your image
output_file = 'output_image.txt'  # The file where the ASCII art will be saved
image_to_characters(image_path, output_file=output_file)
