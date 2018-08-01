import isbnlib
from guizero import App, Text, PushButton, TextBox, Window, Picture
import webbrowser
global ISBN13
global app

def update_details():
    global ISBN13
    book = input_box.value
    book_meta = isbnlib.meta(book)
    description = isbnlib.desc(book)
    title = book_meta["Title"]
    author = book_meta["Authors"][0]
    year = book_meta["Year"]
    ISBN13 = book_meta["ISBN-13"]
    details = Window(app,title=title+" "+author, width=700, layout="grid")
    Publication_Title = Text(details, text="Book Title: "+title, grid=[0,1], align="left")
    Author_Details = Text(details, text="Author(s): "+author, grid=[0,2], align="left")
    Publication_Year = Text(details, text="Year of publication: "+year, grid=[0,3], align="left")
    ISBN13Data = Text(details, text="ISBN-13: "+ISBN13, grid=[0,4], align="left")
    Description = Text(details, text="Description: "+description, grid=[0,5], align="left")
    Visit_Amazon = PushButton(details, text="Visit Amazon", command=openAmazon,grid=[0,8], align="left")
    return ISBN13

def clear_input():
    input_box.value = ""
    input_box.focus()

def openAmazon():
    global ISBN13
    URL = "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
    webbrowser.open_new_tab(URL+ISBN13)
    
app = App(title="Book Scanner", layout="grid", width=700, height=100, bg = (255,0,0))

info = Text(app, text="Scan or type the ISBN 13 digit code to search", enabled=True, grid =[0,0])
input_box = TextBox(app, grid=[1,0], width=15)
input_box.focus()
update = PushButton(app, command=update_details, text="Click here to search", grid=[2,0], align="left")
clear = PushButton(app, command=clear_input, text="Click to clear", grid=[2,1], align="left")
app.display()
