# Crypto 150: CictroHash
**Author**: Cictrone  

**Flag**: RITSEC{I_am_th3_gr3@t3st_h@XOR_3v@}

## Description
See the attached PDF for an amazing new Cryptographic Hash Function called
CictroHash. For this challenge you must implement the described Hash Function
and then find a collision of two strings. Once a collision is found send both 
strings to {{INSERT_SERVER}} as a HTTP POST request like below:


```
curl -X POST http://{{INSERT_SERVER}}/checkCollision \
--header "Content-Type: application/json" \
--data '{"str1": "{{INSERT_STR1}}", "str2": "{{INSERT_STR2}}"}'
```

If the strings are a valid collision then the flag will be returned.

NOTE: requests to this server are being rate-limited for obvious reasons.

## Deployment
The following files must be provided to the user:
- [`CictroHash.pdf`](./CictroHash.pdf)

A docker container must be deployed for this challenge. It is a Flask webserver
that runs on port 80. The following files are required to build this container:
- [`Dockerfile`](./Dockerfile)
- [`server.py`](./server.py)
- [`hash.py`](./hash.py)
- [`requirements.txt`](./requirements.txt)

## Writeup
The writeup directory contains the following files:
- [`CictroHash.docx`](./writeup/CictroHash.docx): The `.docx` file used to
  create `CictroHash.pdf`
- [`hash.py`](./writeup/hash.py): An example script that will find a collision
  in CictroHash