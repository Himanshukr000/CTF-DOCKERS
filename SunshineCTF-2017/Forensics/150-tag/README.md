# [Forensics 150] Tag

The file is a pcap that has been compressed in a .gz file, which has been currupted. Inteded solution is to use either binwalk or wireshark to pull out the password protected flag.7z file. Then use strings or wireshark to find the base64 string. Then base64-decode -> hex-decode to find the qote. Google the quote and realize it is from the book "The Road". The password to the flag.zip is "the road".
