# Mari Gabriel D. De Leon
# CMSC 12 - Y6L
# December 05, 2024
# CMSC 12 Project: Library Inventory and Logging System

# Description: The project revolves around making a Library inventory system in Python. This system should be able to store information about the books in the library, maintain a borrower's list per book,
# and lastly maintain a log of transactions that have happened in the system.

# This file will be the logbook module of the entire project.

from cryptography.fernet import Fernet

# this part is for the visit library function, or adding entries to the logbook
def visitLibrary(personName, date, time, purposeUser):
    global logbookDict # gets global logbookDict
    global id

    logID = "L" + str(id) # makes a logID
    logInfo = [personName, date, time, purposeUser] # makes the information in one list
    logbookDict[logID] = logInfo # creates new entry in logbookDict
    id += 1 # increments the id
    saveLogbook()

# this part is for the view all function, or to view all entries in the logbookDict
def viewAll(): # viewall function
    global logbookDict # global variable
    allEntries = "" # blank all entries string
    for key, value in logbookDict.items(): # iterates through items in logbookDict
        personName = value[0] # gets the information
        date = value[1]
        time = value[2]
        purpose = value[3]
        log = (f"\nLog ID: {key}\n" # places the information into one variable, a string
        f"Person Name: {personName}\n"
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Purpose: {purpose}\n")
        allEntries += log # adds these to the blank string (allEntries) that we made earlier
    return allEntries

# this part is for view transactions per day function, or to view logbook transactions per day
def viewPerDay(viewDate):
    global logbookDict # global dictionary
    perDayDict = {} # temporary dictionary to store per day
    entries = "" # blank entries variable
    for key, value in logbookDict.items(): # iterates through item in logbook dict
        logDate = value[1] 
        if viewDate == logDate: # if viewdate is equal to the logbookdate
            perDayDict[key] = [value[0], logDate, value[2], value[3]] # adds antry into our temp dict 

    if len(perDayDict) == 0: # if length is 0, meaning none was added it just returns
        return
    else:
        for key, value in perDayDict.items(): #else, it iterates through the temp dictionary
            log= ( # gets information, places it into one variable
                f"\nLog ID: {key}\n"
                f"Person Name: {value[0]}\n"
                f"Date: {value[1]}\n"
                f"Time: {value[2]}\n"
                f"Purpose: {value[3]}\n"
            )
            entries += log # adds it to the blank string that we made
        return entries

# this function saves the state of the logbook module
def saveLogbook(): 
    global logbookDict # similar to books save function
    global id

    fileHandle = open("logbookData.dat", "w")
    fileHandle.write(str(id) + "\n")
    for key, value in logbookDict.items():
        output = f"{key}|{value[0]}|{value[1]}|{value[2]}|{value[3]}\n"
        fileHandle.write(output)
    fileHandle.close()

    with open("logbookData.dat", "rb") as logbookOrig:
        original = logbookOrig.read()

    encrypted = f.encrypt(original)

    with open("logbookData.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# this try function loads the dat file and key available, 
# if there is none, those after except will be the one that will run. meaning a new file is created
try:
    logbookDict = {}
    with open("myKeyLogbook.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)

    with open("logbookData.dat", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)
    with open("logbookData.dat", "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    readHandle = open("logbookData.dat", "r")
    id = int(readHandle.readline())
    for line in readHandle:
        usersData = line.strip().split("|")
        logID = usersData[0]
        name = usersData[1]
        date = usersData[2]
        time = usersData[3]
        purpose = usersData[4]
        logbookDict[logID] = [name, date, time, purpose]
    readHandle.close()
    saveLogbook()

except FileNotFoundError:
    id = 1
    logbookDict = {}
    key = Fernet.generate_key()
    f = Fernet(key)
    with open("myKeyLogbook.key", "wb") as key_file:
        key_file.write(key)
