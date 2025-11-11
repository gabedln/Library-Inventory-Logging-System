# Mari Gabriel D. De Leon
# CMSC 12 - Y6L
# December 05, 2024
# CMSC 12 Project: Library Inventory and Logging System

# Description: The project revolves around making a Library inventory system in Python. This system should be able to store information about the books in the library, maintain a borrower's list per book,
# and lastly maintain a log of transactions that have happened in the system.

# This file will be the books module of the entire project.

from cryptography.fernet import Fernet # imports cryptography library 

# this part is for the add book function
def addBook(bookTitle, bookAuthor, bookPublished): # takes these parameters
    global bookDict # sets the variables that we are using as global
    global id

    bookID = "B" + str(id) # creates bookID format
    borrowerList = [] # creaters initial blank borrowerlist
    bookInfo = [bookTitle, bookAuthor, bookPublished, "Available", borrowerList] # adds all the info in one list
    bookDict[bookID] = bookInfo # adds a dictionary entry with bookInfo as value    
    id+=1 # increments id
    saveLibrary()

# this part is for the delete book function
def deleteBook(bookTitle, bookAuthor):
    global bookDict

    for key, value in bookDict.items(): # iterates through
        if (value[0].lower().strip() == bookTitle.lower().strip() # if value is found, meaning they're the same
            and value[1].lower().strip() == bookAuthor.lower().strip()):
            bookDict.pop(key) # removes key
            saveLibrary()
            return True
    return False

# this part is for the delete all books function
def deleteAllBooks():
    bookDict.clear() # clears book dictionary
    saveLibrary()

# this part is for the view book function
def viewBook(bookTitle, bookAuthor):
    import borrow # imports modules
    import logbook
    global bookDict # sets global variable
    nameOfBorrowers = [] # list for name of borrowers
    nameOfBorrowersString = "" # initial string, meaning blank
    for key, value in bookDict.items():
            if (value[0].lower().strip()==bookTitle.lower() # if value is the same
                and value[1].lower().strip()==bookAuthor.lower()):
                bookID = key # gets information
                title = value[0]
                author = value[1]
                datePublished = value[2]
                status = value[3]
                for borrowID in value[4]: # iterates through list of borrowers in borrowerList
                    for key, value in borrow.borrowDict.items(): # iterates through borrowDict
                        if borrowID == key: # if key and borrowID are matching, gets information
                            logID = value[1]
                            for key, value in logbook.logbookDict.items(): # if logid and key are matching, gets information
                                if logID == key:
                                    nameOfBorrowers.append(value[0])
                if len(nameOfBorrowers)==0: # if there are no borrowers
                    nameOfBorrowersString = "N/A" # string is N/A
                else:
                    for name in nameOfBorrowers: # if there is adds it into name of borrower string
                        nameOfBorrowersString += f"\n{name}"
                info = f"Book ID: {bookID}\nTitle: {title}\nAuthor: {author}\nDate Published: {datePublished}\nStatus: {status}\nList of Borrowers: {nameOfBorrowersString}"
                return info

# this part is for the edit book function
def editBook(bookTitle, bookAuthor, datePublished, status, borrowerList, bookKey): # takes these parameters
    global bookDict
    bookInfo = [ # places info into a list using the parameters
        bookTitle,
        bookAuthor,
        datePublished,
        status,
        borrowerList,
    ]
    bookDict[bookKey] = bookInfo # updates bookDict by changing value of the book in the dictionary
    saveLibrary()
    return

# this part is for the view pending function
def viewPending():
    import borrow # imports other modules
    import logbook

    entries = "" # makes a blank string for entries
    global bookDict
    for key, value in bookDict.items(): # iterates through bookDictionary items
        if value[3].strip().lower() == "unavailable": # checks to see if the status is unavailable
            bookKey = key # if status unavailable, gets book information
            title = value[0]
            author = value[1]
            datePublished = value[2]
            status = value[3]
            borrowers = value[4]
            last = len(borrowers) - 1 # gets the index of the last borrower
            latestBorrower = borrowers[last] # latestBorrower = index from borrowers list, gets the last value in the string
            for key, value in borrow.borrowDict.items(): # iterates through borrowDict items
                if latestBorrower == key: # if the latestborrower that we set is equal to the key of borrowDict
                    returnDate = value[2] # gets information
                    logID = value[1]
                    for key, value in logbook.logbookDict.items(): # similar but to the logbookDict
                        if logID.strip() == key.strip(): # gets informaiton
                            name = value[0] 
                    log = ( # adds information in one variable, a string
                        f"\nBook ID: {bookKey}\n"
                        f"Title: {title}\n"
                        f"Author: {author}\n"
                        f"Date Published: {datePublished}\n"
                        f"Status: {status}\n"
                        f"Last Borrower: {name}\n"
                        f"Expected Date of Return: {returnDate}\n"
                    )
                    entries+=log # adds the log to the entries
    return entries # returns the entries

# this function saves the state of the books module
def saveLibrary():
    global bookDict  # makes the bookDict variable global for access
    global id  # makes the id variable global for access

    # opens the library data file in write mode to store book information
    fileHandle = open("libraryData.dat", "w")
    fileHandle.write(str(id) + "\n")  # writes the current id as the first line
    for key, value in bookDict.items():  # iterates through the dictionary
        joinedBorrowers = ",".join([borrower.strip() for borrower in value[4]])  # joins borrower list into a single string
        output = (
            f"{key}|{value[0]}|{value[1]}|{value[2]}|{value[3]}|{joinedBorrowers}\n"
        )  # formats the book information as a single line
        fileHandle.write(output)  # writes the book information to the file
    fileHandle.close()  # closes the file after writing

    # encrypts the library data for security
    with open("libraryData.dat", "rb") as libraryOrig:
        original = libraryOrig.read()  # reads the original file content

    encrypted = f.encrypt(original)  # encrypts the content using the Fernet key

    with open("libraryData.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted)  # writes the encrypted content back to the file

# this try function loads the dat file and key available, 
# if there is none, those after except will be the one that will run. meaning a new file is created
try:
    bookDict = {}
    with open("myKeyBooks.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)

    with open("libraryData.dat", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)
    with open("libraryData.dat", "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    readHandle = open("libraryData.dat", "r")
    id = int(readHandle.readline())
    for line in readHandle:
        book = line.strip().split("|")
        bookID = book[0]
        title = book[1]
        author = book[2]
        datePublished = book[3]
        status = book[4]
        if book[5] == "":
            borrowers = []
        else:
            borrowers = book[5].strip().split(",")
        bookDict[bookID] = [
            title,
            author,
            datePublished,
            status,
            borrowers,
        ]
    readHandle.close()
    saveLibrary()

except:
    id = 1
    bookDict = {}
    key = Fernet.generate_key()
    with open("myKeyBooks.key", "wb") as key_file:
        key_file.write(key)
    f = Fernet(key)