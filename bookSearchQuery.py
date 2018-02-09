import requests
from bs4 import BeautifulSoup as bs
import re
from Book import Book
import ShoppingCart

# Base function to create a query and send it to 
# webserver. Modify this later to include this as
# seperate python file.
def bookSearch(url) :
    content = requests.get(url).text
    soup = bs(content, "lxml")

    bookList = []
    allDivs = soup.findAll('div',attrs={'class':'product-info'})

    for div in allDivs:
        #extract the authorname
        bookInfo = {}
        lists = div.find_all(True, {"class" : "contributors"})[0]
        author = lists.contents[1].string
        #bookInfo["author"] = author

        product_list = div.find_all(True, {"class" : "product-info-title"})[0]
        title = product_list.contents[1].string
        #bookInfo["title"] = title

        links = product_list.findAll('a')
        for a in links:
            #copy to the book_info
            url = a['href']
        #url = url.split(";")[0]
        bookInfo["url"] = url
        bookInfo = Book(author, title, url)
        bookList.append(bookInfo)
    return bookList
