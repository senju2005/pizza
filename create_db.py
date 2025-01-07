import mysql.connector

connection = mysql.connector.connect(
    host="localhost", 
    user="root",       
    password="2004Aytac@"  
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS PizzaRestoran")
cursor.execute("USE PizzaRestoran")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(255) NOT NULL,
    qiymet DECIMAL(10, 2) NOT NULL,
    kateqoriya VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Musteriler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(255) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sifarisler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    musteri_id INT,
    tarix DATE,
    umumi_qiymet DECIMAL(10, 2),
    FOREIGN KEY (musteri_id) REFERENCES Musteriler(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sifaris_Detallari (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sifaris_id INT,
    menu_id INT,
    miqdar INT,
    FOREIGN KEY (sifaris_id) REFERENCES Sifarisler(id),
    FOREIGN KEY (menu_id) REFERENCES Menu(id)
)
""")


menu_items = [
    ('Margarita Pizza', 8.99, 'Pizza'),
    ('Pepperoni Pizza', 10.99, 'Pizza'),
    ('Coca Cola', 1.99, 'İçki'),
    ('Sprite', 1.89, 'İçki'),
    ('Chicken BBQ Pizza', 12.99, 'Pizza'),
    ('Veggie Pizza', 9.99, 'Pizza'),
    ('Garlic Bread', 3.49, 'Yan yemək'),
    ('Cheese Sticks', 4.99, 'Yan yemək'),
    ('Chocolate Cake', 5.49, 'Şirniyyat'),
    ('Ice Cream', 2.99, 'Şirniyyat'),
    ('Water', 0.99, 'İçki'),
    ('Fries', 3.29, 'Yan yemək'),
    ('Buffalo Wings', 7.99, 'Yan yemək'),
    ('Hawaiian Pizza', 11.99, 'Pizza'),
    ('Beef Burger', 6.99, 'Burger')
]

cursor.executemany("INSERT INTO Menu (ad, qiymet, kateqoriya) VALUES (%s, %s, %s)", menu_items)

musteriler = [
    ('Aytaç Məmmədli', '0551234567', 'aytac@example.com'),
    ('Nihad Əliyev', '0507654321', 'nihad@example.com'),
    ('Leyla Hüseynova', '0709876543', 'leyla@example.com'),
    ('Elvin Quliyev', '0774567890', 'elvin@example.com'),
    ('Aysel Məmmədova', '0512345678', 'aysel@example.com'),
    ('Murad Əhmədov', '0557654321', 'murad@example.com'),
    ('Elnarə Əliyeva', '0701122334', 'elnare@example.com'),
    ('Rəşad Qasımov', '0509988776', 'reshad@example.com'),
    ('Günay Nəcəfova', '0776655443', 'gunay@example.com'),
    ('Kamran Hüseynov', '0554433221', 'kamran@example.com')
]

cursor.executemany("INSERT INTO Musteriler (ad, telefon, email) VALUES (%s, %s, %s)", musteriler)


sifarisler = [
    (1, '2024-12-01', 19.97),
    (2, '2024-12-02', 12.49),
    (3, '2024-12-03', 25.99),
    (4, '2024-12-04', 9.99),
    (5, '2024-12-05', 15.89),
    (6, '2024-12-06', 20.99),
    (7, '2024-12-07', 30.45),
    (8, '2024-12-08', 18.29),
    (9, '2024-12-09', 8.99),
    (10, '2024-12-10', 13.59)
]

cursor.executemany("INSERT INTO Sifarisler (musteri_id, tarix, umumi_qiymet) VALUES (%s, %s, %s)", sifarisler)


sifaris_detallari = [
    (1, 1, 2),
    (1, 3, 1),
    (2, 2, 1),
    (2, 5, 1),
    (3, 4, 2),
    (3, 6, 1),
    (4, 7, 3),
    (5, 8, 2),
    (6, 9, 1),
    (7, 10, 2),
    (8, 11, 5),
    (9, 12, 3),
    (10, 13, 4)
]

cursor.executemany("INSERT INTO Sifaris_Detallari (sifaris_id, menu_id, miqdar) VALUES (%s, %s, %s)", sifaris_detallari)

connection.commit()

print("Bütün məlumatlar uğurla əlavə edildi!")
