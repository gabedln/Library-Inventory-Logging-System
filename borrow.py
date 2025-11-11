# Mari Gabriel D. De Leon
# CMSC 12 - Y6L
# December 05, 2024
# CMSC 12 Project: Library Inventory and Logging System

# Description: The project revolves around making a Library inventory system in Python. This system should be able to store information about the books in the library, maintain a borrower's list per book,
# and lastly maintain a log of transactions that have happened in the system.

# This file will be the borrow module of the entire project.

from cryptography.fernet import Fernet

# this part is for the borrow book function
def borrowBook(titleBorrow, authorBorrow, returnDate, logID): # takes the following parameters
    global borrowIDNumber # global borrowID variable
    import books # imports books module

    borrowID = "BL" + str(borrowIDNumber) # creates borrowID with that format

    for key, value in books.bookDict.items(): # iterates through bookdict and gets information
        title = value[0].strip().lower()
        author = value[1].strip().lower()
        status = value[3].strip().lower()

        if ( # if title matches with the user input
            titleBorrow.strip().lower() == title
            and authorBorrow.strip().lower() == author
        ):
            if status == "available": # checks if status is available
                bookID = key # gets the information the book, specifically the bookID
                value[3] = "Unavailable" # updates status of the book
                value[4].append(borrowID) # adds the borrowID to the list of borrowers
                books.saveLibrary() # saves the status of books module
                borrowDict[borrowID] = [bookID, logID, returnDate]
                borrowIDNumber +=1 # increments borrowIDNumber
                saveborrowDict()
                return 1 # 1 means book found

            elif status == "unavailable": # if status is unavailable it just returns
                return 0 # 0 means unavailable, none means no book was found

# this part is for the return book function
def returnBook(titleReturn, authorReturn):
    import books # imports books function
    # for return book function, the functionalities of this is just similar to borrow book, but in the case of return book
    # the value will be updated to available from unavailable, and there will be no appending of borrowerID. that is the
    # only main difference of borrow and return books, but their logic is almost the same
    for key, value in books.bookDict.items():
        title = value[0].strip().lower()
        author = value[1].strip().lower()
        status = value[3].strip().lower()

        if (
            titleReturn.strip().lower() == title
            and authorReturn.strip().lower() == author
        ):
            if status == "unavailable":
                value[3] = "Available"
                books.saveLibrary()
                return 1 # 1 means book is successfully returned

            elif status == "available":
                return 0 # 0 means book is currently available, none means no book

# this part is for the view all entries function
def viewAll():
    import books # imports books and logbooks
    import logbook

    global borrowDict # global borrowDict variable
    allEntries = "" # blank allEntries variable
    for key, value in borrowDict.items(): # iterates through item in borrowDictionary
        borrowID = key # gets the following information
        bookID = value[0]
        logID = value[1]
        returnDate = value[2]
        for key, value in books.bookDict.items(): # iterates to check if the information is a match
            if bookID == key:
                title = value[0] # gets more information from books module, gets title and author of book
                author = value[1]
                datePublished = value[2]
        for key, value in logbook.logbookDict.items(): # iterates but this time in logbookDict
            if logID == key: # checks to see if information is a match and if it is it gets the value of name of borrower
                name = value[0]
        try:
            log = ( # adds all the information into one variable/string using f string
                f"\nBorrow ID: {borrowID}"
                f"\nTitle: {title}"
                f"\nAuthor: {author}"
                f"\nDate Published: {datePublished}"
                f"\nDate Return: {returnDate}"
                f"\nBorrower: {name}\n"
            )
        except:
            log = "" # if for example, there is one variable that is failed to get, then it will just be blank 
            # assumed that this is for books that were deleted

        allEntries += log # adds the log variable to allEntries string we made
    return allEntries # returns all entries

# this part is for the view expected returns function
def viewExpected(viewDate):
    import logbook
    import books
    global borrowDict
    expectedDict = {}
    entries = ""

    for key, value in borrowDict.items():
        returnDate = value[2]

        if viewDate == returnDate:
            expectedDict[key]=[value]
            borrowID = key
            bookID = value[0]
            logID = value[1]
            for key, value in books.bookDict.items():
                if bookID == key:
                    title = value[0]
                    author = value[1]
                    datePublished = value[2]
                    status = value[3]
            for key, value in logbook.logbookDict.items():
                if logID == key:
                    name = value[0]

            try:
                log = (
                    f"\nBorrow ID: {borrowID}"
                    f"\nTitle: {title}"
                    f"\nAuthor: {author}"
                    f"\nDate Published: {datePublished}"
                    f"\nStatus: {status}"
                    f"\nBorrower: {name}"
                )
            except:
                log=""

            entries+=log

    if len(expectedDict)==0 or entries=="":
        return
    else:
        return entries

# this function saves the current state of the borrow module
def saveborrowDict(): # similar to the previous save functions
    global borrowIDNumber
    global borrowDict
    fileHandle = open("borrowData.dat", "w")
    fileHandle.write(str(borrowIDNumber) + "\n")
    for key, value in borrowDict.items():
        output = f"{key}|{value[0]}|{value[1]}|{value[2]}\n"
        fileHandle.write(output)
    fileHandle.close()

    with open("borrowData.dat", "rb") as borrowOrig:
        original = borrowOrig.read()

    encrypted = f.encrypt(original)

    with open("borrowData.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# this try function loads the dat file and key available, 
# if there is none, those after except will be the one that will run. meaning a new file is created
try:
    borrowDict = {}
    with open("myKeyBorrow.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)

    with open("borrowData.dat", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)
    with open("borrowData.dat", "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    readHandle = open("borrowData.dat", "r")
    borrowIDNumber = int(readHandle.readline())
    for line in readHandle:
        userData = line.strip().split("|")
        borrowID = userData[0]
        bookID = userData[1]
        logID = userData[2]
        returnDate = userData[3]
        borrowDict[borrowID] = [bookID, logID, returnDate]
    readHandle.close()
    saveborrowDict()

except:
    borrowIDNumber = 1
    borrowDict = {}
    key = Fernet.generate_key()
    f = Fernet(key)
    with open("myKeyBorrow.key", "wb") as key_file:
        key_file.write(key)

