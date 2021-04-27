# -*- coding: utf-8 -*-
import webbrowser
import sys
import os
import time

# The new functions of the community can be written here, it will make the code easier to read, and the bugs faster to correct.
# WARNING: don't import 'script.py' or 'tomodules.py' in this file !

def example():				# You can access this function in the 'script.py' and 'tomodules.py' files by writting community_scripts.example().
	print("Hello world !")
						    # You can test this function by writting 'testbox' in the main menu.

def browser():
	print("Opening your default web browser...")
	webbrowser.open_new("https://www.google.com")

# recommended modules :
	# pygame
	# sys
	# hashlib
	# termcolor
	# argparse
