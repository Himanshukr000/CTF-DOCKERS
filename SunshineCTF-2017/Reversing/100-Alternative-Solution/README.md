# [Reversing 10] Alternative Solution

## Setup

To run this challenge, copy this directory into the Pwnableharness directory. Then while in the base Pwnableharness directory run the command "make docker-start" and the challenge should run. The players will recieve a copy of the binary and 32 libpwn harness (they have to run the binary in the same directory as the libpwn harness). 

## Solution

Floating point values are compared to numbers with too many decimal points, so just type "nan".
