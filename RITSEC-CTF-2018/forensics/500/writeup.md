# Lite Forensics Writeup
The secret to this challenge is the _content_ of the data means nothing, Only the _length_ matters. The focus is on the internal workings of how SQLite stores data.

## Step 1. Filtering Out Unneeded Data.
Each row can be broken down into pairs of columns (e.g. `01_a` and `01_b`), the only records that matter are the records that contain `1` in the `0X_a` columns.

> Removing extra data is optional and the flag can still be found without doing this, however, filtering out all the noise will make the process a lot faster.

We can quickly find all important data by grepping for the `1`'s.
```
grep -Eo '1, [^,^)]+' file_format.sql  # Only show the valid data
grep '1, ' file_format.sql             # Only show the valid rows
```

The simplest way to process the data is to remove all non-valid rows from the SQL script. This shrinks the amount of data we need to search through. 

## Step 2. Building the Database
The flag itself does not actually exist in the data until it is sent through the SQLite engine and written to an actual database. We can load the script into a database by writing a simple python script.

```python
import sqlite3

with open("file_format.sql") as fil:
    script = fil.read()
conn = sqlite3.connect("file_format.sqlite")
curr = conn.cursor()
curr.executescript(script)
conn.commit()
```

## Step 3. Analyzing the Binary
SQLite stores each `record` (a database row) in a special format. The record consists of two parts, the `header` and the `body`. Different types of data in the record are represented as different varints in the header. The format which is used is well documented on the [SQLite website](https://www.sqlite.org/fileformat.html#record_format).

Each column of data has a corresponding value in the `header` of the record. If the random string is important information (the column is preceeded by a `1`) then the value in the header is a letter to the flag.

The best way to analyze the data is to open a hex editor and start finding the records in the binary. The first record we need to find  contains the string `zDH{Hg4JP9CY`. The entire hex value of the record is below.

```
|        Header         |
 08 00 08 51 09 52 08 31 7A 44 48 7B 48 67 34 4A 50 39 43 59 74 67 
 49 47 5A 36 55 74 78 35 59 68 73 21 74 42 4B 45 49 32 4A 48 89 85 
 A9 F5 D9 99 A3 28 45 F0 80 AB 3A 05 B5 50 83 86 A6 2C FD 05 25 1C 
 5A 07 E4 E5 43 FF D6 87 63 C2 6B 75 4E 75 32 7A 7B 69 43 37 51 53 
 62 39 68 65 61 68 5A                                              
```

We can disect this record to get the idividual pieces
```
# Header
08 00 08 51 09 52 08 31 
# 00_b
7A 44 48 7B 48 67 34 4A 50 39 43 59 74 67 49 47 5A 36 55 74 78 35 59 68 73 21 74 42 4B 45 49 32 4A 48
# 01_b
89 85 A9 F5 D9 99 A3 28 45 F0 80 AB 3A 05 B5 50 83 86 A6 2C FD 05 25 1C 5A 07 E4 E5 43 FF D6 87 63 C2 6B
# 02_b
75 4E 75 32 7A 7B 69 43 37 51 53 62 39 68 65 61 68 5A                                              
```

We now have the header that we are looking for. We can pull apart the header to get the letter for our flag.

The first byte `0x08` is the length of the header.

The second byte `0x00` is NULL. Each record was given a NULL value in the `base` column to help while digging through the binary.

The third byte `0x08` indicates that a `0` is stored in `00_a`.

The fourth byte `0x51` is the length of `00_b`

The fifth byte `0x09` indicates that `1` is stored in `01_a`. Since this is a 1. The next record is important for us.

The fifth byte `0x52` is the length of `01_b`. `0x52` also happens to be `R`. The first letter of out flag.

We dont need to worry about the last two bytes of the header. We have the first letter of our flag. We may now continue to parse through each record until we find the flag.

## Shortcuts
Because each record has 7 columns, the header of the record will always be 8 bytes long (`0x08` + the header). Because the first column is alway NULL, the second byte of the header will always be `0x00`. The third byte will always contain a `1` (`0x09`) or a `0` (`0x08`). We may now search the binary for those values to get all the headers in the database.

A simple python script can do this for us
```
import re

with open('test.sqlite', 'rb') as fil:
    data = fil.read()

regex = rb'\x08\x00[\x08|\x09].....'
headers = re.findall(regex, data)
```

Once we have all the headers. We can go through and find the `0x09` and the byte that comes after it.
```
flag = b""
for header in headers:
    flag += re.search(rb'\t(.)', header).group(1)
print(flag[::-1])
```

All of these characters concatonated are the flag.

NOTE: The flag is in reverse order as SQLite starts writing records at the bottom and works up.