#! usr/bin/python

from OLA import sendDMXframe
from R4Tpatch import *

selected = []		 	# no fixture selected
rdmx = [0] * 512 		# generate empty list of 512
patch = []			# generate empty patch

########################################

########################################

stxt = '\033[1m'
etxt = '\033[0m'

########################################

cmd = 'intro'
while cmd != 'quit':
	if cmd == 'intro': print(stxt + '\n		Welcome to the grandRAT 0.1 interface\n		This software is a private alternative\n		ligthing controller designed by "Keyboard RAT"\n\n		May it one day make coffee and roll cigarets\n' + etxt)
	cmd = raw_input('grandRAT cmd > ')
	if cmd == 'help':
		print(stxt + '\n		Existing commands :\n\n			1 - help\n			2 - quit\n			3 - patch\n			4 - setup\n			5 - set dmx value\n			6 - dmx\n' + etxt)
	if cmd == 'patch':
		print(stxt)
		ManualPatch(patch)
		print(etxt)
	if cmd == 'setup': 
		print(stxt + '\n		grandRAT setup\n' + etxt)
		print(patch)
		print(' ')
	if cmd == 'set dmx value':
		print('work in progress')
	if cmd == 'dmx':
		print('work in progress')
