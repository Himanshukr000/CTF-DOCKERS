# Misc 200: Check out this cool filter
**Author**: 1cysw0rdk0 & oneNutW0nder

**Flag**: RITSEC{TIL_JPEG_COMPRESSION_MESSES_WITH_RGB_VALUES}

## Description
https://www.youtube.com/watch?v=zA52uNzx7Y4

## Deployment
The following files must be provided to the user:
- [`CheckOutThisFilter.png`](./CheckOutThisFilter.png)

## Writeup
The writeup directory contains the following files:
- [`decode.py`](./writeup/decode.py): A script to get the blue RGB values of
  the pixels in the picture
- [`encode.py`](./writeup/encode.py): A script to encode a string into an image
  by replacing one of the RGB values with the ASCII values of the characters
- [`writeup.docx`](./writeup/writeup.docx): A description of how the challenge
  would be solved