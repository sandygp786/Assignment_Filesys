'''
import platform----To check built-in modules
import sys---------Provides access to system-specific parameters
                   and functions, such as command-line arguments,
                   module paths, and exit status.
import math--------mathematical functions like square root,
                   trigonometric functions, logarithms, etc.
import os----------Facilitates interaction with the operating
                   system, including file system manipulation,
                   environment variables, and process management.
#x = dir(platform)----command to check all built in modules
print(x)
'''

import os
file_name = 'sample.txt'
file1 = open(file_name,'r')
data1 = file1.readline()
data2 = file1.readline()
print("Reading File Content:")
print("Line 1 :",data1.strip())
print("Line 2 :",data2.strip())
file1.close()

#Going to Rename sample.txt file
os.rename('sample.txt', 'sample1.txt')
#rename file to sample1.txt done.
#Reading sample.txt file Again

print(('\n') *3)
try:
    file1 = open('sample.txt','r')
    file1.close()
except FileNotFoundError:
    print('Error: The file ' + file_name + ' was not found.')
