from image_to_ascii import ImageToAscii  

def main():
    image_path = 'path/To/Your/Image'  
    output_file = 'output_image.txt'  
    
    image_to_ascii = ImageToAscii(image_path, output_file=output_file)
    
    image_to_ascii.convert()

if __name__ == "__main__":
    main()
