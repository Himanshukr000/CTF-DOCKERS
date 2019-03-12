__author__ = 'Collin Petty'
import os
import random
import hashlib

dict_file = "/usr/share/dict/words"


def validate_dependencies():
    print "DEPENDENCY CHECK - trythemall.py (autogen)"
    if not os.path.exists(dict_file):
        #utilities.send_email_to_list(common.admin_emails, "Autogenerator Validation Error",
        #                             """Could not validate that the word list file for 'trythemall.py' exists.""")
        print ("ERROR - trythemall - Could not validate that the word list file exists.")
        return False
    if _get_random_word() == "":
        #tilities.send_email_to_list(common.admin_emails, "Autogenerator Validation Error",
        #                             """Test load of a random word failed to return a non-empty string.""")
        print ("ERROR - trythemall - Test load of a random word failed to return a non-empty string.")
        return False
    return True


def generate():
    # we don't need the parameters for this problem
    word = _get_random_word()
    salt = str(random.randint(1000, 9999))
    key_hash = hashlib.md5(word + salt).hexdigest()
    desc = """You have found a passwd file containing salted passwords.
    An unprotected configuration file has revealed a salt of %s.
    The hashed password for the 'admin' user appears to be %s, try to brute force this password.""" % (salt, key_hash)
    return None, word, desc


def _get_random_word():
    word_list = open(dict_file, 'r')
    file_size = os.stat(dict_file)[6]
    word_list.seek((word_list.tell() + random.randint(0, file_size-1)) % file_size)
    word_list.readline()  # flushes line since we are probably in the middle
    return word_list.readline().strip()