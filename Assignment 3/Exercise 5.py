import os
os.system('cls')

class Book:
    def __init__(self, title=str,author=str, price=float ):
        self.title= title
        self.author= author
        self.price = price
    def View(self):
        print(f'Book title: {self.title}')
        print(f'Book author: {self.author}')
        print(f'Book price: {self.price}')
    
def bookTask():
    n= int(input("Enter value n: "))
    bookArray= []
    for i in range (n):
        title = str(input('Enter title book:'))
        author= str(input('Enter author book: '))
        price = float(input('Enter price book: '))
        bookArray.append(Book(title,author,price))

        min_price= bookArray[0].price
        min_price_name= bookArray[0]
    for i in bookArray:
        if min_price > i.price:
            min_price= i.price
            min_price_name= i
    print (f"The book have min price: {min_price_name.title}")
    for i in range(n-1):
        for j in range(i+1,n):
            if bookArray[i].price < bookArray[j].price:
                temp= bookArray[i]
                bookArray[i]=bookArray[j]
                bookArray[j]= temp
        print ("Book price decrease : ")
        for i in bookArray:
            print(i.title)

if __name__ == '__main__':
    bookTask()