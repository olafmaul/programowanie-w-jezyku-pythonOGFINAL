class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __str__(self):
        return (f"Student {self.name}, ID: {self.ID}")


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka w {self.city}, ul. {self.street} {self.zip_code}. "
                f"Godziny: {self.open_hours}, Tel: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name}, "
                f"Zatrudniony: {self.hire_date}, Kontakt: {self.phone}, "
                f"Adres: {self.city}, ul. {self.street}")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: '{self.author_name} {self.author_surname}', {self.number_of_pages} stron. "
                f"Wydana: {self.publication_date}.\n"
                f"Biblioteka w: {self.library.city}, przy ul. {self.library.street}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list_str = "\n    ".join([str(book) for book in self.books])

        return (f"Zamówienie z dnia: {self.order_date}\n"
                f"Pracownik bilbioteki: {self.employee.first_name} {self.employee.last_name}\n"
                f"Wypożyczający: {self.student.name}  (ID: {self.student.ID})\n"
                f"Zamówione książki ({len(self.books)} szt.): \n{books_list_str}\n")


# 1. BIBLIOTEKI
library_1 = Library("Katowicach", "Matrymonialna 22", "40-123", "Pon-Pt 6-16", "32 223 441 551")
library_2 = Library("Gdańsku", "Wolności 111", "66-221", "Pon-Sb 10-21", "555 666 777")

# 2. KSIĄŻKI
book1 = Book(library_1, "26/06/1998", "J.R.R.", "Tolkien", 800)
book2 = Book(library_1, "29/07/2021", "J.R.R.", "Tolkien", 900)
book3 = Book(library_1, "22/01/2008", "J.R.R.", "Tolkien", 1000)
book4 = Book(library_2, "02/02/1997", "J.R.R.", "Tolkien", 1812)
book5 = Book(library_2, "12/04/1955", "J.R.R.", "Tolkien", 6033)

# 3. PRACOWNICY
emp1 = Employee("Adam", "Kawka", "12/10/1998", "12/10/1955", "Katowice", "Kikota 5", "11-147", "222 333 444")
emp2 = Employee("Ewa", "Sapkowska", "20/12/2008", "12/10/1966", "Gdańsk", "Długa 12", "22-019", "655 666 777")
emp3 = Employee("Michał", "Moniuszko", "06/02/2001", "12/10/1922", "Gdańsk", "Marszal 3", "55-042", "711 222 333")

# 4. STUDENCI
s1 = Student("Tomasz Zieliński", 1)
s2 = Student("Katarzyna Wójcik", 2)
s3 = Student("Marek Kaczmarek", 3)

# 5. ZAMOWIENIA
order1 = Order(emp1, s1, [book1], "31/08/2022")
order2 = Order(emp2, s2, [book2, book4, book3], "12/12/2025")

print(order1)
