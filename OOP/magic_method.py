# Magic Method => Biasa diawali double underscore __init__, __str__

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "J.K Rowling", 223)
book3 = Book("The Lion", "C.S Lewis", 172)

print(book1)
print("Lion" in book3) # True => Lion adalah Title di book 3
print(book1["author"])
print(book2["title"])
print(book3["num_pages"])