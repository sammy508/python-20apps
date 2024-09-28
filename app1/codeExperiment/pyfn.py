# Here the glob function is use to 

# Understanding Python's glob Module

# The glob module in Python is used for file path pattern matching.
#    It allows you to search for files with specific patterns, similar to how you would use wildcards in Unix or Linux shell commands. The module provides a way to perform file operations
#    without having to loop through directories manually.

import glob

myfiles = glob.glob("journal/*.txt")

for filepath in myfiles:
    with open (filepath, 'r') as file:
        print(file.read())