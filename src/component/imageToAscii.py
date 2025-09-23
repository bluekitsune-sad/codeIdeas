from PIL import Image

class ImageToAscii:
    def __init__(self, image_path, white_char='c', black_char='b', new_size=(64, 64), output_file='output.txt'):
        self.image_path = image_path
        self.white_char = white_char
        self.black_char = black_char
        self.new_size = new_size
        self.output_file = output_file
        self.image = None
        self.grayscale_img = None
        self.pixels = None
    
    def load_image(self):
        """Open the image and resize it."""
        self.image = Image.open(self.image_path)
        self.image = self.image.resize(self.new_size)
    
    def convert_to_grayscale(self):
        """Convert the image to grayscale."""
        self.grayscale_img = self.image.convert("L")
        self.pixels = self.grayscale_img.load()
    
    def generate_ascii(self):
        """Generate ASCII art from the grayscale image."""
        width, height = self.grayscale_img.size
        result = []
        
        for y in range(height):
            row = []
            for x in range(width):
                pixel_value = self.pixels[x, y]
                
                # If pixel is closer to white, set it to white_char, else black_char
                if pixel_value > 128:
                    row.append(self.white_char)
                else:
                    row.append(self.black_char)
            result.append(''.join(row))
        
        return '\n'.join(result)
    
    def save_to_file(self, ascii_art):
        """Save the generated ASCII art to a text file."""
        with open(self.output_file, 'w') as f:
            f.write(ascii_art)
        print(f"ASCII art saved to {self.output_file}")
    
    def convert(self):
        """Complete process: load, convert, generate ASCII, and save to file."""
        self.load_image()
        self.convert_to_grayscale()
        ascii_art = self.generate_ascii()
        self.save_to_file(ascii_art)
