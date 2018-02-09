"""
BookShopper.py: Main Shopper program to start the search and cart transactions
Authors: Vijaya Ram Illa
         Shaunak Mukherjee
"""
import re
import sys
import requests
import lxml.html
import HTMLParser
from bs4 import BeautifulSoup as bs
from bookSearchQuery import bookSearch
from Book import Book
from ShoppingCart import ShoppingCart

def shopper(book_name) :
    bookname = book_name.lower()
    bookName = '+'.join(bookname.split())
    url = 'http://www.barnesandnoble.com/s/' + bookName + '?_requestid=*'
    bookList = bookSearch(url)

    # call the print function
    displayResults(bookList)  # ask user to select a book 
    bookNo = input("\n\nSelect the book number to checkout or press enter exit to main menu: ") 
    if option == "" :
        return
    else :
		addToCart(bookList, bookNo)
    
# function given to search according to author name

def author_search(author_name) :
    authorname = author_name.lower()
    authorName = '+'.join(authorname.split())
    url =  'http://www.barnesandnoble.com/s/' + authorName + '?_requestid=*'
    authorList = bookSearch(url)

    #call the print function
    displayResults(authorList) # ask user to select a book   
    bookNo = input("\n\nSelect the book number to checkout or press enter exit to main menu: ") 
    if option == "" :
        return
    else :
		addToCart(authorList, bookNo)

# helper function to convert HTML entities to Unicode
def convert(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text

def displayResults(bookList) : 

    print " ============================================================"
    print " ***************** LIST OF RETRIVED BOOKS   *****************"
    print " ============================================================"
    

    print " NUMBER" ," " * 5,"BOOK NAME"," " * 40, "AUTHOR"
    print "","-" * 60
    for i in range(len(bookList)):
        #print i+1 ," " * 5,bookList[i]["title"]," " * 20,bookList[i]["author"]
		print i+1 ," " * 5,bookList[i].getTitle()," " * 20,bookList[i].getAuthor()
    

# helper function to try and extract contents out of soup

def selectedBookDetails(newURL) :
    content = requests.get(newURL).text
    soup = bs(content, "lxml")
    # get book review:
    allDivs = soup.find('div',attrs={'class':'flexColumn'})
    #print allDivs
    
    links = allDivs.findAll('p')
    review = ""
    for link in links:
        if not link.empty:
            review += str(link.string)
    
    temp_price = soup.find(True, {"class" : "price current-price"})
    currentPrice =  temp_price.contents[0]
    discounts = soup.find(True, {"class" : "discount-amount"})
    discount = 0
    if discounts is not None :
        discount = discounts.contents[0]

    print "===================================================================="
    print "Review of the book -->\n", review
    print "\nCURRENT PRICE --> ", currentPrice
    print "\nDiscount is  --> ", discount
    print "===================================================================="

# function to show reviews and prices for reference

def addToCart (bookList, bookNo) :

    print "\n\nSelected Book: ", bookList[bookNo - 1].getTitle(), " by ", bookList[bookNo - 1].getAuthor()
    newURL = 'http://www.barnesandnoble.com' + bookList[bookNo - 1].getURL()
   
    selectedBookDetails(newURL)

    proceed = raw_input("Add the book to the shopping bag?(y/n):  ")
    if proceed == 'y' :
        #add to cart
        cart.add(bookList[bookNo - 1])

    showCart = raw_input("Do you want to check the cart content?(y/n): ")
    if showCart == 'y':
        # DisplayCart
        print "total items in the cart = ", cart.getCartNumber()
        print "================================================================"
        print "=========================CART DETAILS==========================="
        print "================================================================"
        cart.displayCart()

    
    choice_shipping = input("\n\nContinue to billing?\n\n 1 for YES, 0 for NO!\n\n")
    if choice_shipping == 0 :
        pass
    else :
        shipping(bookList, bookNo)

# method to start and end shipping process

def shipping(bookList, bookNo) :

    lines = [] # to display the lines
    with open("userdata.txt") as f :
        content = f.readlines()
    content = [x.strip() for x in content]
    fname = content[0]
    lname = content[1]
    address = content[2]
    suite = content[3]
    city = content[4]
    state = content[5]
    zip = content[6]
    phone = content[7]
    company = content[8]

    print "\n\n(Now reading data from file given)\n\n"
    print "\n\n=========================BILLING DETAILS==========================\n"
    print "First Name = ",fname,"\nLast Name = ", lname,"\nAddress = ",address,"\nCity = ", city, "\nState = ", state, "\nZIP = ",zip,"\nPhone Number = ",phone, "\nCompany Name = ",company
    print "ORDER DETAILS = \nBook Name : ", bookList[bookNo - 1]["title"],"\nAuthor = ", bookList[bookNo - 1]["author"]
    print "\n\n==================================================================\n"
    choice_final = input("\n\nDo you want to checkout? Press 1 for checking out and 0 if you want to go back and change any details!\n\n")
    if choice_final == 1 :
        print "\n\n=======================SUCCESS!!=====================\n\n Your Order has been successfully placed ! \nThank you so much for using our Shopping Bot !\n\n"
        print "\n\n(C) Shaunak Mukherjee and Vijayaram Illa, 2017.\n\n"
    sys.exit()



def welcomeMenu() :
    print " ======================================================================\n"
    print " ************ Welcome to the 600.466 Automatic BookShopper ************\n" 
    print " ======================================================================\n"
    print "1. Search books by the Book Name"
    print "2. Search books by the Author Name"
    print "3. Get the details (price / review) of a book"
    print "4. Exit"

loop=True

while loop:
    #create cart
    cart = ShoppingCart()

    welcomeMenu()
    option = input("Enter choice: ")
    if option == 1 :
        print "Enter the name of the book you wish to buy: "
        bookName = raw_input()
        print "\n\nYou're currently searching for books named : ", bookName
        shopper(bookName)
    if option == 2 :
        print "Enter the name of the author whose book you wish to buy: "
        authorName = raw_input()
        print "\n\nYou're currently searching for books authored by : ", authorName
        author_search(authorName)
    if option == 4 :
        sys.exit()
