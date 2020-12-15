from tkinter import *
from tkinter import ttk
from database import DB


db = DB()


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Store Desktop Application")
        self.geometry("600x400")
        self.configure(background="Light Blue")
        self.widgets()
        self.show_all()

    def widgets(self):

        self.title_input = StringVar()
        self.author_input = StringVar()
        self.year_input = StringVar()
        self.isbn_input = StringVar()

        self.title_label = ttk.Label(self, text="Title : ")
        self.title_label.grid(column=1,row=1, sticky=E, pady=10)
        self.title_entry = ttk.Entry(self, textvariable=self.title_input)
        self.title_entry.grid(column=2, row=1, sticky=W)

        self.author_label = ttk.Label(self, text="Author : ")
        self.author_label.grid(column=3, row=1, sticky=E)
        self.author_entry = ttk.Entry(self, textvariable=self.author_input)
        self.author_entry.grid(column=4, row=1, sticky=W)

        self.year_label = ttk.Label(self, text="Year : ")
        self.year_label.grid(column=1, row=2, sticky=E)
        self.year_entry = ttk.Entry(self, textvariable=self.year_input)
        self.year_entry.grid(column=2, row=2, sticky=W)

        self.isbn_label = ttk.Label(self, text="ISBN : ")
        self.isbn_label.grid(column=3, row=2, sticky=E)
        self.isbn_entry = ttk.Entry(self, textvariable=self.isbn_input)
        self.isbn_entry.grid(column=4, row=2, sticky=W)

        self.add_button = ttk.Button(self, text="Add", command=self.add)
        self.add_button.grid(column=1, row=3, pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete)
        self.delete_button.grid(column=2, row=3)

        self.update_button = ttk.Button(self, text="Update", command=self.update)
        self.update_button.grid(column=3, row=3)

        self.search_button = ttk.Button(self, text="Search", command=self.search)
        self.search_button.grid(column=4, row=3)

        self.books = Listbox(self, height=6,width=50, border=2)
        self.books.grid(column=0, row=4, rowspan=7, columnspan=5, padx=10, pady=10)
        self.books.bind("<<ListboxSelect>>", self.select_book)

    def select_book(self, select):
        book_name = select.widget
        self.selected_line = book_name.get(ANCHOR)
        self.selected_id = self.selected_line[0]

    def show_all(self):
        self.books.delete(0, END)
        books = db.fetch()
        for book in books:
            self.books.insert(END, book)

    def add(self):
        db.insert(self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get())
        self.show_all()

    def delete(self):
        db.delete(self.selected_id)
        self.show_all()

    def update(self):
        db.update(self.selected_id, self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get())
        self.show_all()

    def search(self):
        search_index = db.search(self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get())
        for index in search_index:
            self.books.insert(END, index)


window = Window()
window.mainloop()