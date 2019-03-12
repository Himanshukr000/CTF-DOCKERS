__author__ = 'Collin Petty'

import os
import random
import string
import tempfile
import zipfile
from subprocess import call

javac_path = "/usr/bin/javac"
template_file = "bytecode.Authenticator.java"
templates = "autogenerators/templates/"


def validate_dependencies():
    print "DEPENDENCY CHECK - bytecode.py (autogen)"
    if not os.path.exists(javac_path):
        print "ERROR - bytecode - The specified java compiler (%s) does not appear to exist." % javac_path
        return False
    if not os.access(javac_path, os.X_OK):
        print "ERROR - bytecode - javac is not executable by the python runtime."
        return False
    if not os.path.exists(_template_path()):
        print "ERROR - bytecode - Could not locate the java template file (%s) ." % _template_path()
        return False
    return True


def generate():
    template = open(_template_path(), 'r').read()
    key_list = [ord(random.choice(string.letters)) for _ in range(10)]
    key = ''.join([chr(k) for k in key_list])
    magic_string = "ThisIsth3mag1calString%s" % str(random.randint(999, 9999))
    for idx, k in enumerate(key_list):
        template = template.replace("###char%s###" % str(idx), str(k))
    template = template.replace("###string###", magic_string)

    output_folder = tempfile.mkdtemp()
    print "## random output_folder: %s" % output_folder
    java_file = open("%s/Authenticator.java" % output_folder, 'w')
    java_file.write(template)
    java_file.close()
    call([javac_path, '-d', output_folder, "%s/Authenticator.java" % output_folder])
    class_path = "%s/Authenticator.class" % output_folder
    out_zip = tempfile.NamedTemporaryFile(delete=True, suffix=".zip")
    out_zip.close()
    zf = zipfile.ZipFile(os.path.abspath(out_zip.name), mode='w')
    zf.write(os.path.abspath(class_path), os.path.basename(class_path))
    zf.close()
    print "Returning Key: %s" % key
    return [os.path.abspath(out_zip.name)], key, """<p>You need to authenticate with the guard to gain\
     access to the loading bay! Enter the root password from the vault application to retrieve the passkey!\
     <a href='###file_1_url###' target='_blank'>This</a> class file is the executable for the vault application.</p>"""


def _template_path():
    return templates + template_file