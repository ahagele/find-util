
# version 3

# Python exercise to duplicate command line tool 'find'
# 13/11/22 AH
# find [<path>] [-name <pattern>] [-print]
# default: path = '.' pattern = '*'

import subprocess
import fnmatch 
import os 
  
default_pattern = '*'
default_folder = '.'


pattern = default_pattern
folder = default_folder

# command line processing


print(f"{pattern=}")
  
files = os.listdir(folder) 
for name in files: 
  if fnmatch.fnmatch(name, pattern):
    print (f"{name}")
    
print("sub process")   
p = subprocess.run(["ls","-ls"])   
#p = subprocess.Popen("ls -lh", stdout=subprocess.PIPE, shell=True)
#p = subprocess.Popen("cat ex1.py", shell=True)

#print(p.communicate())

# add support for -type d f option
#more changes
#and more
#even more

