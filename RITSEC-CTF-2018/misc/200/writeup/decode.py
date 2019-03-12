from PIL import Image

def decodeImage():
	# Open the image
    image = Image.open('CheckOutThisFilter.png')

	# This for loop will only print the Blue values of all
	# the pixels subtracting 13 to remove the ROT13 we applied
    for color in image.getdata():
        print(chr(color[2] - 13))


if __name__ == '__main__':
    decodeImage()
