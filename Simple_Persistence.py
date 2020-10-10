import os
import sys
import pickle

simple_path = os.path.curdir + "\\Assignment 1 - data\\simple\\"
long_path = os.path.curdir + "\\Assignment 1 - data\\long\\"
large_path = os.path.curdir + "\\Assignment 1 - data\\large\\"
long_serializing = os.curdir + "\\Assignment 1 - data\\long serialized\\"

class Employee(object):
    def __init__(self, id, firstname, lastname, year):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.id = id
    def __str__(self):
        string = f"{self.firstname}, {self.lastname} hired in: {self.year} with id number: {self.id}"
        return string

class LargeEmployee(Employee):
    someData = []

def addemployee(id, firstname, lastname, hiredate):
    with open(long_path+'!2.txt', 'w+') as f:
        instream = id, firstname, lastname, hiredate
        f.write(instream)
        f.close()

def deleteemployee(id, directory):
    path = os.path.curdir+"\\Assignment 1 - data\\"+directory
    try:
        if id in directory:
            os.remove(path)
        else:
            print("The file you were looking for could not be found")
    except RuntimeError:
        print("You broke something, great job")

def updateemployee(id, firstname, lastname, hiredate):
    # updates file with the records you designate
    # cannot change id (like a primary key)
    for f in os.listdir(os.path.curdir+"\\Assignment 1 - data\\"):
        for s in os.listdir(os.path.curdir+"\\Assignment 1 - data\\simple"):
            print(s)
    pass

def serializeallemployee():
    # iterate through long dir and create Employee object from file
    # serialize object and then output to a new file in dir /long serialized/ with proper .ser extension
    if os.path.isdir(long_serializing):
        pass
    else:
        os.mkdir(long_serializing)
    for e in os.listdir(long_path):
        if e.endswith('.txt'):
            noserial = open(long_path+e, 'r+')
            dumper = noserial.readlines()
            serialized = open(long_serializing+e.replace('.txt','.ser',-1), 'wb')
            for d in dumper:
                pickle.dump(d, serialized)
    noserial.close()
    serialized.close()

def getserializedemployee(id):
    # id is the param and will search for the file with the input id
    # returns the deserialized data as an Employee object
    id = 0
    firstname = ""
    lastname = ""
    year = 0
    for f in os.listdir(long_serializing):
        if(f.startswith(id)):
            f = open(long_serializing+id + '.ser')
        o_file = f.readlines()
        for n in o_file:
            data = n.split()
    out = Employee(id, firstname, lastname, year)
    pass

def printemployees(path):
    e = Employee(0,"","",0)
    for f in os.listdir(path):
        if f.endswith('.txt'):
            file = open(path+f, "r")
        n_file = file.readlines()
        for n in n_file:
            elements = n.split(', ')
            e.id = elements[0]
            e.firstname = elements[1]
            e.lastname = elements[2]
            e.year = elements[3]
            e.year = e.year.strip('\n')
            print(e)

def printpeopledetails(path):
    for f_name in os.listdir(path):
        if f_name.endswith('.txt'):
            simple_file = open(path+f_name, "r")
        s_file = simple_file.readlines()
        for entry in s_file:
            print(entry)
    simple_file.close()

updateemployee(1,"Vera", "Lambert", 1988)
