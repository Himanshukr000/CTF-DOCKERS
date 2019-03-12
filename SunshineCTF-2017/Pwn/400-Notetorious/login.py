#!/usr/bin/env python
import os
import fcntl
import grp
import subprocess

# Unprivileged system user account
NOTETORIOUS_USER = "notetorious"


def login(username, password):
	if not username.isalnum():
		raise ValueError("Username must be alphanumeric!")
	
	if not password:
		raise ValueError("Password cannot be empty!")
	
	# Try opening and locking password file as notetorious_auth:notetorious_auth 0600
	pass_fname = username + ".password"
	fd = os.open(pass_fname, os.O_RDWR | os.O_CREAT, 0600)
	fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
	
	try:
		# Read existing password
		existing_pass = os.read(fd, 64)
		if not existing_pass:
			# Create new user directory as notetorious_auth:notetorious 0775
			os.mkdir(username)
			os.chown(username, -1, grp.getgrnam(NOTETORIOUS_USER).gr_gid)
			os.chmod(username, 0775)
			
			# Write new password
			os.lseek(fd, 0, os.SEEK_SET)
			os.write(fd, password)
		else:
			# Validate password
			if password != existing_pass:
				raise ValueError("Wrong password!")
	finally:
		# Unlock and close password file
		fcntl.flock(fd, fcntl.LOCK_UN)
		os.close(fd)


def notetorious(username):
	# Use sudo to run main notetorious program as an unprivileged user
	subprocess.call(["/usr/bin/sudo", "-Hu", NOTETORIOUS_USER, "/notetorious/notetorious.py", username])


if __name__ == "__main__":
	# Enter data directory
	os.chdir("data")
	
	# Display banner and login prompt
	print("Welcome to Notetorious!")
	print("")
	print("Please enter login information. If user does not exist, it will be created for you.")
	username = raw_input("Username: ")[:64]
	password = raw_input("Password: ")[:64]
	
	# Log the user in
	login(username, password)
	
	# Start notetorious as unprivileged user
	notetorious(username)
	
	# Log out
	print("Goodbye!")
