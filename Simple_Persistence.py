import os
import sys
import pickle

simple_path = os.path.curdir + "\\Assignment 1 - data\\simple\\"
long_path = os.path.curdir + "\\Assignment 1 - data\\long\\"
large_path = os.path.curdir + "\\Assignment 1 - data\\large\\"
long_serializing = os.curdir + "\\Assignment 1 - data\\long serialized\\"
large_serialized= os.curdir + "\\Assignment 1 - data\\large serialized\\"

class Employee(object):
    def __init__(self, employee_id, firstname, lastname, year):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.employee_id = employee_id
    def __str__(self):
        string = f"{self.firstname}, {self.lastname} hired in: {self.year} with id number: {self.employee_id}"
        return string

class LargeEmployee(Employee):
    someData = []

def addemployee(employee_id, firstname, lastname, hiredate):
    with open(long_path+f'{employee_id}'+'.txt', 'w+') as f:
        instream = f"{employee_id}, {firstname}, {lastname}, {hiredate}\n"
        instream = instream.swapcase()
        f.write(instream)
        f.close()

def deleteemployee(employee_id, directory):
    path = os.path.curdir+"\\Assignment 1 - data\\"+directory+'\\'
    try:
        if employee_id+'.txt' in os.listdir(path):
            os.remove(path+employee_id+'.txt')
        else:
            print("The file you were looking for could not be found")
    except RuntimeError:
        print("You broke something, great job")

def updateemployee(employee_id, firstname, lastname, hiredate):
    # updates file with the records you designate
    # cannot change id (like a primary key)
    for f in os.listdir(os.path.curdir+"\\Assignment 1 - data\\"):
        if os.path.exists(simple_path+employee_id+'.txt'):
            with open(simple_path+employee_id+'.txt','w+') as fi:
                fi.write(f'{employee_id}, {firstname}, {lastname}, {hiredate}\n'.swapcase())
                break
        elif os.path.exists(large_path+employee_id+'.txt'):
            with open(large_path+employee_id+'.txt', 'w+') as fi:
                fi.write(f'{employee_id}, {firstname}, {lastname}, {hiredate}\n'.swapcase())
                break
        elif os.path.exists(long_path+employee_id+'.txt'):
            with open(long_path+employee_id+'.txt','w+') as fi:
                fi.write(f'{employee_id}, {firstname}, {lastname}, {hiredate}\n'.swapcase())
                break
        else:
            break

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

def getserializedemployee(employee_id):
    # id is the param and will search for the file with the input id
    # returns the deserialized data as an Employee object
    for f in os.listdir(long_serializing):
        if(f.startswith(employee_id)):
            with open(long_serializing+employee_id+'.ser','rb')as f:
                data = pickle.Unpickler(f).load()
                elements = data.split(', ')
                employee_id = elements[0]
                firstname = elements[1]
                lastname = elements[2]
                year = elements[3]
                year = year.strip('\n')
                out = Employee(employee_id, firstname, lastname, year)
    print(out)

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
    for f_name in os.listdir(os.path.curdir+'\\Assignment 1 - data\\'+path+'\\'):
        if f_name.endswith('.txt'):
            with open(os.path.curdir+'\\Assignment 1 - data\\'+path+'\\'+f_name, "r") as simple_file:
                s_file = simple_file.readlines()
                for entry in s_file:
                    print(entry)



updateemployee('1','vera','lambert','1920')