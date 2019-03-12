import sys

from challengeutils import install, get_config

if __name__ == '__main__':
	name = sys.argv[1]
	install(name, get_config(name))
