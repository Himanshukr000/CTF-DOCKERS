# [Stego 50] Nonlinear 1

## How It Works

Players are given a .wav file that appears to be morse code, but each morse character is eight ticks long, instead of varying between 2 and 5. This is a hint that the dits and dahs actually represent binary characters, which when decoded result in a base 64 string, which then decodes into the flag.

## Building

N/A

## Deployment

N/A

## Maintenance

N/A

## Intended Solution

Transcribe the morse code into binary, with dits as 0s and dahs as 1s, then decode the base 64 string.
