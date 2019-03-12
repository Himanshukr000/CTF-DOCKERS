#!/usr/bin/python
import base64

def reverse(s):
    return s[::-1]


def b32decode(s):
    return base64.b32decode(s)


def reversePigLatin(s):
    return s[-1] + s[:-1]


def rot13(s):
    return s.decode('rot13')


def main():
    print 'Something Something Danger Zone'
    return '=YR2XYRGQJ6KWZENQZXGTQFGZ3XCXZUM33UOEIBJ'


if __name__ == '__main__':
    s = main()
    print s
    s = reverse(s)
    s = b32decode(s)
    s = rot13(s)
    s = reversePigLatin(s)
    print s
