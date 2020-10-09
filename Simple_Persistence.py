import os

simple_path = os.path.curdir + "\\Assignment 1 - data\\simple\\"
long_path = os.path.curdir + "\\Assignment 1 - data\\long\\"
large_path = os.path.curdir + "\\Assignment 1 - data\\large\\"

def printingfilecontents(path):
    for f_name in os.listdir(path):
        if f_name.endswith('.txt'):
            simple_file = open(path+f_name, "r")
        s_file = simple_file.readlines()
        for entry in s_file:
            print(entry)
    simple_file.close()

printingfilecontents(long_path)
