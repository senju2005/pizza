import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004Aytac@",
    database="PizzaRestoran"
)
cursor = connection.cursor()

# 1. Bütün menyu maddələrini əldə et
def show_menu():
    cursor.execute("SELECT * FROM Menu")
    results = cursor.fetchall()
    print("\n--- Menu ---")
    for row in results:
        print(f"ID: {row[0]}, Ad: {row[1]}, Qiymət: {row[2]} AZN, Kateqoriya: {row[3]}")

# 2. Müştəriləri göstər
def show_customers():
    cursor.execute("SELECT * FROM Musteriler")
    results = cursor.fetchall()
    print("\n--- Müştərilər ---")
    for row in results:
        print(f"ID: {row[0]}, Ad: {row[1]}, Telefon: {row[2]}, Email: {row[3]}")

# 3. Sifarişlərin ümumi qiymətini və tarixlərini göstər
def show_orders():
    cursor.execute("""
        SELECT Sifarisler.id, Musteriler.ad, Sifarisler.tarix, Sifarisler.umumi_qiymet
        FROM Sifarisler
        JOIN Musteriler ON Sifarisler.musteri_id = Musteriler.id
    """)
    results = cursor.fetchall()
    print("\n--- Sifarişlər ---")
    for row in results:
        print(f"ID: {row[0]}, Müştəri: {row[1]}, Tarix: {row[2]}, Ümumi Qiymət: {row[3]} AZN")

# 4. Sifariş detalları göstər
def show_order_details(order_id):
    cursor.execute("""
        SELECT Sifaris_Detallari.id, Menu.ad, Sifaris_Detallari.miqdar
        FROM Sifaris_Detallari
        JOIN Menu ON Sifaris_Detallari.menu_id = Menu.id
        WHERE Sifaris_Detallari.sifaris_id = %s
    """, (order_id,))
    results = cursor.fetchall()
    print(f"\n--- Sifariş Detalları (Sifariş ID: {order_id}) ---")
    if results:
        for row in results:
            print(f"ID: {row[0]}, Yemək: {row[1]}, Miqdar: {row[2]}")
    else:
        print("Bu sifariş üçün detallar tapılmadı.")

# 5. Yeni müştəri əlavə et
def add_customer(ad, telefon, email):
    cursor.execute("INSERT INTO Musteriler (ad, telefon, email) VALUES (%s, %s, %s)", (ad, telefon, email))
    connection.commit()
    print(f"\nMüştəri əlavə edildi: {ad}")

# 6. Yeni sifariş əlavə et
def add_order(musteri_id, tarix, umumi_qiymet):
    cursor.execute("INSERT INTO Sifarisler (musteri_id, tarix, umumi_qiymet) VALUES (%s, %s, %s)", (musteri_id, tarix, umumi_qiymet))
    connection.commit()
    print(f"\nYeni sifariş əlavə edildi: Müştəri ID {musteri_id}, Tarix {tarix}, Ümumi Qiymət {umumi_qiymet} AZN")

# 7. Menyudan müəyyən bir kateqoriyanı göstər
def show_category_items(category):
    cursor.execute("SELECT * FROM Menu WHERE kateqoriya = %s", (category,))
    results = cursor.fetchall()
    print(f"\n--- {category} Kateqoriyası ---")
    for row in results:
        print(f"ID: {row[0]}, Ad: {row[1]}, Qiymət: {row[2]} AZN")
def main():
    while True:
        print("\n--- Pizza Restoran Sorğuları ---")
        print("1. Menyunu göstər")
        print("2. Müştəriləri göstər")
        print("3. Sifarişləri göstər")
        print("4. Sifariş detalları göstər")
        print("5. Yeni müştəri əlavə et")
        print("6. Yeni sifariş əlavə et")
        print("7. Kateqoriyaya görə menyunu göstər")
        print("0. Çıxış")

        choice = input("\nSeçiminizi daxil edin: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_customers()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            order_id = int(input("Sifariş ID-ni daxil edin: "))
            show_order_details(order_id)
        elif choice == "5":
            ad = input("Müştərinin adını daxil edin: ")
            telefon = input("Telefon nömrəsini daxil edin: ")
            email = input("Email ünvanını daxil edin: ")
            add_customer(ad, telefon, email)
        elif choice == "6":
            musteri_id = int(input("Müştəri ID-ni daxil edin: "))
            tarix = input("Sifariş tarixi (YYYY-MM-DD): ")
            umumi_qiymet = float(input("Ümumi qiymət: "))
            add_order(musteri_id, tarix, umumi_qiymet)
        elif choice == "7":
            kateqoriya = input("Kateqoriyanı daxil edin (məsələn, 'Pizza', 'İçki', 'Yan yemək'): ")
            show_category_items(kateqoriya)
        elif choice == "0":
            print("Çıxılır...")
            break
        else:
            print("Yanlış seçim. Yenidən cəhd edin.")

if __name__ == "__main__":
    main()
cursor.close()
connection.close()
