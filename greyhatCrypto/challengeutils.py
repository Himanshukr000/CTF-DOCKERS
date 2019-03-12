import json
import os

def get_logfile(name):
	return open('var/log/%s' % name, 'a')

def get_metadata(name):
	return json.load(open('challenges/%s/metadata.json' % name))

def get_config(name):
	try:
		config_doc = json.load(open('config.json'))
		if name in config_doc:
			config = dict(config_doc[name])
			for k, v in config_doc['__default__'].iteritems():
				if k not in config:
					config[k] = v
			return config
		else:
			return config_doc['__default__']
	except (ValueError, KeyError):
		return {}

def install(name, config):
	metadata = get_metadata(name)

	if 'setup_command' in metadata:
		old_cwd = os.getcwd()
		os.chdir('challenges/%s/' % name)
		subprocess.check_call(metadata['setup_command'] % config, shell=True)
		os.chdir(old_cwd)

def is_challenge(name):
	return name in challenge_list()

def challenge_list():
	return os.listdir('challenges')
