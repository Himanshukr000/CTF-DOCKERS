#!/usr/bin/env python
import os
import sys
import inspect

MAX_NOTE_SIZE = 1024

arg_handlers = []


# Validate that the relative filesystem path `name` is within the sandbox
def validate(name):
	if not os.path.abspath(name).startswith(sandbox):
		raise IOError("Illegal note name: %s (%s)" % (name, os.path.abspath(name)))

def list_notes():
	print("Here are your notes:")
	notes = []
	for item in os.listdir("."):
		if os.path.isdir(item):
			notes.append("Folder: %s" % item)
		else:
			notes.append("Note: %s" % item)
	print("\n".join(notes))
arg_handlers.append(("list", "List the notes and folders in this folder", list_notes))

def display_note(name):
	validate(name)
	with open(name, "r") as fp:
		print(fp.read())
arg_handlers.append(("display", "Display the contents of the note", display_note))

def compose_note(name):
	validate(name)
	body = raw_input("Enter note body: ")
	if len(body) > MAX_NOTE_SIZE:
		raise ValueError("Cannot create a note larger than %d characters!" % MAX_NOTE_SIZE)
	with open(name, "w") as fp:
		fp.write(body)
arg_handlers.append(("compose", "Compose a new note", compose_note))

def create_shortcut(linkName, targetNote):
	validate(linkName)
	actual = os.path.join(os.path.dirname(linkName), targetNote)
	validate(actual)
	if not os.path.exists(actual):
		raise IOError("Note %s does not exist!" % actual)
	os.symlink(targetNote, linkName)
arg_handlers.append(("shortcut", "Create a shortcut to an existing note", create_shortcut))

def create_folder(name):
	validate(name)
	os.mkdir(name)
arg_handlers.append(("folder", "Create a new folder for notes", create_folder))

def open_folder(name):
	validate(name)
	os.chdir(name)
	list_notes()
arg_handlers.append(("open", "Open a folder of notes", open_folder))

def rename_note(name, newName):
	validate(name)
	validate(newName)
	os.rename(name, newName)
arg_handlers.append(("rename", "Rename an existing note", rename_note))

def delete_note(name):
	validate(name)
	os.remove(name)
arg_handlers.append(("delete", "Delete an existing note", delete_note))

def show_help():
	print("Commands available:")
	for handler in arg_handlers:
		argnames = inspect.getargspec(handler[2])[0]
		arginfo = handler[0] + "".join(" <%s>" % arg for arg in argnames)
		print("%-35s %s" % (arginfo, handler[1]))
arg_handlers.append(("help", "Display this help", show_help))

def quit():
	sys.exit(0)
arg_handlers.append(("quit", "Exit Notetorious", quit))


def handle_command(cmd, *args):
	for handler in arg_handlers:
		if cmd.lower() == handler[0]:
			argnames = inspect.getargspec(handler[2])[0]
			if len(args) != len(argnames):
				raise RuntimeError("Command %s expects %d arguments!" % (handler[0], len(argnames)))
			handler[2](*args)
			return
	raise NameError("Unknown command %s!" % cmd)


if __name__ == "__main__":
	assert len(sys.argv) == 2
	
	# Username is passed as first argument
	username = sys.argv[1]
	os.chdir(username)
	global sandbox
	sandbox = os.path.abspath(os.getcwd())
	
	# Greet logged-in user
	print("Welcome, %s!" % (username,))
	print("For a list of available commands, please type 'help'.")
	print("")
	
	# Show notes
	list_notes()
	
	# Input loop
	while True:
		# Read command line input
		line = raw_input("[>] ")
		if not line:
			print("")
			quit()
		
		# Split input line by whitespace into arguments
		args = line.strip().split()
		if not args:
			continue
		
		# Attempt to process the command
		try:
			handle_command(*args)
		except Exception, e:
			# Print all errors that bubble up to this level
			print("Error: %s" % e)
