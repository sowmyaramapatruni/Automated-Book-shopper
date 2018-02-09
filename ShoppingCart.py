"""
Class ShoppingCart: This class provides cart data structure
                    to hold the books that are selected for purcahse.

This also provides interfaces for other programs to add/remove/view 
bokks that are added to the cart. This cart is designed to suit the 
shoping cart interface of a popular shoping website.

Author: Vijaya Ram Illa
        Shaunak Mukherjee
"""
import Book

class ShoppingCart:
    def __init__(self):
        self.cart = []
        pass

    #check if the book is present in the cart
    def hasCart(self, book):
        url =  book.getURL()
        for i in range(len(self.cart)) :
            if url == self.cart[i].get():
                return i
        return -1

    # Increment the quantity of the book in the cart
    def incrementQuantity(self, book):
        index = self.hasCart(book)
        if index == -1 :
            print "Book Not present in cart!"
        else :
            book.incrementQuantity()
            
    # Add book to the cart
    def add(self, book):
        index = self.hasCart(book)
        if index == -1 :
            self.cart.append(book)
        else:
            book.incrementQuantity()

    # return a particular book dictionary
    def get(self, index):
        return self.cart[index]

    # Added to give the total number of books in the cart
    def getCartNumber(self):
        return len(self.cart) + 1

    # Display the details of the books in the cart.
    def displayCart(self):

        for i in range(len(self.cart)):
            print "Book: ", i+1
            print "\nBook Title = ", self.cart[i].getTitle()
            print "\nAuthor = ", self.cart[i].getAuthor()
            print "\nQuantity = ", self.cart[i].getQuantity()

    #remove a given book from the cart
    def removeFromCart(self, book):
        index = self.hasCart(book)
        if index == -1 :
            print "Nothing to remove"
            return
        else:
            #rearrange the cart to remove the selected item 
            self.cart.pop(index)

    #change the quantity of a book in the cart
    def changeExistingQuantity(self, book, newQuantity) :
        index = self.hasCart(book)
        if index == -1 :
            print "No matching book in the cart"
            return
        else :
            self.cart[index].incrementQuality()

        
