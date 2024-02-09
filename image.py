######################################
# Image Filter Project Starter Code  #
#                                    #
#             UTeach CSP             #
#                                    #
######################################


# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os, cv2

# Deletes old created images if they exist
images = ["Assets/combinedFilters.jpg","Assets/dotted.jpg","Assets/channel.jpg","Assets/filter3.jpg","Assets/gray.jpg"]
for i in images:
    if os.path.exists(i):
        os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('Assets/image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
    scale = mwidth
else:
    scale = mheight
if scale != 0:
    img = img.resize( (width // scale, height // scale) )

########################
#    Example Filter    #
########################
def gray():
    # Creates an ImageCore Object from original image
    pixels = img.getdata()
    # Creates empty array to hold new pixel values
    new_pixels = []
    # For every pixel from our original image, it saves
    # a copy of that pixel to our new_pixels array
    for p in pixels:
        new_pixels.append(p)
    # Starts at the first pixel in the image
    location = 0
    # Continues until it has looped through all pixels
    while location < len(new_pixels):
        # Gets the current color of the pixel at location
        p = new_pixels[location]
        # Splits color into red, green and blue components
        r = p[0]
        g = p[1]
        b = p[2]
        # Perform pixel manipulation and stores results
        # to a new red, green and blue components
        newr = (r + g + b) // 3
        newg = (r + g + b) // 3
        newb = (r + g + b) // 3
        # Assign new red, green and blue components to pixel
        # # at that specific location
        new_pixels[location] = (newr, newg, newb)
        # Changes the location to the next pixel in array
        location = location + 1
    # Creates a new image, the same size as the original 
    # using RGB value format
    newImage = Image.new("RGB", img.size)
    # Assigns the new pixel values to newImage
    newImage.putdata(new_pixels)
    # Sends the newImage back to the main portion of program
    return newImage


#####################
#    Your Filter    #
#####################

def dotted():
    # Creates an ImageCore Object from original image
    pixels = img.getdata()
    # Creates empty array to hold new pixel values
    new_pixels = []
    # For every pixel from our original image, it saves
    # a copy of that pixel to our new_pixels array
    for p in pixels:
        new_pixels.append(p)
    # Starts at the first pixel in the image
    location = 0
    # Continues until it has looped through all pixels
    for location, p in enumerate(new_pixels):
        # Splits color into red, green and blue components
        r = p[0]
        g = p[1]
        b = p[2]
        # Perform pixel manipulation and stores results
        # to a new red, green and blue components
        if location % 4 == 0 or location-2 % 4 == 0:
            newr, newg, newb = 0, 0, 0
        else:
            newr, newg, newb = r, g, b
        # Assign new red, green and blue components to pixel
        # # at that specific location
        new_pixels[location] = (newr, newg, newb)
        # Changes the location to the next pixel in array
        location = location + 1
    # Creates a new image, the same size as the original 
    # using RGB value format
    newImage = Image.new("RGB", img.size)
    # Assigns the new pixel values to newImage
    newImage.putdata(new_pixels)
    # Sends the newImage back to the main portion of program
    return newImage

#####################################
#    Your Filters with User Input   #
#####################################

def channel():
    print("Channel Options:")
    # Creates an ImageCore Object from original image
    pixels = img.getdata()
    # Creates empty array to hold new pixel values
    new_pixels = []
    # For every pixel from our original image, it saves
    # a copy of that pixel to our new_pixels array
    for p in pixels:
        new_pixels.append(p)
    # Starts at the first pixel in the image
    location = 0
    # Continues until it has looped through all pixels

    chnl = input("What channel? R, G, or B? ").lower()

    while all([chnl != "r" and chnl != "red", chnl != "g" and chnl != "green", chnl != "b" and chnl != "blue"]):
        print("Try again. Choose an option from the given choices.")
        chnl = input("What channel? R, G, or B? ").lower()
 
    while location < len(new_pixels):
        # Gets the current color of the pixel at location
        p = new_pixels[location]
        # Splits color into red, green and blue components
        match chnl:
            case "r" | "red":
                r, g, b = p[0], 0, 0
            case "g" | "green":
                r, g, b = 0, p[1], 0
            case "b" | "blue":
                r, g, b = 0, 0, p[2]
        # Perform pixel manipulation and stores results
        # to a new red, green and blue components
        newr, newg, newb = r, g, b
        # Assign new red, green and blue components to pixel
        # # at that specific location
        new_pixels[location] = (newr, newg, newb)
        # Changes the location to the next pixel in array
        location = location + 1
    # Creates a new image, the same size as the original 
    # using RGB value format
    newImage = Image.new("RGB", img.size)
    # Assigns the new pixel values to newImage
    newImage.putdata(new_pixels)
    # Sends the newImage back to the main portion of program
    return newImage

def filter3():
    print("filter3 Options:")
    newImage = img
    return newImage

# Creates the four filter images and saves them to our files
a = gray()
a.save("Assets/gray.jpg")
b = dotted()
b.save("Assets/dotted.jpg")
c = channel()
c.save("Assets/channel.jpg")
d = filter3()
d.save("Assets/filter3.jpg")

# Image filter names for use below
f1 = "dotted"
f2 = "channel"
f3 = "filter3"

# Apply multiple filters through prompts with the user
print("\nThe following prompt will ask you which filter to apply to the combined filter. It will keep asking until you answer 'none'.")
answer = input(f"\nWhich filter do you want me to apply?\n gray\n {f1}\n {f2}\n {f3}\n none\n\n")
while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input(f"\nIncorrect filter, please enter:\n gray\n {f1}\n {f2}\n {f3}\n none\n\n")

while answer == "gray" or answer == f1 or answer == f2 or answer == f3:
    if answer == "gray":
        img = gray()
    elif answer == f1:
        img = dotted()
    elif answer == f2:
        img = channel()
    elif answer == f3:
        img = filter3()
    else:
        break
    print("Filter \"" + answer + "\" applied...")
    answer = input(f"\nWhich filter do you want me to apply next?\n gray\n {f1}\n {f2}\n {f3}\n none\n\n")
    while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
        answer = input(f"\nIncorrect filter, please enter:\n gray\n {f1}\n {f2}\n {f3}\n none\n\n")

print("Combined filter being created...Done")

# Create the combined filter image and saves it to our files
img.save("Assets/combinedFilters.jpg")