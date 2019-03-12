# [Stego 100] Nonlinear 2

## How It Works

Players are given a .txt file that appears to be a hexdump, but when decoded into binary can actually be seen to be in similar shape to a QR code. The binary can then be used to generate an image with the 0s as white pixels and the 1s as black pixels.

## Building

N/A

## Deployment

N/A

## Maintenance

N/A

## Intended Solution

Remove the `0x` padding with `sed -i 's/0x//g' nonlinear2.txt` then decode the hex into binary with Python. Then use the Python Imaging Library to generate a 27 x 33 image with 0s as white pixels and 1s as black pixels. Then scan the QR code with your phone, and the flag is presented in plaintext.
