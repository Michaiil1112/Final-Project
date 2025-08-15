import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("library.json","r", encoding="utf-8") as f:
                self.books = [Book(**data) for data in json.load(f)]  
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open("library.json", "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, ensure_ascii=False, indent=3)

    def add_book(self):
        title = input("Название книги: ")
        author = input("Автор: ")
        year = input("Год: ")
        self.books.append(Book(title, author, year))
        self.save_books()

    def show_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.title} — {book.author} ({book.year})")

    def find_book(self):
        search = input("Введите название или автора: ").lower()
        for book in self.books:
            if search in book.title.lower() or search in book.author.lower() or search in book.year.lower():
                print(f"{book.title} — {book.author} ({book.year})")

lib = Library()

while True:
    print("\n1. Показать книги\n2. Добавить книгу\n3. Найти книгу\n4. Выход")
    choice = input("Выберите: ")
    if choice == "1":
        lib.show_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.find_book()
    elif choice == "4":
        break

