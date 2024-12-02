#!/usr/bin/env python
# coding: utf-8

# In[1]:


library = []

borrowed_books = ()

# Adding a book

def add_book():
    title = input("Enter book title:")
    author = input("Enter author name:")
    genre = input("Enter book genre:")
    publication_year = input("Enter the publication year:")
    book = f"{title} by {author}"
    if book not in library:
        library.append(book)
        print(f"{title} has been added to the collection")
    else:
        print(f"{title} is already in the collection")


# In[2]:


# search for books

def search_book():
    keyword = input("Enter a keyword to search for a book:")
    books_found = [book for book in library if keyword.lower() in book.lower()]
    if books_found:
        print("Book found:")
        for book in books_found:
            print(book)
    else:
        print("Book not found!")


# In[3]:


# remove the book

def remove_book():
    title = input("Enter the exact title of the book to remove: ")
    book_to_remove = next((book for book in library if title.lower() in book.lower()), None)
    if book_to_remove:
        library.remove(book_to_remove)
        print(f"'{title}' has been removed from the collection.")
    else:
        print(f"'{title}' not found in the collection.")
    


# In[4]:


# display unique authors

def display_unique_authors():
    authors = {book.split('by')[1] for book in library}
    if authors:
        print("Unique Authors:")
        for author in authors:
            print(author)
    else:
        print("author not found!")
        


# In[5]:


# sort books by title
def sort_books():
    library.sort()  
    print("Books sorted by title:")
    for book in library:
        print(book)


# In[6]:


# borrow books

def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    borrower = input("Enter the borrower's name: ")
    book_to_borrow = next((book for book in library if title.lower() in book.lower()), None)
    if book_to_borrow:
        global borrowed_books
        borrowed_books += ((book_to_borrow, borrower),)
        print(f"'{title}' has been borrowed by {borrower}.")
    else:
        print(f"'{title}' is not available in the collection.")


# In[7]:


# show borrowed books

def display_borrowed_books():
    if borrowed_books:
        print("Borrowed Books:")
        for book, borrower in borrowed_books:
            print(f"{book} is borrowed by {borrower}")
    else:
        print(f"No books are currently borrowed")
        


# In[10]:


# creating a main menu for all the function

def menu():
    while True:
        print("\nLibrary Book Tracker")
        print("1. Add a new book")
        print("2. Search for books")
        print("3. Remove a book")
        print("4. Display unique authors")
        print("5. Display books sorted by title")
        print("6. Borrow a book")
        print("7. Show borrowed books")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            display_unique_authors()
        elif choice == "5":
            sort_books()
        elif choice == "6":
            borrow_book()
        elif choice == "7":
            display_borrowed_books()
        elif choice == "8":
            print("Exiting the program.")
            break  # Correct usage of 'break' inside a loop
        else:
            print("Invalid choice. Please choose a valid option.")


# In[11]:


menu()


# In[ ]:


'''
Days of Distraction

Author: Alexandra Chang
Genre: Contemporary Fiction, Literary Fiction
Publication Year: 2020
    

The Fountainhead

Author: Ayn Rand
Genre: Fiction, Philosophy
Publication Year: 1943

White Nights

Author: Fyodor Dostoevsky
Genre: Classic, Romance
Publication Year: 1848

'''

