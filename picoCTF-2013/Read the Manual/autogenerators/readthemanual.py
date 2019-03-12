__author__ = 'Collin Petty'
import tempfile
import os
import random
import string

template_file = "readthemanual.txt"
templates = "autogenerators/templates/"


def validate_dependencies():
    print "DEPENDENCY CHECK - readthemanual.py (autogen)"
    if not os.path.exists(_template_path()):
        print "ERROR - Read the Manual - Could not find the template file (%s)" % template_file
        return False
    return True


def generate():
    template = open(_template_path(), 'r').read()
    key = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
    template = template.replace('###KEY###', key)
    shift = random.randint(1, 26)
    out_text = _caesar(template, shift)
    output = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    output.write(out_text)
    output.close()
    return [os.path.abspath(output.name)], key, """<p>On the back of the broken panel you see a recovery\
    <a href='###file_1_url###' target='_blank'>manual</a>. You need to find the emergency repair key in\
    order to put the robot into <code>autoboot</code> mode, but it appears to be ciphered using a Caesar cipher.</p>"""


def _template_path():
    return templates + template_file


def _caesar(text, shift):
    ret = list()
    for t in text:
        t = ord(t)
        if t in range(ord('a'), ord('z')+1):
            ret.append(((t - ord('a') + shift) % 26) + ord('a'))
        elif t in range(ord('A'), ord('Z')+1):
            ret.append(((t - ord('A') + shift) % 26) + ord('A'))
        elif t in range(ord('0'), ord('9')+1):
            ret.append(((t - ord('0') + shift) % 10) + ord('0'))
        else:
            ret.append(t)
    return string.joinfields(map(chr, ret), "")