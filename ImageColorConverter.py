from PIL import Image #Imports Image Module From Pillow
import preferences as pref

def PixelConverter(image_path, replace_color, new_color):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Define the color to be replaced
    replace_color = replace_color

    # Create a new image with the same size and the specified background color
    new_image = Image.new("RGB", (width, height), new_color)

    # Iterate through each pixel of the original image
    for x in range(width):
        for y in range(height):
            # Get the color of the current pixel
            pixel_color = image.getpixel((x, y))

            # If the pixel color is not white, replace it with the new color
            if pixel_color != replace_color:
                new_image.putpixel((x, y), pixel_color)

    # Save the modified image back to the original file path
    new_image.save(image_path)




#This Function Is Used To Replace Colors Within An Image
def replace_color(image_path, target_color, new_color):
    # Open the image using Pillow
    image = Image.open(image_path)

    #Debug
    if pref.debug == True:
            print("Target  Color : ", target_color)
            print("Replace Color : ", new_color)

    # Convert the image to RGBA mode if it's not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # Get the pixel data as a list of tuples
    pixel_data = list(image.getdata())

    # Create a new list to store the modified pixel data
    new_pixel_data = []

    # Define a tolerance for color matching (adjust as needed)
    tolerance = 10

    # Iterate through each pixel and check if it matches the target color
    for pixel in pixel_data:
        r, g, b, a = pixel

        # Check if the pixel color is within the tolerance of the target color
        if (
            abs(r - target_color[0]) <= tolerance and
            abs(g - target_color[1]) <= tolerance and
            abs(b - target_color[2]) <= tolerance
        ):
            # Replace the target color with the new color
            new_pixel_data.append(new_color + (a,))
        else:
            # Keep the original pixel color
            new_pixel_data.append(pixel)

    # Create a new image with the modified pixel data
    image.putdata(new_pixel_data)

    # Save the modified image back to the original file path
    image.save(image_path)

    #Debug
    if pref.debug == True:
         print("Image Converted Successfully")


