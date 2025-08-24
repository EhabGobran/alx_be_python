class Book:
    def __init__(self, author:str, title:str, year:int):
        self.author = author
        self.title = title
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        print(f"{self.title} by {self.author}, published in {self.year}")

    def __repr__(self):
        print(f"Book('{self.title}', '{self.author}', {self.year})")
    