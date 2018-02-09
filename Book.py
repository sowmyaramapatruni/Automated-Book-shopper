"""
Book.py: This provides a book class to stire the details of the books.
        These objects are used at several instances of the shopping
        program.

Author: Vijaya Ram Illa
        Shaunak Mukherjee
"""

class Book :
    def __init__(self, author, title, url):
        self.bookInfo = {}
        self.bookInfo["author"] = author
        self.bookInfo["title"] = title
        self.bookInfo["url"] = url
        self.bookInfo["quantity"] = 1
        pass

    # auxiliary function added so that the __init__ works properly

    def __getitem__(self, item):
        return self.bookInfo[item]
    
    def getTitle(self) :
        return self.bookInfo["title"]

    def getAuthor(self) :
        return self.bookInfo["author"]

    def getURL(self) :
        return self.bookInfo["url"]
    
    def getQuantity(self) :
        return self.bookInfo["quantity"]

    def incrementQuantity() :
        self.bookInfo["quantity"] += 1



