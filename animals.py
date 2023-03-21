import sqlite3


class Animal:
    def __init__(self, index, name, kind, weight, age, keeper, home):
        self.index = index
        self.name = name
        self.kind = kind
        self.weight = weight
        self.age = age
        self.keeper = keeper
        self.home = home

    def __repr__(self):
        return ("Animal: " +
                "\n index: " + str(self.index)
                + "\n name: " + self.name
                + "\n kind: " + self.kind
                + "\n weight: " + str(self.weight)
                + "\n age: " + str(self.age)
                + "\n keeper: " + str(self.keeper)
                + "\n home: " + str(self.home))


class Employee:
    def __init__(self, index, name, task, salary):
        self.index = index
        self.name = name
        self.task = task
        self.salary = salary

    def __repr__(self):
        return ("Employee: " +
                "\n index: " + str(self.index)
                + "\n name: " + self.name
                + "\n task: " + self.task
                + "\n salary: " + str(self.salary))


class Avial:
    def __init__(self, index, width, height, capacity):
        self.index = index
        self.width = width
        self.height = height
        self.capacity = capacity

    def __repr__(self):
        return ("Employee: " +
                "\n index: " + str(self.index)
                + "\n width: " + self.width
                + "\n height: " + self.height
                + "\n capacity: " + str(self.capacity))


def add_animals(cursor):
    borya = Animal(0, "Borya", "bear", 300, 20, 1, 1)
    gosha = Animal(1, "Gosha", "lion", 150, 10, 2, 2)
    misha = Animal(2, "Misha", "eagle", 20, 5, 1, 3)

    animals = [borya, gosha, misha]

    cursor.execute('''CREATE TABLE IF NOT EXISTS animals(
                id INT PRIMARY KEY,
                name TEXT,
                kind TEXT,
                weight REAL,
                age INT,
                keeper INT,
                home INT
                )''')

    for animal in animals:
        cursor.execute('''INSERT INTO animals VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (animal.index, animal.name, animal.kind, animal.weight, animal.age, animal.keeper, animal.home))


def add_employee(cursor):
    victor = Employee(0, "Victor Petrov", "feed", 50000)
    leonid = Employee(1, "Leonid ", "clean", 45000)
    employees = [victor, leonid]

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
                id INT PRIMARY KEY,
                name TEXT,
                task TEXT,
                salary INT
                )''')

    for employee in employees:
        cursor.execute('''INSERT INTO employees VALUES (?, ?, ?, ?)''',
                       (employee.index, employee.name, employee.task, employee.salary))


def add_avials(cursor):
    avials = [
        Avial(0, 120, 180, 1),
        Avial(1, 200, 100, 2),
        Avial(2, 200, 300, 1),
    ]

    cursor.execute('''CREATE TABLE IF NOT EXISTS avials(
                id INT PRIMARY KEY,
                width TEXT,
                height TEXT,
                capacity INT
                )''')

    for avial in avials:
        cursor.execute('''INSERT INTO avials VALUES (?, ?, ?, ?)''',
                       (avial.index, avial.width, avial.height, avial.capacity))


def main():
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()

    add_animals(cursor)
    add_employee(cursor)
    add_avials(cursor)

    r = cursor.fetchall()

    print(r)


if __name__ == "__main__":
    main()
