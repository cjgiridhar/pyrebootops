PyRebootOps
--

Often in Windows systems we observe that move or delete operations can't be executed on a file if it's locked.
Files can get locked if different processes start accessing it or if the file has already been loaded in RAM. 

Such problems can be resolved by scheduling file operations for the next system restart before the processes or services start and set locks on the files. 
PyRebootOps uses windows mechanism for scheduling operations on a file so that these operations can be executed during next system restart. 


Features in PyRebootOps1.0:
--

- Schedule - Move, Rename, Delete operations on locked files.
- View and Reset scheduled operations.
- Restart the user system. 


Usage
--
<pre>
***********************************************************
PyRebootOps1.0: Schedule file opeartions to be executed
with the ystem reboot.
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
</pre>


Dependencies
--
- Windows OS
- winreg
- Python 2.6


Contact
--
- Chetan Giridhar cjgiridhar@gmail.com

License
--
GNU General Public License v3.0

Copyright (c) Chetan Giridhar, 2012
