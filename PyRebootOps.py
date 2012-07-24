#!/usr/bin/env python

_app_name = "PyRebootOps"
#############################################################################
# PyRebootOps.py - Schedule file opeartions to be executed with system reboot
#
# PyRebootOps Version 0.1
# Copyright 2012
# Chetan Giridhar cjgiridhar@gmail.com
# Created: 07/24/2012 Last Modified: 07/24/2012
#
# This file is part of PyRebootOps.
#
# PyRebootOps is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation;
#
# PyRebootOps is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
#############################################################################


import sys, os, _winreg, win32api

def help():
	""" Help for the PyRebootOps utility """
	
	print """
	***********************************************************
	PyRebootOps1.0: Schedule file opeartions to be executed
	during the next system reboot. - Chetan Giridhar
	***********************************************************
	
	syntax: PyRebootOps.exe [<switch>...] <source> <destination>
		
	-move: Moves a file from source to destination. 
	<source> and <destination> are required.
	
	-delete: Deletes the file from the harddisk after reboot. 
	<destination> not required.
	
	-rename: Renames a file.
	<source> and <destination> are required.
	
	-scheduled: Prints all the scheduled operations for the next reboot.
	
	-reset: Resets all the operations that were previously scheduled.
	
	-reboot: Restarts the system after a timeout of 1 sec.
	"""
	sys.exit(0)
	
def move(source, destination):
	""" Method for scheduling move operation """

	sourceDir = os.path.dirname(source)
	destinationDir = os.path.dirname(destination)
	if sourceDir == destinationDir:
		print "Alert: Move operation is done across directories or volumes.\nUse Rename operation instead."
		sys.exit(0)
	if not os.path.exists(source): 
		print "Alert: " +source + " doesn't exist but move operation is scheduled."		
	
	_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
	key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", 0,_winreg.KEY_ALL_ACCESS)
	key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
	try:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
	except:
		sample = ([],7)
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, sample[0])
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = "\\??\\" + destination 
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)
	else:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = "\\??\\" + destination 
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)
		

def rename(source, destination):  
	""" Method for scheduling rename operation """
	
	sourceDir = os.path.dirname(source)
	destinationDir = os.path.dirname(destination)
	
	if sourceDir != destinationDir:
		print "Alert: Rename operation should be done in the same directory.\nUse Move operation instead."
		sys.exit(0)
		
	if not os.path.exists(source): 
		print "Alert: " +source + " doesn't exist but rename operation is scheduled."
		
	_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
	key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", 0,_winreg.KEY_ALL_ACCESS)
	key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")

	try:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
	except:
		sample = ([],7)
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, sample[0])
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = "\\??\\" + destination 
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)
	else:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = "\\??\\" + destination 
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)

def delete(source):
	""" Method for scheduling a delete operation """
	
	if not os.path.exists(source): 
		print "Alert: " +source + " doesn't exist but delete operation is scheduled."
		
	_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
	key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", 0,_winreg.KEY_ALL_ACCESS)
	key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
	try:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
	except:
		sample = ([],7)
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, sample[0])
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = ""
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)
	else:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		list = operations[0]
		source = "\\??\\" + source 
		destination = "" 
		list.append(unicode (source))
		list.append(unicode (destination))
		tup = (list, 7)
		key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager")
		_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, tup[0])
		_winreg.CloseKey(key)

def scheduledOperations():  
	""" Method for getting the scheduled operations """
	
	_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
	key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", 0,_winreg.KEY_ALL_ACCESS)
	try:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		if operations[0] == []:
			print "No operations scheduled..."
	except:
		print "No operations scheduled..."
		_winreg.CloseKey(key)
	else:
		operations = _winreg.QueryValueEx(key, "PendingFileRenameOperations")
		count = 0
		while( count < len(operations[0])):
			try:
				operations[0][count+1]
			except:
				print "Delete operation scheduled for %s" %(operations[0][count].split('\??\\')[1])
				count+=2
			else:
				if not os.path.dirname(operations[0][count].split('\??\\')[1]) == os.path.dirname(operations[0][count+1].split('\??\\')[1]):
					print "Move operation scheduled from %s to %s" %(operations[0][count].split('\??\\')[1], operations[0][count+1].split('\??\\')[1])
				if os.path.dirname(operations[0][count].split('\??\\')[1]) == os.path.dirname(operations[0][count+1].split('\??\\')[1]):
					print "Rename operation scheduled from %s to %s" %(operations[0][count].split('\??\\')[1], operations[0][count+1].split('\??\\')[1])
				count+=2
		_winreg.CloseKey(key)
		
def reset():
	""" Method for resetting the scheduled operations """
	
	_winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
	key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", 0,_winreg.KEY_ALL_ACCESS)
	sample = ([],7)
	_winreg.SetValueEx(key, "PendingFileRenameOperations", 0, _winreg.REG_MULTI_SZ, sample[0])
	print "All scheduled operations removed"
	_winreg.CloseKey(key)
	
def reboot():
	""" Method for rebooting the system """
	
	choice = raw_input("Do you want to restart your system [y|Y]:")
	if choice == 'y' or choice == 'Y':
		os.system("shutdown -r -t 1")
	else:
		print "You chose not to reboot your system"

if len(sys.argv) == 1:
	help()
if sys.argv[1] not in ["-move", "-delete", "-rename", "-reset", "-reboot", "-scheduled"]:  
	help()
if sys.argv[1] in ["-move", "-rename"] and (len(sys.argv)<4 or len(sys.argv)>4):
	help()
if sys.argv[1] in ["-delete"] and (len(sys.argv)<3 or len(sys.argv)>3):
	help()	
if sys.argv[1] in ["-reset", "-reboot", "-scheduled"] and (len(sys.argv)<2 or len(sys.argv)>2):   
	help()		
if sys.argv[1] == "-move":
	move(sys.argv[2], sys.argv[3])
if sys.argv[1] == "-scheduled":
	scheduledOperations()
if sys.argv[1] == "-delete":
	delete(sys.argv[2])
if sys.argv[1] == "-rename":
	rename(sys.argv[2], sys.argv[3])	
if sys.argv[1] == "-reset":
	reset()
if sys.argv[1] == "-reboot":
	reboot()	