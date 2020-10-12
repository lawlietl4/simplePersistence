import os
import sys
import pickle

data_path = os.curdir+"\\Assignment 1 - data\\"
simple_path = data_path +"simple\\"
long_path = data_path+"long\\"
large_path = data_path+"large\\"
long_serializing = data_path+"long serialized\\"
large_serialized= data_path+"large serialized\\"
simple_serializing = data_path+'simple serialized\\'

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

def findemployeebyid(employee_id):
    #searches all directories for first employee record that matches the supplied id
    #returns an Employee object
    for f in os.listdir(data_path):
        if os.path.exists(simple_path+employee_id+'.txt'):
            with open(simple_path+employee_id+'.txt','r') as fi:
                elements = fi.readlines()
                for el in elements:
                    n = el.split(', ')
                    emlid = n[0]
                    elastname = n[1]
                    efirstname = n[2]
                    ehiredate = n[3]
                    ehiredate = ehiredate.strip('\n')
                    e = Employee(emlid, elastname, efirstname, ehiredate)
                print(e)
                break
        elif os.path.exists(large_path+employee_id+'.txt'):
            with open(large_path+employee_id+'.txt', 'r') as fi:
                elements = fi.readlines()
                for e in elements:
                    n = e.split(', ')
                    eid = n[0]
                    elastname = n[1]
                    efirstname = n[2]
                    ehiredate = n[3]
                    ehiredate = ehiredate.strip('\n')
                em = Employee(eid,elastname,efirstname,ehiredate)
                print(em)
                break
        elif os.path.exists(long_path+employee_id+'.txt'):
            with open(long_path+employee_id+'.txt','r') as fi:
                elements = fi.readlines()
                for elem in elements:
                    n = elem.split(', ')
                    emplid = n[0]
                    elastname = n[1]
                    efirstname = n[2]
                    ehiredate = n[3]
                    ehiredate = ehiredate.strip('\n')
                    em = Employee(emplid, elastname, efirstname, ehiredate)
                print(em)
                break
        else:
            break

def findemployeebylastname(lastname):
    #searches all employees for the first record that corresponds with the last name specified
    #returns an Employee object
    for file_name in os.listdir(long_path):
        if os.path.isfile(long_path+file_name):
            with open(long_path+file_name, 'r') as file:
                n = file.readlines()
                for lines in n:
                    lines = lines.lower()
                    l = lines.split(', ')
                    if lastname == l[2]:
                        empid = l[0]
                        emplast = l[1]
                        empfirst = l[2]
                        emphire = l[3]
                        emphire = emphire.strip('\n')
                        em = Employee(empid,empfirst,emplast,emphire)
                        print(em)
        break

def findallemployeesbylastname(lastname):
    #searches all records for all employees with the supplied last name
    #returns list of results
    for file_name in os.listdir(long_path):
        if os.path.isfile(long_path+file_name):
            with open(long_path+file_name, 'r') as file:
                n = file.readlines()
                for lines in n:
                    lines = lines.lower()
                    l = lines.split(', ')
                    if lastname in l:
                        empid = l[0]
                        emplast = l[1]
                        empfirst = l[2]
                        emphire = l[3]
                        emphire = emphire.strip('\n')
                        em = Employee(empid,empfirst,emplast,emphire)
                        print(em)
                    break
    pass

def printserializeddetails(path):
    #iterates over all serialized files in a directory
    #deserialize into an Employee object and print __str__
    index = 1
    for f in os.listdir(data_path+path+'\\'):
        if(os.path.isdir(data_path+path+'\\')):
            for file in os.listdir(data_path+path+'\\'):
                if file.endswith('.txt') and index != 10001:
                    with open(data_path+path+'\\'+str(index)+'.txt', 'r') as f:
                        data = f.readlines()
                        for line in data:
                            elements = line.split(', ')
                            employee_id = elements[0]
                            firstname = elements[1]
                            lastname = elements[2]
                            year = elements[3]
                            year = year.strip('\n')
                        e = Employee(employee_id,firstname,lastname,year)
                        print(e)
                        index += 1
                elif file.endswith('.ser'):
                    with open(path+str(index)+'.ser','rb')as f:
                        data = pickle.Unpickler(f).load()
                        elements = data.split(', ')
                        employee_id = elements[0]
                        firstname = elements[1]
                        lastname = elements[2]
                        year = elements[3]
                        year = year.strip('\n')
                        out = Employee(employee_id, firstname, lastname, year)
                        print(out)
                        index += 1
                elif index == 10001:
                    break
            if index ==10001:
                break
        if index == 10001:
            break

def getallemployees(path):
    #iterates over all serialized files in a directory
    #deserialize each object and put into hashmap keyed by employeeid
    #return the hashmap of all entries
    allemployees = dict()
    index = 1
    for f in os.listdir(data_path+path+'\\'):
        if(f.endswith('.ser')):
            with open(data_path+path+'\\'+str(index)+'.ser','rb')as f:
                data = pickle.Unpickler(f).load()
                elements = data.split(', ')
                allemployees[elements[0]] = elements
        index += 1
    return allemployees

def printallemployees():
    #calls on getallemployees
    #loops through returned hashmap and prints each employees' details
    index = 0
    emplist = getallemployees('long serialized')
    for entries in emplist:
        if index == 10001:
            break
        print(emplist[entries])
        index += 1
    pass

def addemployee(employee_id, firstname, lastname, hiredate):
    with open(long_path+f'{employee_id}'+'.txt', 'w+') as f:
        instream = f"{employee_id}, {firstname}, {lastname}, {hiredate}\n"
        instream = instream.swapcase()
        f.write(instream)
        f.close()

def deleteemployee(employee_id, directory):
    path = data_path+directory+'\\'
    try:
        if employee_id+'.txt' in os.listdir(path):
            os.remove(path+employee_id+'.txt')
            print("File deleted")
        else:
            print("The file you were looking for could not be found")
    except RuntimeError:
        print("You broke something, great job")

def updateemployee(employee_id, firstname, lastname, hiredate):
    # updates file with the records you designate
    # cannot change id (like a primary key)
    for f in os.listdir(data_path):
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
    if not os.path.isdir(simple_serializing):
        os.mkdir(simple_serializing)
    for e in os.listdir(simple_path):
        if e.endswith('.txt'):
            noserial = open(simple_path+e, 'r+')
            dumper = noserial.readlines()
            serialized = open(simple_serializing+e.replace('.txt','.ser',-1), 'wb')
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
    for f_name in os.listdir(data_path+path+'\\'):
        if f_name.endswith('.txt'):
            with open(data_path+path+'\\'+f_name, "r") as simple_file:
                s_file = simple_file.readlines()
                for entry in s_file:
                    print(entry)

printallemployees()