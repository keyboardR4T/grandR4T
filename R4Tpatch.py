#! /usr/bin/python

########################################
##### 1 - PATCHING #####################
########################################

def Patch(patch, fixID, chanID, uni, dmxAdr, fixture, name, quantity): #NEED TO ADD UID

	uid = len(patch) + 1 # Get the last available UID
	i = 0
	if fixID != 0: # Patch an automatic fixture
		
		while i < quantity:
			f = open("Fixtures/" + fixture + ".fixt")
			out = f.read().splitlines()
			for line in out:
				patch.append([uid, fixID, 0, uni, dmxAdr, fixture, name, line])
				uid += 1
				dmxAdr += 1
			fixID += 1
			i += 1
	elif chanID != 0: # Patch a trad, shutter, smoke machine[...]
		while i < quantity:
			patch.append([uid, 0, chanID, uni, dmxAdr, fixture, name, ''])
			uid += 1
			dmxAdr += 1
			chanID += 1
			i += 1
	else:
		print('no channel ID or fixture ID were chosen')
	

def ManualPatch(patch):
	fixture = raw_input('	Patch time BITCHES !\n	Enter a fixture model : ')
	name = raw_input('	Would you like to name it ? ')
	fixID = raw_input('	Enter fixture ID : ')
	if fixID == ''  or fixID == 0:
		chanID = raw_input('	Enter channel ID : ')
		fixID = 0
	else : chanID = 0
	uni = input('	Enter universe : ')
	dmxAdr = input('	Enter DMX adress : ')
	quantity = input('	How many ? ')
	print('\n	Patching fixture...')
	Patch(patch, int(fixID), int(chanID), uni, dmxAdr, fixture, name, quantity)
	print('\n	Done !')


########################################
##### 2 - MODIFY PATCH #################
########################################

def DelPatchLine(patch, uid):
	i = 1
	while i <= len(patch):
		if i == uid:
			patch[i] = [uid, 0, 0, 0, 0, '', '', '']
#def AddPatchLine(patch, fixID, chanID, uni, dmxAdr, fixture, name, param):

def ModPatchFixID(patch, uid, fixID):
	i = 1
	while i <= len(patch):
		if i == uid:
			patch[i][1] = fixID
			i = len(patch) # maybe fin a quicker way to end the thing ?
		i += 1

#def ModPatchChanID(patch, uid, chanID):
#	patch[i][2] = chanID
#def ModPatchUni(patch, uid, uni):
#	patch[i][3] = uni
#def ModPatchDmx(patch, uid, dmxAdr):
#	patch[i][4] = dmxAdr
#def ModPatchFix(patch, uid, fixture):
#	patch[i][5] = fixture
#def ModPatchNam(patch, uid, name):
#	patch[i][6] = name
#def ModPatchPar(patch, uid, param):
#	patch[i][7] = param
	
########################################
########################################
########################################

