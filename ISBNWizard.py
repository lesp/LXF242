import isbnlib
from guizero import App, Text, PushButton, TextBox
import webbrowser
global ISBN13
global book

def update_details():
    global book
    #ID = book.value
    print(book)

def scanbook():
    global book
    scanner = App()
    input_box = TextBox(scanner)
    input_box.focus()
    info = Text(scanner, text="Scan or type the ISBN 13 digit code to search", enabled=True)
    update = PushButton(scanner, command=update_details, text="Click here to run")
    book = info.value
    scanner.display()
    

def openAmazon():
    global ISBN13
    URL = "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
    webbrowser.open_new_tab(URL+ISBN13)

def bookfinder(ISBN):
    global book
    global ISBN13
    #isbn = "1491953403"
    book_meta = isbnlib.meta(ISBN)
    description = isbnlib.desc(ISBN)
    print(description)
    #print(book_meta)
    title = book_meta["Title"]
    author = book_meta["Authors"][0]
    year = book_meta["Year"]
    ISBN13 = book_meta["ISBN-13"]
    app = App(title=title, layout="grid")
    Publication_Title = Text(app, text="Book Title: "+title, grid=[0,0], align="left")
    Author_Details = Text(app, text="Author(s): "+author, grid=[0,1], align="left")
    Publication_Year = Text(app, text="Year of publication: "+year, grid=[0,2], align="left")
    ISBN13Data = Text(app, text="ISBN-13: "+ISBN13, grid=[0,3], align="left")
    Description = Text(app, text="Description: "+description, grid=[0,4,1,4], align="left")
    Visit_Amazon = PushButton(app, text="Visit Amazon", command=openAmazon,grid=[0,6], align="left")
    app.display()

