# Virtual-Box-reVer
Python script to swap out Oracle Virtual Box configs (allowing multiple versions on same host)

## How to use

In the folder containing the script make two files, home.txt and vbox.txt.

home.txt should contain the path to your VirtualBox HOME folder. This is usually the path to your user account folder followed by ".VirtualBox".

vbox.txt will contain a list of all the different configs you want to be available to you. Items in this list have the following form: [name of item]\n[filename]

Generally you'll want to install each Virtual Box version you want to use one after the other, pausing in between to copy the VirtualBox.xml file each version
creates for itself in HOME folder into the folder containing this script and renaming it to something appropriate for your purpose for that installation.

Vbox.txt should probably look something like this:

Vbox 5 32-bit
vbox5_32.xml
Vbox 6.1 64-bit
vbox6.1_32.xml

When you run the script you'll get a menu with the options you created. Making a selection will overwrite the existing VirtualBox.xml file with the associated copy,
thus enabling you to use that version of Virtual Box.
