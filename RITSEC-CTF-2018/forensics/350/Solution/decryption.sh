#!/bin/bash
#
# Purpose: Decrypt Hard1 challenge for networking week
#
# Author: Scott Brink
#

# Makes the capture just the correct DNS packets
tshark -r hard.pcap -x -Y 'ip.addr == 192.168.1.1' | cut -d" " -f13 > filtered.txt

# Grabs the 1s and the 0s and places them in a file
while read i
     do
         if [ "$i" == "01" ]; then
             echo 1 >> answer.txt
         elif [ "$i" == "00" ]; then
             echo 0 >> answer.txt
        fi
done < filtered.txt

# Removes newlines
i=$(cat answer.txt | tr -d "\n") 

# Converts bit string to ascii representation
python3 binascii.py $i 

# Remove the junk I make lol (I should probably use variables)
rm filtered.txt
rm answer.txt
