# Here the glob function is use to 

#The glob module uses the os.scandir() 
# and fnmatch.fnmatch() functions to match file patterns. 
# It supports wildcards such as * (matches any number of characters), ? 
# (matches a single character), and character ranges like [a-z]. For example, glob.glob('*.txt')
#  will match all files ending with .txt.

import glob

myfiles = glob.glob("journal/*.txt")

for filepath in myfiles:
    with open (filepath, 'r') as file:
        print(file.read())


