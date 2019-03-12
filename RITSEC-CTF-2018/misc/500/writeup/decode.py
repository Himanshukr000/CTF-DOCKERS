from PIL import Image

def decodeImage():
    
    flag1 = ""
    flag2 = ""
    flag3 = ""

    image = Image.open('test.png')
    for color in image.getdata():
        flag3 += chr(color[2])
        flag2 += chr(color[0])
        flag1 += chr(color[1])


    print(flag1)
    print(flag2)
    print(flag3)

if __name__ == '__main__':
    decodeImage()
