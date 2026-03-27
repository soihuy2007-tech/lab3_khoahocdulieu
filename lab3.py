import sqlite3

conn = sqlite3.connect("lab3.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE khach_hang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten TEXT,
    tuoi INTEGER,
    dia_chi TEXT
)
""")

cursor.execute("""
INSERT INTO khach_hang (ten, tuoi, dia_chi)
VALUES ('Nguyen Van A', 20, 'Ha Noi')
""")

conn.commit()
conn.close()

print("Tao bang thanh cong!")