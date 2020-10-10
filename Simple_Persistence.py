import os
import re

simple_path = os.path.curdir + "\\Assignment 1 - data\\simple\\"
long_path = os.path.curdir + "\\Assignment 1 - data\\long\\"
large_path = os.path.curdir + "\\Assignment 1 - data\\large\\"

class Employee(object):
    def __init__(self, id, firstname, lastname, year):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.id = id
    def __str__(self):
        string = f"{self.firstname}, {self.lastname} hired in: {self.year} with id number: {self.id}"
        return string

class Large_employee(Employee):
    someData = []

def printemployees(path):
    e = Employee(0,"","",0)
    for f in os.listdir(path):
        if f.endswith('.txt'):
            file = open(path+f, "r")
            file.read
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

printemployees(long_path)
