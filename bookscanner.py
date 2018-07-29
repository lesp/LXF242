import isbnlib
from guizero import App, Text, PushButton, TextBox
import webbrowser
global ISBN13

def update_details():
    global ISBN13
    book = input_box.value
    book_meta = isbnlib.meta(book)
    description = isbnlib.desc(book)
    print(description)
    print(book)
    title = book_meta["Title"]
    author = book_meta["Authors"][0]
    year = book_meta["Year"]
    ISBN13 = book_meta["ISBN-13"]
    Publication_Title = Text(app, text="Book Title: "+title, grid=[0,1], align="left")
    Author_Details = Text(app, text="Author(s): "+author, grid=[0,2], align="left")
    Publication_Year = Text(app, text="Year of publication: "+year, grid=[0,3], align="left")
    ISBN13Data = Text(app, text="ISBN-13: "+ISBN13, grid=[0,4], align="left")
    Description = Text(app, text="Description: "+description, grid=[0,5,1,5], align="left")
    Visit_Amazon = PushButton(app, text="Visit Amazon", command=openAmazon,grid=[0,8], align="left")
    return ISBN13

def openAmazon():
    global ISBN13
    URL = "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
    webbrowser.open_new_tab(URL+ISBN13)
    
app = App(title="Book Scanner", layout="grid", width=700)

info = Text(app, text="Scan or type the ISBN 13 digit code to search", enabled=True, grid =[0,0])
input_box = TextBox(app, grid=[1,0])
input_box.focus()
update = PushButton(app, command=update_details, text="Click here to search", grid=[2,0])

app.display()
