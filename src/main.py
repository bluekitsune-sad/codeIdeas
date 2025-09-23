from image_to_ascii import ImageToAscii  

def main():
    image_path = 'C:/Users/HuTa0710/Desktop/dontknowbutcute.jpeg'  
    output_file = 'output_image.txt'  
    
    image_to_ascii = ImageToAscii(image_path, output_file=output_file)
    
    image_to_ascii.convert()

if __name__ == "__main__":
    main()
