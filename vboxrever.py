# Virtual Box version swapper
# author: Anthony Caudill (tcaudilllg/tcaud123/tcaud)

import shutil

# get home path

vboxHome = open("home.txt", "r")

vboxHomeDir = vboxHome.read()

# load table of vbox configs
    
vboxConfigsData = open("vbox.txt", "r")

vboxNames = []
vboxPaths = []

# read in data

lineIndex = 0
for line in vboxConfigsData:
    
    if lineIndex % 2 == 0:   # even line, therefore it is a name
        vboxNames.append(line)
    else:
        vboxPaths.append(line)
        
    lineIndex += 1
    
    
# show menu    

print("VirtualBox Version Swapper")
    
for nameI in range(len(vboxNames)):

    print((nameI + 1) + ". " + nameI)
    

print ((len(vboxNames)) + ". Quit")


# loop menu

choice = 0
while choice < len(vboxNames):

    print()

    choice = input("Enter selection:")



# load vbox config
# first, nuke existing config
    
os.remove(vboxHomeDir + "/VirtualBox.xml")

# now copy in replacement

shutil.copy(vboxPaths[choice], vboxHomeDir + "/VirtualBox.xml")

print(vboxPaths[choice] + " has replaced content of VirtualBox.xml")
print("Operation suceeded")
