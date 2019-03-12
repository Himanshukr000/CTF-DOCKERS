# Authors:  Shadow5229  1cysw0rdk0
# File: encode.py
# 
# This file takes a string and will encode it into an RGB formatted image.
# It does this by taking the ORD value of each character and setting them
# as one of the RGB values (code replaces BLUE value) with the new value.
#
# Created for RITSEC CTF2018

from PIL import Image

def changeImage():
    # open the image you want to encode data to
    image = Image.open('the-mighty-stegosaurus.png')
    
    # This the string that will be encoded into the image
    flag1 = "(t<<3)*[8/9,1,9/8,6/5,4/3,3/2,0]"
    flag2 = "[[0xd2d2c7,0xce4087,0xca32c7,0x8e4008]"
    flag3 = "[t>>14&3.1]>>(0x3dbe4687>>((t>>10&15)>9?18:t>>10&15)*3&7.1)*3&7.1]"
    # a list to hold the tuples of pixels for the new image
    newImageData = []
    # count for looping around 
    count = 0
    # COLOR is a tuple of RGB value data for each pixel
    for color in image.getdata():
        red = (ord(flag1[count % len(flag1)]))
        green = (ord(flag2[count % len(flag2)]))
        blue = (ord(flag3[count % len(flag3)]))
        # a new RGB tuple with the ord value of the char from the flag string
        newPixel = (red, green, blue)
        # Appends the tuple to the list
        newImageData.append(newPixel)
        # used for wrapping back around the flag
        count += 1

    # creates a new IMAGE object with the same mode and size as the original
    newImage = Image.new('RGB', image.size)
    
    # Copies pixel data to the image
    newImage.putdata(newImageData)
    
    # Writes new image to disk
    newImage.save('test.png','PNG')

if __name__ == '__main__':
    changeImage()
