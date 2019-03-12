# [Stego 150] Hello Friend

## How It Works

Players are given the image `HelloFriend.png` and are told that it contains information about Stage 2. The image has hidden data encoded in the color values of the pixels. Specifically, the least significant bit of the red, green, and blue channels are set to each show a different B&W QR code. Each QR code can be decoded into short text strings:

| Color | String
|-------|--------
| Red   | `"Sorry, it's not quite that easy..."`
| Green | `"Maybe try combining these hints..."`
| Blue  | `"m{ekyzewRd =sR,=Gu> N1!nv\x0b.~>4dd}"`

## Building

* Install required Python modules
  * `sudo -H pip install pillow pyqrcode numpy`
* Generate output PNG file from input JPG and flag.txt
  * `python HelloFriend.py`
* This should create `attachments/HelloFriend.png`

## Deployment

N/A

## Maintenance

N/A

## Intended Solution

Build a string by XOR-ing all 3 strings from the QR codes together. This is the flag.
