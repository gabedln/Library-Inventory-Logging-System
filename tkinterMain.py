# Mari Gabriel D. De Leon
# CMSC 12 - Y6L
# December 05, 2024
# CMSC 12 Project: Library Inventory and Logging System

# Description: The project revolves around making a Library inventory system in Python. This system should be able to store information about the books in the library, maintain a borrower's list per book,
# and lastly maintain a log of transactions that have happened in the system.

# This file will be the tkinter file, and will primarily hold all the functions.

# this part is for the import of the other modules, format is import (module name)
import tkinter 
import books
import borrow
import logbook
from tkinter import PhotoImage, messagebox # tkinter is the only third party library here, PhotoImage came from tkinter too

# sets root to library, tkinter.Tk(), basically makes the frame
library = tkinter.Tk() 
# part to specify the dimentions of the window, and title
library.title("CMSC 12 Project: Library Inventory and Logging System")
library.geometry("800x530")

# Everything under this comment is frame for the menus, frame is basically placeholder for element in tkinter
mainMenuFrame = tkinter.Frame(library, bg="#393131") # library means it is placed in the root, bg= changes the background color
booksMenuFrame = tkinter.Frame(library, bg="#393131")
booksHeaderFrame = tkinter.Frame(library, bg="#393131")
borrowMenuFrame = tkinter.Frame(library, bg="#393131")
borrowHeaderFrame = tkinter.Frame(library, bg="#393131")
logbookMenuFrame = tkinter.Frame(library, bg="#393131")
logbookHeaderFrame = tkinter.Frame(library, bg="#393131")

# Everything under this comment is frame for the books module
addBookFrame = tkinter.Frame(library, bg="#393131")
viewBookFrame = tkinter.Frame(library, bg="#393131")
bookDetailsFrame = tkinter.Frame(library, bg="black", border=7) # border = adds a border to the frame
deleteBookFrame = tkinter.Frame(library, bg="#393131")
editBookFrame = tkinter.Frame(library, bg="#393131")
viewPendingFrame = tkinter.Frame(library, bg="black", border=7)

# Everything under this comment is frame for the borrow module
borrowBookFrame = tkinter.Frame(library, bg="#393131")
returnBookFrame = tkinter.Frame(library, bg="#393131")
viewAllBorrowFrame = tkinter.Frame(library, bg="black", border=7)
viewExpectedFrame = tkinter.Frame(library, bg="black", border=7)

# Everything under this comment is frame for the logbook module
visitLibraryFrame = tkinter.Frame(library, bg="#393131")
viewAllLogbookFrame = tkinter.Frame(library, bg="black", border=7)
viewPerDayFrame = tkinter.Frame(library, bg="black", border=7)

# This part is for all the image headers used
headingimg = PhotoImage(file="headers/mainMenuHeading.png") # PhotoImage(file=), gets the image file from specific folder titled headers, then gets .png
mainMenuHeading = tkinter.Label(mainMenuFrame, image=headingimg, bd=0) # creates a label with the image on it, bd=0 removes the border of the image
booksHeading = PhotoImage(file="headers/booksHeading.png")
booksHeader = tkinter.Label(booksHeaderFrame, image=booksHeading, bd=0)
borrowHeading = PhotoImage(file="headers/borrowHeading.png")
borrowHeader = tkinter.Label(borrowHeaderFrame, image=borrowHeading, bd=0)
logbookHeading = PhotoImage(file="headers/logbookHeading.png")
logbookHeader = tkinter.Label(logbookHeaderFrame, image=logbookHeading, bd=0)
addBookimg = PhotoImage(file="headers/addBookHeading.png")
addBookHeader = tkinter.Label(library, image=addBookimg, bd=0)
viewBookimg = PhotoImage(file="headers/viewBookHeader.png")
viewBookHeader = tkinter.Label(library, image=viewBookimg, bd=0)
deleteBookimg = PhotoImage(file="headers/deleteBookHeader.png")
deleteBookHeader = tkinter.Label(library, image=deleteBookimg, bd=0)
editBookimg = PhotoImage(file="headers/editBookHeader.png")
editBookHeader = tkinter.Label(library, image=editBookimg, bd=0)
viewPendingimg = PhotoImage(file="headers/viewPendingHeader.png")
viewPendingHeader = tkinter.Label(library, image=viewPendingimg, bd=0)
borrowBookimg = PhotoImage(file="headers/borrowBookHeader.png")
borrowBookHeader = tkinter.Label(library, image=borrowBookimg, bd=0)
returnBookimg = PhotoImage(file="headers/returnBookHeader.png")
returnBookHeader = tkinter.Label(library, image=returnBookimg, bd=0)
viewAllBorrowimg = PhotoImage(file="headers/viewAllBorrowHeader.png")
viewAllBorrowHeader = tkinter.Label(library, image=viewAllBorrowimg, bd=0)
viewExpectedimg = PhotoImage(file="headers/viewExpectedHeader.png")
viewExpectedHeader = tkinter.Label(library, image=viewExpectedimg, bd=0)
visitLibraryimg = PhotoImage(file="headers/visitLibraryHeader.png")
visitLibraryHeader = tkinter.Label(library, image=visitLibraryimg, bd=0)
viewAllLogbookimg = PhotoImage(file="headers/viewAllLogbookHeader.png")
viewAllLogbookHeader = tkinter.Label(library, image=viewAllLogbookimg, bd=0)
viewPerDayimg = PhotoImage(file="headers/viewPerDayHeader.png")
viewPerDayHeader = tkinter.Label(library, image=viewPerDayimg, bd=0)


# this function calls the main menu, in tkinter .pack() is placing something in the window, and .pack_forget() is removing it
# in this function, all the other menus are removed and only main menu is added. the frames of the other modules are removed, and
# all the needed labels and headers for main menu are packed
def mainMenu():
    booksHeaderFrame.pack_forget()
    booksMenuFrame.pack_forget()
    borrowHeaderFrame.pack_forget()
    borrowMenuFrame.pack_forget()
    logbookMenuFrame.pack_forget()
    logbookHeaderFrame.pack_forget()
    mainMenuHeading.pack(pady=10) # pady = 10 means there is a whitespace of 10 pixels vertically, pady is important for spacing
    booksButton.pack(pady=10)
    borrowButton.pack(pady=10)
    logbookButton.pack(pady=10)
    exitButton.pack(pady=10)
    mainMenuFrame.pack()

# this function is just to show an error message
def errorMessage():
    messagebox.showerror("Empty Library!", "No books in book dictionary!")

# defines book menu, similar to main menu, we're just removing everything from the window and adding all that is needed
def booksMenu():
    bookDict = books.bookDict 
    if len(bookDict) == 0: # if there is no book present meaning length is 0, all the buttons in the books menu cannot be used and it will just show an error message
        viewBookButton.config(command=errorMessage) # config changes the attributes of the tkinter element, command= changes the action of that element
        deleteBookButton.config(command=errorMessage) # in this case the element is a button, so this means the buttons purpose is to just show an error message that there are no books
        deleteAllButton.config(command=errorMessage)
        editBookButton.config(command=errorMessage)
    else:
        viewBookButton.config(command=viewBook) # if len is not equal to zero, configs each element to its proper command
        deleteBookButton.config(command=deleteBook)
        deleteAllButton.config(command=deleteAll)
        editBookButton.config(command=editBook)

    # everything under this is just .pack_forget(), meaning it is just removing unnecessary things on the window
    mainMenuFrame.pack_forget()
    
    addBookFrame.pack_forget()
    viewBookFrame.pack_forget()
    deleteBookFrame.pack_forget()
    editBookFrame.pack_forget()
    bookDetailsFrame.pack_forget()

    submitButton.pack_forget()
    viewBookScrollbar.pack_forget()
    bookDetailsText.pack_forget()

    addBookHeader.pack_forget()
    viewBookHeader.pack_forget()
    deleteBookHeader.pack_forget()
    editBookHeader.pack_forget()
    viewPendingHeader.pack_forget()

    viewPendingFrame.pack_forget()
    viewPendingText.pack_forget()
    viewPendingScrollbar.pack_forget()
    
    backToBooksButton.pack_forget()

    # after removing the unnecessary things from the window, this function then adds the needed elements for the books menu
    booksHeader.pack()
    booksHeaderFrame.pack() # difference of pack from grid is in grid, you can place the elements in rows and columns
    addBookButton.grid(row=0, column=0, pady=10, padx=10) # in this case, we're not putting the element directly on the library, but we're placing it on a frame
    viewBookButton.grid(row=0, column=1, pady=10, padx=10) # we place the elements by using .grid, but the frame is placed using .pack
    deleteBookButton.grid(row=1, column=0, pady=10, padx=10)
    deleteAllButton.grid(row=1, column=1, pady=10, padx=10)
    editBookButton.grid(row=2, column=0, pady=10, padx=10)
    viewPendingButton.grid(row=2, column=1, pady=10, padx=10)
    returnMainButtonBooks.grid(row=3, columnspan=2, pady=10, padx=10, sticky="ew")
    booksMenuFrame.pack()

# defines borrow menu, similar to other menu functions, this clears the window of unnecessary elements and adds only what is needed for the borrow menu
def borrowMenu():
    # removes the main menu and any other frames or elements that were previously packed
    mainMenuFrame.pack_forget()
    borrowBookFrame.pack_forget()
    visitLibraryFrame.pack_forget()
    submitButton.pack_forget()
    backToBorrowButton.pack_forget()
    borrowBookHeader.pack_forget()
    returnBookHeader.pack_forget()
    returnBookFrame.pack_forget()

    # clears the frames and elements related to viewing expected returns
    viewExpectedFrame.pack_forget()
    viewExpectedText.pack_forget()
    viewExpectedDateLabel.pack_forget()
    viewExpectedDate.pack_forget()
    viewExpectedScrollbar.pack_forget()
    viewExpectedHeader.pack_forget()

    # clears the frames and elements related to viewing all borrowed books
    viewAllBorrowFrame.pack_forget()
    borrowText.pack_forget()
    borrowScrollbar.pack_forget()
    viewAllBorrowHeader.pack_forget()

    # ensures the submit button is active for the borrow menu
    submitButton.config(state="normal")

    # after clearing the window, adds all the necessary elements for the borrow menu
    borrowHeaderFrame.pack() 
    borrowHeader.pack()  

    # places buttons for borrowing and returning books, as well as viewing records, using .grid() for layout
    borrowBookButton.grid(row=0, column=0, pady=10, padx=10) 
    returnBookButton.grid(row=0, column=1, pady=10, padx=10)  
    viewAllBorrowButton.grid(row=1, column=0, pady=10, padx=10)  
    viewExpectedButton.grid(row=1, column=1, pady=10, padx=10)  

    # places the button to return to the main menu at the bottom, spanning two columns
    returnMainButtonBorrow.grid(row=3, columnspan=2, pady=10, padx=10, sticky="ew")

    # packs the borrow menu frame, displaying it in the window
    borrowMenuFrame.pack()


# defines logbook menu, similar to other menu functions, this clears the window of unnecessary elements and adds only what is needed for the logbook menu
def logbookMenu():
    # removes the main menu and any other frames or elements that were previously packed
    mainMenuFrame.pack_forget()
    visitLibraryFrame.pack_forget()
    submitButton.pack_forget()
    backToLogbookButton.pack_forget()
    viewAllLogbookFrame.pack_forget()
    viewAllLogbookHeader.pack_forget()
    logbookText.pack_forget()
    logbookScrollbar.pack_forget()
    viewPerDayFrame.pack_forget()
    viewPerDayText.pack_forget()
    viewPerDayHeader.pack_forget()
    viewDateLabel.pack_forget()
    viewDate.pack_forget()
    visitLibraryHeader.pack_forget()

    # after clearing the window, adds all the necessary elements for the logbook menu
    logbookHeaderFrame.pack()
    logbookHeader.pack()
    visitLibraryButton.pack(pady=10)  # button to log a library visit
    viewAllLogbookButton.pack(pady=10)  # button to view all logbook entries
    viewPerDayButton.pack(pady=10)  # button to view logbook entries for a specific day
    returnMainButtonLogbook.pack(pady=10)  # button to return to the main menu
    logbookMenuFrame.pack()

# defines the add book function, clears unnecessary elements from the window, and adds the required elements for the add book form
def addBook():
    # clears any previously entered values in the entry fields for title, author, and date
    titleAdd.delete(0, tkinter.END)
    authorAdd.delete(0, tkinter.END)
    datePublishedAdd.delete(0, tkinter.END)

    # removes the books menu and header frames from the window
    booksMenuFrame.pack_forget()
    booksHeaderFrame.pack_forget()

    # displays the frame and header for adding a book
    addBookFrame.pack(pady=10)
    addBookHeader.pack()

    # positions labels and entry fields for book details
    titleAddLabel.grid(row=0, column=0, sticky="w")
    titleAdd.grid(row=1, column=0)
    authorAddLabel.grid(row=2, column=0, sticky="w")
    authorAdd.grid(row=3, column=0)
    datePublishedAddLabel.grid(row=4, column=0, sticky="w")
    datePublishedAdd.grid(row=5, column=0)

    # configures the submit button to trigger the function that processes adding a book
    submitButton.config(command=processAddBook)
    submitButton.pack(pady=10)
    backToBooksButton.pack()

# processes the addition of a book to the library, includes validation for inputs and handles duplicate entries
def processAddBook():
    bookDict = books.bookDict  # dictionary containing all books in the library

    # retrieves and strips whitespace from user input fields
    bookTitle = titleAdd.get().strip()
    bookAuthor = authorAdd.get().strip()
    bookPublished = datePublishedAdd.get()

    # input validation to ensure all fields are filled
    if not bookTitle:
        messagebox.showerror("Input Error", "Please enter a book title!")
        return
    if not bookAuthor:
        messagebox.showerror("Input Error", "Please enter a book author!")
        return
    if not bookPublished:
        messagebox.showerror("Input Error", "Please enter a publication date!")
        return

    # checks for duplicate books based on title and author
    for key, value in bookDict.items():
        if bookTitle.lower() == value[0].lower() and bookAuthor.lower() == value[1].lower():
            messagebox.showerror("Duplicate Error", "Book is already in the library!")
            return

    # validates the publication date format
    bookPublished = validateDate(bookPublished)
    if bookPublished == None:
        messagebox.showerror("Date Error", "Please input a valid date!")
        return

    # adds the book to the dictionary using the addBook function from the books module
    books.addBook(bookTitle, bookAuthor, bookPublished)

    # success message and clearing the input fields
    messagebox.showinfo("Success!", "Book successfully added!")
    titleAdd.delete(0, tkinter.END)
    authorAdd.delete(0, tkinter.END)
    datePublishedAdd.delete(0, tkinter.END)

# handles the setup for viewing a book, removes unnecessary elements from the window and displays the search form
def viewBook():
    # clears any previously entered values in the title and author input fields
    titleView.delete(0, tkinter.END)
    authorView.delete(0, tkinter.END)

    # removes the books menu and header frames from the window
    booksMenuFrame.pack_forget()
    booksHeaderFrame.pack_forget()

    # displays the header and frame for the view book form
    viewBookHeader.pack()
    viewBookFrame.pack()

    # positions the labels and entry fields for the book title and author
    titleViewLabel.grid(row=0, column=0, sticky="w")
    titleView.grid(row=1, column=0)
    authorViewLabel.grid(row=2, column=0, sticky="w")
    authorView.grid(row=3, column=0)

    # configures the submit button to trigger the function that processes the book search
    submitButton.config(command=processViewBook)
    submitButton.pack(pady=10)

    # adds a back button to return to the books menu
    backToBooksButton.pack()

# processes the search for a book, retrieves and displays details if found
def processViewBook():
    # retrieves and strips user input for book title and author
    bookTitle = titleView.get().strip()
    bookAuthor = authorView.get().strip()

    # clears the book details text area before fetching new info
    bookDetailsText.config(state="normal")
    bookDetailsText.delete("1.0", "end")

    # calls the viewBook function from the books module to fetch book information
    info = books.viewBook(bookTitle, bookAuthor)

    if info:  # if book information is found
        # removes the current view book form and displays the book details frame
        viewBookFrame.pack_forget()
        submitButton.pack_forget()
        backToBooksButton.pack_forget()
        bookDetailsFrame.pack(pady=10)

        # configures the scrollbar and displays the book details
        viewBookScrollbar.config(command=bookDetailsText.yview)
        bookDetailsText.insert("1.0", info)
        bookDetailsText.config(state="disabled")  # disables editing of displayed details

        # adds a back button to return to the books menu
        bookDetailsText.pack(side="left")
        viewBookScrollbar.pack(side="right", fill="y")
        backToBooksButton.pack(pady=20)

        # clears input fields after successful search
        titleView.delete(0, tkinter.END)
        authorView.delete(0, tkinter.END)
        return

    # handles the case where no book is found, clears input fields and shows an error message
    titleView.delete(0, tkinter.END)
    authorView.delete(0, tkinter.END)
    messagebox.showerror("Book Error", "No book found!")


# handles the process of deleting a book from the library
def deleteBook():
    # clears the input fields for book title and author
    titleDelete.delete(0, tkinter.END)
    authorDelete.delete(0, tkinter.END)

    # removes current frames and prepares the delete book view
    booksMenuFrame.pack_forget()
    booksHeaderFrame.pack_forget()
    deleteBookHeader.pack()
    deleteBookFrame.pack()

    # arranges the grid for the delete book input fields
    titleDeleteLabel.grid(row=0, column=0, sticky="w")
    titleDelete.grid(row=1, column=0)
    authorDeleteLabel.grid(row=2, column=0, sticky="w")
    authorDelete.grid(row=3, column=0)

    # sets the command for the submit button to process the deletion
    submitButton.config(command=processDeleteBook)

    # packs the submit button and the back button
    submitButton.pack(pady=10)
    backToBooksButton.pack()


# process of deleting, previous function was just for menu
def processDeleteBook():
    bookTitle = titleDelete.get().strip() # gets info and strips to use for validation
    bookAuthor = authorDelete.get().strip()
    deleted = books.deleteBook(bookTitle, bookAuthor) # runs deleteBook function in books module, that function returns True if a book is deleted, and False if not
    if deleted: # if the value returned is True:
        messagebox.showinfo("Book Deleted!", "Book successfully deleted!") # shows messagebox that info is deleted
        titleDelete.delete(0, tkinter.END) # deletes user entry from entry element
        authorDelete.delete(0, tkinter.END)
    else: # else if the value returned is False:
        messagebox.showerror("Book Error", "No book found!") # prints error message that no book is found
        titleDelete.delete(0, tkinter.END) # deletes user entry from entry element
        authorDelete.delete(0, tkinter.END)
    return


# asks the user for confirmation to delete all books in the library
def deleteAll():
    result = messagebox.askquestion("Confirmation", "Delete all books?")  # displays a confirmation dialog
    if result == "yes":  # if the user confirms with 'yes'
        books.deleteAllBooks()  # calls the deleteAllBooks function in the books module to delete all books
        messagebox.showinfo("Books Deleted", "All books successfully deleted!")  # shows a success message
        booksMenu()  # returns to the books menu after deletion
    elif result == "no":  # if the user confirms with 'no'
        return  # does nothing and exits the function

# sets up the interface for editing a book
def editBook():
    # hides the labels and entry fields for new title, author, and date published
    newTitleLabel.grid_forget()
    newTitle.grid_forget()
    newAuthorLabel.grid_forget()
    newAuthor.grid_forget()
    newDatePublishedLabel.grid_forget()
    newDatePublished.grid_forget()
    
    # clears the entry fields for title and author
    titleEdit.delete(0, tkinter.END)
    authorEdit.delete(0, tkinter.END)
    
    # hides the previous book menu components
    booksMenuFrame.pack_forget()
    booksHeaderFrame.pack_forget()
    
    # packs the components for editing a book
    editBookHeader.pack() 
    editBookFrame.pack()
    
    # sets up the grid for title and author entry fields
    titleEditLabel.grid(row=0, column=0, sticky="w")
    titleEdit.grid(row=1, column=0)
    authorEditLabel.grid(row=2, column=0, sticky="w")
    authorEdit.grid(row=3, column=0)
    
    # configures the submit button to trigger the processEditBook function
    submitButton.config(command=processEditBook)
    submitButton.pack(pady=10)
    
    # packs the back button to return to the books menu
    backToBooksButton.pack()

# processes the edit action for a book
def processEditBook():
    # temporary dictionary to store book details if a match is found
    tempEdit = {}

    # clears the new book details entry fields
    newTitle.delete(0, tkinter.END)
    newAuthor.delete(0, tkinter.END)
    newDatePublished.delete(0, tkinter.END)

    # retrieves and strips user input for title and author
    bookTitle = titleEdit.get().strip()
    bookAuthor = authorEdit.get().strip()
    
    # loops through book dictionary to find a match for title and author
    for key, value in books.bookDict.items():
        if (
            value[0].strip().lower() == bookTitle.lower()
            and value[1].strip().lower() == bookAuthor.lower()
        ):
            tempEdit[key] = value  # stores matched book in temporary dictionary
            bookKey = key
            status = value[3]  # retrieves the book status
            borrowerList = value[4]  # retrieves the list of borrowers
            
            # hides the title and author entry fields, and submit button
            titleEditLabel.grid_forget()
            titleEdit.grid_forget()
            authorEditLabel.grid_forget()
            authorEdit.grid_forget()
            submitButton.pack_forget()
            backToBooksButton.pack_forget()
    
    # if no book is found, show an error message
    if len(tempEdit) == 0:
        messagebox.showerror("Book Error", "No Book Found!")
        return

    # shows the new title, author, and date published fields for editing
    newTitleLabel.grid(row=0, column=0, sticky="w")
    newTitle.grid(row=1, column=0)
    newAuthorLabel.grid(row=2, column=0, sticky="w")
    newAuthor.grid(row=3, column=0)
    newDatePublishedLabel.grid(row=4, column=0, sticky="w")
    newDatePublished.grid(row=5, column=0)
    
    # packs the submit button with updated validation command
    submitButton.pack(pady=10)
    submitButton.config(command=lambda: editBookValidate(status, borrowerList, bookKey))
    
    # packs the back button to return to the books menu
    backToBooksButton.pack()

# validates and processes the edited book details
def editBookValidate(status, borrowerList, bookKey):
    # retrieves and strips user input for book title, author, and publication date
    bookTitle = newTitle.get().strip()
    bookAuthor = newAuthor.get().strip()
    datePublished = newDatePublished.get().strip()

    # checks if any required field is empty
    if not bookTitle:
        messagebox.showerror("Input Error", "Please enter a book title!")
        return
    if not bookAuthor:
        messagebox.showerror("Input Error", "Please enter a book author!")
        return
    if not datePublished:
        messagebox.showerror("Input Error", "Please enter a publication date!")
        return

    # validates the publication date format
    datePublished = validateDate(datePublished)
    if datePublished == None:
        messagebox.showerror("Date Error", "Please input valid date!")
        return

    # calls the editBook function to update the book details
    books.editBook(bookTitle, bookAuthor, datePublished, status, borrowerList, bookKey)
    
    # shows success message and clears input fields
    messagebox.showinfo("Edit Success", "Book successfully edited!")
    newTitle.delete(0, tkinter.END)
    newAuthor.delete(0, tkinter.END)
    newDatePublished.delete(0, tkinter.END)

# sets up the view pending books screen, displays all pending books
def viewPending():
    # makes the text widget editable, clears any previous data
    viewPendingText.config(state="normal")
    viewPendingText.delete("1.0", "end")

    # hides other frames and prepares the layout for pending view
    booksMenuFrame.pack_forget()
    booksHeaderFrame.pack_forget()
    booksHeader.pack_forget()

    # sets up the view pending frame and scrollbars
    viewPendingFrame.pack(pady=15)
    viewPendingText.pack(side="left")
    viewPendingScrollbar.pack(side="right", fill="y")

    # retrieves and displays the pending books info
    info = books.viewPending()
    viewPendingText.insert("1.0", info)

    # disables editing after displaying the information
    viewPendingText.config(state="disabled")

    # displays the header and back button
    viewPendingHeader.pack()
    backToBooksButton.pack()


# sets up the borrow book form, clears previous inputs
def borrowBook():
    # clears the previous user inputs
    nameLog.delete(0, tkinter.END)
    dateLog.delete(0, tkinter.END)
    timeLog.delete(0, tkinter.END)
    purposeLog.delete(0, tkinter.END)

    titleBorrow.delete(0, tkinter.END)
    authorBorrow.delete(0, tkinter.END)
    returnDate.delete(0, tkinter.END)

    # ensures the input fields are editable
    titleBorrow.config(state="normal")
    authorBorrow.config(state="normal")
    returnDate.config(state="normal")

    # adjusts the layout and hides other frames
    borrowBookHeader.pack()
    borrowHeader.pack_forget()
    borrowHeaderFrame.pack_forget()
    borrowMenuFrame.pack_forget()
    visitLibraryFrame.pack()

    # sets up labels and input fields for the user to fill in
    nameLogLabel.grid(row=0, column=0, sticky="w")
    nameLog.grid(row=1, column=0)
    dateLogLabel.grid(row=2, column=0, sticky="w")
    dateLog.grid(row=3, column=0)
    timeLogLabel.grid(row=4, column=0, sticky="w")
    timeLog.grid(row=5, column=0)
    purposeLogLabel.grid(row=6, column=0, sticky="w")
    purposeLog.grid(row=7, column=0)

    # sets the submit button to trigger the borrowing process
    submitButton.config(command=processBorrowBook)
    submitButton.pack(pady=10)
    backToBorrowButton.pack()

# processes the borrow book action, handles user info and prepares borrowing details
def processBorrowBook():
    # retrieves visit information without showing an alert, returns None if no log
    log = processVisitLibrary(showAlert=False)

    if log is not None:  # if there is a log
        name = log[0]
        userDate = log[1]
        time = log[2]
        purpose = log[3]

        # hides previous elements and sets up borrowing screen
        submitButton.pack_forget()
        backToBorrowButton.pack_forget()
        visitLibraryFrame.pack_forget()
        borrowBookFrame.pack()

        # displays the borrowing form with labels and fields
        titleBorrowLabel.grid(row=0, column=0, sticky="w")
        titleBorrow.grid(row=1, column=0, sticky="w")
        authorBorrowLabel.grid(row=2, column=0, sticky="w")
        authorBorrow.grid(row=3, column=0)
        returnDateLabel.grid(row=4, column=0, sticky="w")
        returnDate.grid(row=5, column=0)

        # sets submit button with the correct validation
        submitButton.config(command=lambda: borrowBookValidate(name, userDate, time, purpose))
        submitButton.pack(pady=10)
        backToBorrowButton.pack()

# validates user inputs for borrowing a book and processes the borrow action
def borrowBookValidate(name, userDate, time, purpose):
    # retrieves the entered information for book title, author, and return date
    bookTitle = titleBorrow.get().strip()
    bookAuthor = authorBorrow.get().strip()
    date = returnDate.get().strip()
    id = logbook.id

    logID = "L" + str(id)

    # checks if the book title is provided
    if not bookTitle:
        messagebox.showerror("No Entry", "Please enter a book title!")
        return

    # checks if the book author is provided
    if not bookAuthor:
        messagebox.showerror("No Entry", "Please enter a book author!")
        return

    # checks if the return date is provided
    if not date:
        messagebox.showerror("No Entry", "Please enter return date!")
        return

    # validates the return date
    date = validateDate(date)
    if date == None:
        messagebox.showerror("Invalid Date", "Please enter a valid date!")
        return

    # attempts to borrow the book, returns the status
    state = borrow.borrowBook(bookTitle, bookAuthor, date, logID)

    if state == None:  # no books found matching the criteria
        messagebox.showerror("No Book", "No books found!")
        return

    if state == 0:  # the book is currently unavailable
        messagebox.showerror("Book Unavailable", "Book is currently unavailable!")
        return

    if state == 1:  # book successfully borrowed
        messagebox.showinfo("Book Borrowed", "Book successfully borrowed!")

        # logs the visit to the library
        logbook.visitLibrary(name, userDate, time, purpose)

        # clears and disables input fields after borrowing
        titleBorrow.delete(0, tkinter.END)
        authorBorrow.delete(0, tkinter.END)
        returnDate.delete(0, tkinter.END)
        titleBorrow.config(state="disabled")
        authorBorrow.config(state="disabled")
        returnDate.config(state="disabled")
        submitButton.config(state="disabled")

# sets up the UI for returning a book, and prepares input fields for user interaction
def returnBook():
    # clears previous entries
    nameLog.delete(0, tkinter.END)
    dateLog.delete(0, tkinter.END)
    timeLog.delete(0, tkinter.END)
    purposeLog.delete(0, tkinter.END)

    titleReturn.delete(0, tkinter.END)
    authorReturn.delete(0, tkinter.END)

    # resets the input fields to be editable
    titleReturn.config(state="normal")
    authorReturn.config(state="normal")

    # displays the return book header and hides previous frames
    returnBookHeader.pack()
    borrowHeader.pack_forget()
    borrowHeaderFrame.pack_forget()
    borrowMenuFrame.pack_forget()
    visitLibraryFrame.pack()

    # sets up the grid layout for the log and book return inputs
    nameLogLabel.grid(row=0, column=0, sticky="w")
    nameLog.grid(row=1, column=0)
    dateLogLabel.grid(row=2, column=0, sticky="w")
    dateLog.grid(row=3, column=0)
    timeLogLabel.grid(row=4, column=0, sticky="w")
    timeLog.grid(row=5, column=0)
    purposeLogLabel.grid(row=6, column=0, sticky="w")
    purposeLog.grid(row=7, column=0)

    # configures the submit button to process the return book action
    submitButton.config(command=processReturnBook)
    submitButton.pack(pady=10)
    backToBorrowButton.pack()

# processes the return of a borrowed book
def processReturnBook():
    # retrieves library visit information
    log = processVisitLibrary(showAlert=False)
    if log is not None:
        # extracts data from the log entry
        name = log[0]
        userDate = log[1]
        time = log[2]
        purpose = log[3]

        # hides previous frames and prepares return book frame
        submitButton.pack_forget()
        backToBorrowButton.pack_forget()
        visitLibraryFrame.pack_forget()
        returnBookFrame.pack()

        # sets up the grid for book return inputs
        titleReturnLabel.grid(row=0, column=0, sticky="w")
        titleReturn.grid(row=1, column=0, sticky="w")
        authorReturnLabel.grid(row=2, column=0, sticky="w")
        authorReturn.grid(row=3, column=0)

        # configures the submit button to validate return book info
        submitButton.config(command=lambda: returnBookValidate(name, userDate, time, purpose))
        submitButton.pack(pady=10)
        backToBorrowButton.pack()

def returnBookValidate(name, userDate, time, purpose):
    bookTitle = titleReturn.get().strip()  # get the book title input and remove extra spaces
    bookAuthor = authorReturn.get().strip()  # get the book author input and remove extra spaces
    id = logbook.id  # get the logbook id for generating log ID

    logID = "L" + str(id)  # create a log ID by prefixing 'L' to the logbook ID

    # if book title is empty, show error message and return
    if not bookTitle:
        messagebox.showerror("No Entry", "Please enter a book title!")
        return

    # if book author is empty, show error message and return
    if not bookAuthor:
        messagebox.showerror("No Entry", "Please enter a book author!")
        return

    # call the returnBook method from the borrow module to check the book status
    state = borrow.returnBook(bookTitle, bookAuthor)

    # if the book is not found, show error message and return
    if state == None:
        messagebox.showerror("No Book", "No books found!")
        return

    # if the book is already available, show error message and return
    if state == 0:
        messagebox.showerror("Book Available", "Book is already available!")
        return

    # if the book is successfully returned, show success message and log the visit
    if state == 1:
        messagebox.showinfo("Book Returned", "Book successfully returned!")
        logbook.visitLibrary(name, userDate, time, purpose)  # log the library visit
        titleReturn.delete(0, tkinter.END)  # clear the title input field
        authorReturn.delete(0, tkinter.END)  # clear the author input field
        titleReturn.config(state="disabled")  # disable the title input field
        authorReturn.config(state="disabled")  # disable the author input field
        submitButton.config(state="disabled")  # disable the submit button

def viewAllBorrow():
    # enables the text widget for editing, and clears any previous text
    borrowText.config(state="normal")  
    borrowText.delete("1.0", "end")  
    allEntries = borrow.viewAll()  # retrieves all the borrow entries from the borrow module

    # hides the borrow menu frame and header as we're displaying the full list of borrowed books
    borrowMenuFrame.pack_forget()
    borrowHeaderFrame.pack_forget()
    borrowHeader.pack_forget()
    viewAllBorrowFrame.pack(pady=15)  # displays the frame with borrow entries

    borrowScrollbar.config(command=borrowText.yview)  # links the scrollbar to the text widget for vertical scrolling

    borrowText.pack(side="left")  # places the text widget on the left side of the frame
    borrowScrollbar.pack(side="right", fill="y")  # places the scrollbar on the right side, fills vertically

    borrowText.insert("1.0", allEntries)  # inserts the borrow entries into the text widget starting from the top
    borrowText.config(state="disabled")  # disables the text widget to prevent further editing
    viewAllBorrowHeader.pack()  # shows the header for the "View All Borrowed Books" section
    backToBorrowButton.pack()  # displays the button to go back to the borrow menu


def viewExpected():
    # to summarize, this part clears the preivious entries by clearing the text and the entry elements
    viewExpectedDate.delete(0, tkinter.END)
    viewExpectedText.config(state="normal")
    viewExpectedText.delete("1.0", "end")
    viewExpectedText.config(state="disabled")
    borrowMenuFrame.pack_forget()
    borrowHeaderFrame.pack_forget()
    borrowHeader.pack_forget()
    viewExpectedFrame.pack(pady=15) # displays the frame with the view expected entries

    # configures the scrollbar, links it to the text element and makes it for vertical scrolling
    viewExpectedScrollbar.config(command=viewExpectedText.yview)


    viewExpectedText.pack(side="left") # places text widget on left side of frane
    viewExpectedScrollbar.pack(side="right", fill="y") # places scrollbar on right side, fills it vertically

    viewExpectedDateLabel.pack(pady=5) # inserts label on viewExpectedDate entry
    viewExpectedDate.pack() # places the entry widget
    viewExpectedHeader.pack() # places the header image
    submitButton.config(command=processViewExpected) # links submitButton to processViewExpected
    submitButton.pack(pady=10)
    backToBorrowButton.pack()


def processViewExpected():
    viewExpectedText.config(state="normal")  # enables the text widget for editing (to show entries)
    viewExpectedText.delete("1.0", "end")  # clears any previous entries in the text widget
    
    date = viewExpectedDate.get().strip()  # retrieves the date entered by the user
    date = validateDate(date)  # validates the entered date format using the validateDate function
    
    if date == None:  # if the date is invalid, show an error message
        messagebox.showerror("Invalid Date", "Please enter a valid date!")
        return

    entries = borrow.viewExpected(date)  # retrieves borrow entries that match the specified date
    
    if entries == None:  # if no entries are found, inform the user
        messagebox.showinfo("No Returns", "There are no expected returns on the date.")
        return

    viewExpectedText.insert("1.0", entries)  # inserts the retrieved entries into the text widget
    viewExpectedText.config(state="disabled")  # disables the text widget to prevent further editing


def visitLibrary():
    # clears any previous inputs from the entry fields for new data
    nameLog.delete(0, tkinter.END)
    dateLog.delete(0, tkinter.END)
    timeLog.delete(0, tkinter.END)
    purposeLog.delete(0, tkinter.END)

    # hides previous frames and prepares the new frame for visit library data entry
    logbookMenuFrame.pack_forget()
    logbookHeaderFrame.pack_forget()
    logbookHeader.pack_forget()
    visitLibraryFrame.pack(pady=10)  # displays the visit library frame with padding

    # arranges labels and entry widgets in a grid layout for the user to input data
    nameLogLabel.grid(row=0, column=0, sticky="w")  
    nameLog.grid(row=1, column=0)  
    dateLogLabel.grid(row=2, column=0, sticky="w") 
    dateLog.grid(row=3, column=0)  
    timeLogLabel.grid(row=4, column=0, sticky="w")  
    timeLog.grid(row=5, column=0)  
    purposeLogLabel.grid(row=6, column=0, sticky="w") 
    purposeLog.grid(row=7, column=0)  

    # configures the submit button to call the processVisitLibrary function when clicked
    submitButton.config(command=processVisitLibrary)

    # displays the header and places the submit and back buttons
    visitLibraryHeader.pack()
    submitButton.pack(pady=10)
    backToLogbookButton.pack()

def processVisitLibrary(showAlert=True):
    # defines the possible purposes for visiting the library
    purpose = ["Borrow", "Return", "Visit"]
    
    # retrieves input data from the entry fields and removes leading/trailing spaces
    name = nameLog.get().strip()
    date = dateLog.get().strip()
    time = timeLog.get().strip()
    purposeUser = purposeLog.get().strip().capitalize()

    # checks if the user has entered a name, shows an error if not
    if not name:
        messagebox.showerror("No Entry", "Please enter your name!")
        return
    # checks if the user has entered a date, shows an error if not
    if not date:
        messagebox.showerror("No Entry", "Please enter the date today!")
        return
    # checks if the user has entered a time, shows an error if not
    if not time:
        messagebox.showerror("No Entry", "Please enter the current time!")
        return
    # checks if the user has entered a purpose, shows an error if not
    if not purposeUser:
        messagebox.showerror("No Entry", "Please enter a purpose!")
        return

    # validates the date input, shows an error if invalid
    date = validateDate(date)
    if date == None:
        messagebox.showerror("Invalid Date", "Please enter a valid date!")
        return
    # validates the time input, shows an error if invalid
    time = validateTime(time)
    if time == None:
        messagebox.showerror("Invalid Time", "Please enter a valid time!")
        return

    # checks if the entered purpose is valid, shows an error if not
    if purposeUser not in purpose:
        messagebox.showerror("Invalid Purpose", "Please enter a valid purpose!")
        return

    # stores the validated information for logging
    information = [name, date, time, purposeUser]

    # shows a success message and logs the visit if showAlert is True
    if showAlert == True:
        messagebox.showinfo("Success", "Information logged successfully!")
        logbook.visitLibrary(name, date, time, purposeUser)

    # clears the input fields after successful logging
    nameLog.delete(0, tkinter.END)
    dateLog.delete(0, tkinter.END)
    timeLog.delete(0, tkinter.END)
    purposeLog.delete(0, tkinter.END)
    
    return information

def viewAllLogbook():
    # enables the text widget for editing, and clears any previous text
    logbookText.config(state="normal")  
    logbookText.delete("1.0", "end")  
    
    # retrieves all the logbook entries from the logbook module
    allEntries = logbook.viewAll()  
    
    # hides the logbook menu frame and header as we're displaying the full list of logbook entries
    logbookMenuFrame.pack_forget()
    logbookHeaderFrame.pack_forget()
    logbookHeader.pack_forget()
    
    # displays the frame with logbook entries
    viewAllLogbookFrame.pack(pady=15)

    # links the scrollbar to the text widget for vertical scrolling
    logbookScrollbar.config(command=logbookText.yview)

    # places the text widget on the left side of the frame
    logbookText.pack(side="left")  
    
    # places the scrollbar on the right side, fills vertically
    logbookScrollbar.pack(side="right", fill="y")

    # inserts the logbook entries into the text widget starting from the top
    logbookText.insert("1.0", allEntries)  
    
    # disables the text widget to prevent further editing
    logbookText.config(state="disabled")  
    
    # shows the header for the "View All Logbook Entries" section
    viewAllLogbookHeader.pack(pady=0)
    
    # displays the button to go back to the logbook menu
    backToLogbookButton.pack()



def viewPerDay():
    # clears the previous entries by deleting the contents of the entry and text widgets
    viewDate.delete(0, tkinter.END)
    viewPerDayText.config(state="normal")  # enables the text widget for editing
    viewPerDayText.delete("1.0", "end")  # clears any previous entries in the text widget
    viewPerDayText.config(state="disabled")  # disables the text widget after clearing

    # removes previous frames
    logbookMenuFrame.pack_forget()  
    logbookHeaderFrame.pack_forget()  
    logbookHeader.pack_forget()  
    viewPerDayFrame.pack(pady=15)  # displays the frame for viewing per-day entries

    # configures the scrollbar, linking it to the text widget for vertical scrolling
    viewPerDayScrollbar.config(command=viewPerDayText.yview)

    viewPerDayText.pack(side="left")  # places the text widget on the left side of the frame
    viewPerDayScrollbar.pack(side="right", fill="y")  # places the scrollbar on the right side, fills it vertically

    viewDateLabel.pack(pady=5)  # inserts the label for the viewDate entry
    viewDate.pack()  # places the viewDate entry widget
    viewPerDayHeader.pack()  # places the header image for this view
    submitButton.config(command=processViewPerDay)  # links the submit button to the processViewPerDay function
    submitButton.pack(pady=10)  
    backToLogbookButton.pack()  

def processViewPerDay():
    # enables the text widget for editing to display new entries
    viewPerDayText.config(state="normal")
    viewPerDayText.delete("1.0", "end")  # clears any previous entries in the text widget
    
    date = viewDate.get().strip()  # gets the date input from the user and strips any extra spaces
    date = validateDate(date)  # validates the entered date
    
    if date == None:  # checks if the entered date is invalid
        messagebox.showerror("Invalid Date", "Please enter a valid date!")  # shows error message for invalid date
        return
    
    entries = logbook.viewPerDay(date)  # fetches the logbook entries for the given date
    
    if entries == None:  # checks if there are no entries for the specified date
        messagebox.showinfo("No Entry", "There are no entries on the date.")  # shows message when no entries are found
        return
    
    viewPerDayText.insert("1.0", entries)  # inserts the fetched entries into the text widget
    viewPerDayText.config(state="disabled")  # disables the text widget to prevent further editing


# this button style is basically a format for the tkinter.Buttons elements, when you put **buttonStyle as attribute, it basically unpacks all that is on here and sets it as the style/formatting
buttonStyle = {
    "width": 32,
    "height": 1,
    "font": ("Arial", 12, "bold"),
    "borderwidth": 4,  # border thickness
    "relief": "solid",  # border style (raised, sunken, solid, etc.)
    "bg": "#FFFDD0",  # background color
    "fg": "black",  # text color
    "pady": 5,
}

# everything under this part of the code defines the labels, entry fields, text areas, and scrollbars for the books, borrow, and logbook modules. 
# it includes labels for user inputs, entry fields for data, text areas for displaying content, and scrollbars for navigation.

booksButton = tkinter.Button(mainMenuFrame, text="Books Module", **buttonStyle, command=booksMenu)
borrowButton = tkinter.Button(mainMenuFrame, text="Borrow Module", **buttonStyle, command=borrowMenu)
logbookButton = tkinter.Button(mainMenuFrame, text="Logbook Module", **buttonStyle, command=logbookMenu)
exitButton = tkinter.Button(mainMenuFrame, text="Exit", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=exit)

addBookButton = tkinter.Button(booksMenuFrame, text="Add Book", **buttonStyle, command=addBook)

# Everything under this comment is for the addBook function
titleAddLabel = tkinter.Label(addBookFrame, text="Enter book title:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleAdd = tkinter.Entry(addBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

authorAddLabel = tkinter.Label(addBookFrame, text="Enter book author:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorAdd = tkinter.Entry(addBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

datePublishedAddLabel =  tkinter.Label(addBookFrame, text="Enter date published (ex. 1 Jan 2000):", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
datePublishedAdd = tkinter.Entry(addBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
submitButton = tkinter.Button(library, text="Submit", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#C1E1C1", fg="black", pady=5)

# Everything under this comment is for the viewBook function

viewBookButton = tkinter.Button(booksMenuFrame, text="View Book", **buttonStyle, command=viewBook)

titleViewLabel = tkinter.Label(viewBookFrame, text ="Enter book title to view:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleView = tkinter.Entry(viewBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
authorViewLabel = tkinter.Label(viewBookFrame, text ="Enter book author to view:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorView = tkinter.Entry(viewBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
viewBookScrollbar = tkinter.Scrollbar(bookDetailsFrame)
bookDetailsText = tkinter.Text(bookDetailsFrame, wrap="word", yscrollcommand=viewBookScrollbar, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=6, bg="#FFFDD0")

# Everything under this comment is for the deleteBook function

deleteBookButton = tkinter.Button(booksMenuFrame, text="Delete Book", **buttonStyle, command=deleteBook)
titleDeleteLabel = tkinter.Label(deleteBookFrame, text="Enter book title you want to delete:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleDelete = tkinter.Entry(deleteBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
authorDeleteLabel = tkinter.Label(deleteBookFrame, text="Enter book author you want to delete:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorDelete = tkinter.Entry(deleteBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

# Everything under this comment is for the deleteAll function

deleteAllButton = tkinter.Button(booksMenuFrame, text="Delete All Books", **buttonStyle, command=deleteAll)

# Everything under this comment is for the editBook function

editBookButton = tkinter.Button(booksMenuFrame, text="Edit Book", **buttonStyle, command=editBook)
titleEditLabel = tkinter.Label(editBookFrame, text="Enter book title you want to edit:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleEdit = tkinter.Entry(editBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
authorEditLabel = tkinter.Label(editBookFrame, text="Enter book author you want to edit:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorEdit = tkinter.Entry(editBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
newTitleLabel = tkinter.Label(editBookFrame, text="Enter new book title:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
newTitle = tkinter.Entry(editBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
newAuthorLabel = tkinter.Label(editBookFrame, text="Enter new book author:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
newAuthor = tkinter.Entry(editBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
newDatePublishedLabel = tkinter.Label(editBookFrame, text="Enter new date published:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
newDatePublished = tkinter.Entry(editBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

# Everything under this comment is for the viewPending function

viewPendingButton = tkinter.Button(booksMenuFrame, text="View Pending", **buttonStyle, command=viewPending)
viewPendingScrollbar = tkinter.Scrollbar(viewPendingFrame)
viewPendingText = tkinter.Text(viewPendingFrame, wrap="word", yscrollcommand=viewPendingScrollbar.set, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=10, bg="#FFFDD0")

returnMainButtonBooks = tkinter.Button(booksMenuFrame, text="Back to Main Menu", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=mainMenu)

# Everything under this comment is for the buttons to go back to menus
backToBooksButton = tkinter.Button(library, text="Back to Books Module", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=booksMenu)
backToBorrowButton = tkinter.Button(library, text="Back to Borrow Module", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=borrowMenu)
backToLogbookButton = tkinter.Button(library, text="Back to Logbook Module", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=logbookMenu)

# Everything under this comment is for the borrowBook function

borrowBookButton = tkinter.Button(borrowMenuFrame, text="Borrow Book", **buttonStyle, command=borrowBook)
titleBorrowLabel = tkinter.Label(borrowBookFrame, text="Enter book title to borrow:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleBorrow = tkinter.Entry(borrowBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
authorBorrowLabel = tkinter.Label(borrowBookFrame, text="Enter author of the book:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorBorrow = tkinter.Entry(borrowBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
returnDateLabel = tkinter.Label(borrowBookFrame, text="Enter return date (ex. 1 Jan 2000):", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
returnDate = tkinter.Entry(borrowBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

# Everything under this comment is for the returnBook function

returnBookButton = tkinter.Button(borrowMenuFrame, text="Return Book", **buttonStyle, command=returnBook)
titleReturnLabel = tkinter.Label(returnBookFrame, text="Enter book title to return:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
titleReturn = tkinter.Entry(returnBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")
authorReturnLabel = tkinter.Label(returnBookFrame, text="Enter book author to return:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
authorReturn = tkinter.Entry(returnBookFrame, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")

# Everything under this comment is for the viewAllBorrow function

viewAllBorrowButton = tkinter.Button(borrowMenuFrame, text="View All Entries", **buttonStyle, command=viewAllBorrow)
borrowScrollbar = tkinter.Scrollbar(viewAllBorrowFrame)
borrowText = tkinter.Text(viewAllBorrowFrame, wrap="word", yscrollcommand=borrowScrollbar.set, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=10, bg="#FFFDD0")

# Everything under this comment is for the viewExpected function

viewExpectedButton = tkinter.Button(borrowMenuFrame, text="View Expected Entries", **buttonStyle, command=viewExpected)
viewExpectedScrollbar = tkinter.Scrollbar(viewExpectedFrame)
viewExpectedText = tkinter.Text(viewExpectedFrame, wrap="word", yscrollcommand=viewExpectedScrollbar.set, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=6, bg="#FFFDD0")
viewExpectedDateLabel = tkinter.Label(library, text="Enter date to view expected returns: ", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
viewExpectedDate = tkinter.Entry(library, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")


returnMainButtonBorrow = tkinter.Button(borrowMenuFrame, text="Back to Main Menu", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=mainMenu)

# Everything under this comment is for the visitLibrary function

visitLibraryButton = tkinter.Button(logbookMenuFrame, text="Visit Library", **buttonStyle, command=visitLibrary)
nameLogLabel = tkinter.Label(visitLibraryFrame, text="Enter name:", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
nameLog = tkinter.Entry(visitLibraryFrame, width=40, font=("Arial", 16, "italic"), border=4, relief="solid", bg = "#FFFDD0")
dateLogLabel = tkinter.Label(visitLibraryFrame, text="Enter date (ex. 1 Jan 2000):", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
dateLog = tkinter.Entry(visitLibraryFrame, width=40, font=("Arial", 16, "italic"), border=4, relief="solid", bg = "#FFFDD0")
timeLogLabel = tkinter.Label(visitLibraryFrame, text="Enter time (ex. 10:00 AM):", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
timeLog = tkinter.Entry(visitLibraryFrame, width=40, font=("Arial", 16, "italic"), border=4, relief="solid", bg = "#FFFDD0")
purposeLogLabel = tkinter.Label(visitLibraryFrame, text="Enter purpose (ex. Visit/Borrow/Return):", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
purposeLog = tkinter.Entry(visitLibraryFrame, width=40, font=("Arial", 16, "italic"), border=4, relief="solid", bg = "#FFFDD0")

# Everything under this comment is for the viewAllLogbook function

viewAllLogbookButton = tkinter.Button(logbookMenuFrame, text="View All Entries", **buttonStyle, command=viewAllLogbook)
logbookScrollbar = tkinter.Scrollbar(viewAllLogbookFrame)
logbookText = tkinter.Text(viewAllLogbookFrame, wrap="word", yscrollcommand=logbookScrollbar.set, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=10, bg="#FFFDD0")

# Everything under this comment is for the viewPerDay function

viewPerDayButton = tkinter.Button(logbookMenuFrame, text="View Transactions Per Day", **buttonStyle, command=viewPerDay)
viewPerDayScrollbar = tkinter.Scrollbar(viewPerDayFrame)
viewPerDayText = tkinter.Text(viewPerDayFrame, wrap="word", yscrollcommand=logbookScrollbar.set, font=("Arial", 16, "bold", "italic"), fg="black", width=35,height=6, bg="#FFFDD0")
viewDateLabel = tkinter.Label(library, text="Enter date to view: ", font=("Arial", 14, "italic", "bold"), bg="#393131", fg="white")
viewDate = tkinter.Entry(library, width=40, font=("Arial", 18, "italic"), border=4, relief="solid", bg = "#FFFDD0")


returnMainButtonLogbook = tkinter.Button(logbookMenuFrame, text="Back to Main Menu", width=32, height=1, font=("Arial", 12, "bold"), borderwidth=4, relief="solid", bg="#FF746c", fg="black", pady=5, command=mainMenu)

# this function validates the date inputted by the user
def validateDate(date):
    # list of valid month names
    validMonths = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    ]
    # months that have 31 days
    monthsWith31 = [
        "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec",
    ]
    
    format = date.split()  # splits the date into day, month, and year components

    # if the format doesn't have exactly three parts, return
    if len(format) != 3:
        return

    # if the day is not a number, return
    if not format[0].isdigit() or not format[2].isdigit():
        return

    day = int(format[0])  # convert the day to an integer
    # if the day starts with a zero, return
    if format[0].startswith("0"):
        return

    # if the day is not between 1 and 31, return
    if day < 1 or day > 31:
        return

    # check if the month is valid
    if format[1].capitalize() not in validMonths:
        return
    # if the month has 31 days but the day is greater than 31, return
    if format[1].capitalize() in validMonths and format[1].capitalize() not in monthsWith31 and day > 30:
        return
    
    # if the month is February and the day is greater than 29, return
    if format[1].capitalize() == "Feb" and day > 29:
        return
    
    # check for leap year and ensure February doesn't have more than 28 or 29 days
    if int(format[2]) % 4 != 0 and format[1].capitalize() == "Feb" and day > 28:
        return
    if int(format[2]) % 100 == 0 and int(format[2]) % 400 != 0 and format[1].capitalize() == "Feb" and day > 28:
        return

    # ensure the year is a valid 4-digit number
    if not format[2].isdigit():
        return
    elif int(format[2]) > 9999 or int(format[2]) < 1:
        return

    # rebuild the date string in the correct format
    date = f"{day} {format[1].capitalize()} {format[2]}"

    return date


# this function validates the time inputted by the user
def validateTime(time):
    temp = time.split()  # splits the input time into time and period (AM/PM)

    # if the format does not have exactly two parts, return
    if len(temp) != 2:
        return

    try:
        time = temp[0]  # extract the time part
        period = temp[1]  # extract the period (AM/PM)
        digits = time.split(":")  # split the time into hour and minute
        hour = digits[0]
        minute = digits[1]
    except:
        return  # if there's an error in splitting, return

    # if hour or minute is not a digit, return
    if not hour.isdigit() or not minute.isdigit():
        return

    # if period is not AM or PM, return
    if period.lower().strip() not in ["am", "pm"]:
        return

    # if hour is not between 1 and 12, return
    if int(hour) > 12 or int(hour) < 1:
        return

    # if minute is not between 0 and 59, return
    if int(minute) > 59 or int(minute) < 0:
        return

    # if minute is less than or equal to 9 and period is AM, format the time correctly
    if int(minute) <= 9 and period.lower().strip() == "am":
        validatedTime = f"{hour}:0{int(minute)} AM"
        return validatedTime
    
    # if minute is greater than 9 and period is AM, format the time correctly
    if int(minute) > 9 and period.lower().strip() == "am":
        validatedTime = f"{hour}:{minute} AM"
        return validatedTime

    # if minute is less than or equal to 9 and period is PM, format the time correctly
    if int(minute) <= 9 and period.lower().strip() == "pm":
        validatedTime = f"{hour}:0{int(minute)} PM"
        return validatedTime
    
    # if minute is greater than 9 and period is PM, format the time correctly
    if int(minute) > 9 and period.lower().strip() == "pm":
        validatedTime = f"{hour}:{minute} PM"
        return validatedTime


mainMenu()
library.configure(bg="#393131")
library.mainloop()

# All the headers used in this project were designed using Canva. Any use of templates, icons, or elements from Canva is properly attributed to the platform. 
# These designs are intended for academic purposes only and are specifically created for this project.