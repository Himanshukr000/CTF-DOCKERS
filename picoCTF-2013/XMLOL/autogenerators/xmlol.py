__author__ = 'Collin Petty'
import os
from random import randint
from operator import add
import tempfile

template_file = "xmlol.xml"
templates = "autogenerators/templates/"


def validate_dependencies():
    print "DEPENDENCY CHECK - xmnlol.py (autogen)"
    if not os.path.exists(_template_path()):
        print "ERROR - xmlol - Could not find the template file (%s)" % template_file
        return False
    return True


def generate():
    template = open(_template_path(), 'r').read()
    key = reduce(add, [str(randint(999, 99999)) for _ in range(6)], '')
    template = template.replace('###KEY###', key)
    output = tempfile.NamedTemporaryFile(delete=False, suffix=".xml")
    output.write(template)
    output.close()
    return [os.path.abspath(output.name)], key, """<p>The book has instructions on how to dump the corrupted\
     configuration file from the robot's memory. You find a corrupted <a href='###file_1_url###'\
     target='_blank'>XML file</a> and are looking for a configuration key.</p>"""


def _template_path():
    return templates + template_file