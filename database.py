import sqlite3

class Veritabani:

    def __init__(self):
        self.conn = sqlite3.connect("kutuphane.db")
        self.cursor = self.conn.cursor()

        self.tablolari_olustur()

    def tablolari_olustur(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books(
            BookID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,
            Quantity INTEGER NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Members(
            MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Loans(
            LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
            BookID INTEGER,
            MemberID INTEGER,
            BorrowDate TEXT,
            ReturnDate TEXT,
            FOREIGN KEY(BookID) REFERENCES Books(BookID),
            FOREIGN KEY(MemberID) REFERENCES Members(MemberID)
        )
        """)

        self.conn.commit()

    def baglantiyi_kapat(self):
        self.conn.close()