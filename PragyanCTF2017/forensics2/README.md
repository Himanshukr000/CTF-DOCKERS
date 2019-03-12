# Forensics Question 2

We were given the following image.

![transmission](transmission.png)

After using exiftool to get basic information about the image we saw the image was RGBA. So we came to the conclusion we should try to change the alpha values to be opaque rather than transparent.
So we wrote the small script included in this folder, [solve.py](solve.py)

The result contained the flag.

![output](output.png)
