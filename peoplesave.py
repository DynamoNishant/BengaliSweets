import mainmenu
import pickle
import os
from datetime import date
from random import randint


def peepsmenu(type):
    global FILENAME
    FILENAME = type + '.dat'

    print(f"\t\t\t\t\t\t\t\t {type} MENU\n\n")

    print(f"\t\t1. Enter {type} data\n\t\t2. Display {type} data\n\t\t3. Search {type} data\n\t\t4. Delete {type} data\n\t\t5. GO BACK!!!")

    with open(FILENAME, 'wb') as file:
        entryformat = {"Name": ('ID', 'Date Added', 'Age')}
        filesize = os.path.getsize(FILENAME)
        if filesize == 0: # fills in colnames if the file is empty
            pickle.dump(entryformat,file)



    opt = input(">> ")

    if opt == '1':
        mainmenu.procs()
        saver(type)

    elif opt == '2':
        mainmenu.procs()
        shower(type) # YES, SHOWER

    elif opt == '3':
        mainmenu.procs()
        finder(type)

    elif opt == '4':
        mainmenu.procs()
        remover(type)

    elif opt == '5':
        mainmenu.main()

def saver(type):
    print("<>"*20, f"{type} DATA ENTRY MODULE", "<>"*20)

    file = open(FILENAME, 'wb')

    again = 'y'
    tempdata = dict()
    while again == 'y':
        name = input(f"Enter the name of {type}:")
        id = str(randint(10000, 99999))
        date_add = str(date.today())
        age = input(f"Enter the age of {type} ")

        tempdata[name] = (id, date_add, age)

        pickle.dump(tempdata, file)
        tempdata.clear()

        again = input("Enter another data? (y/n)").lower()
    file.close()

    peepsmenu(type)



def shower(type):
    print("*"*25, "SHOWER OF DATA INCOMING" ,"*"*25)

    with open(FILENAME, 'rb') as file:
        data = pickle.load(file)
        print(data)
        peepsmenu(type)

def finder(type):
    pass
def remover(type):
    pass
