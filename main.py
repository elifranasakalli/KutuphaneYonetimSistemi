from database import Veritabani
from datetime import datetime

vt = Veritabani()


def kitap_ekle():

    print("\n=== KİTAP EKLE ===")

    kitap_adi = input("Kitap Adı: ")
    yazar = input("Yazar: ")
    stok = int(input("Stok Miktarı: "))

    vt.cursor.execute("""
        INSERT INTO Books
        (Title, Author, Quantity)
        VALUES (?, ?, ?)
    """, (kitap_adi, yazar, stok))

    vt.conn.commit()

    print("Kitap başarıyla eklendi.")


def kitaplari_listele():

    print("\n=== KİTAPLAR ===")

    vt.cursor.execute("""
        SELECT *
        FROM Books
    """)

    kitaplar = vt.cursor.fetchall()

    if len(kitaplar) == 0:
        print("Kayıtlı kitap bulunamadı.")
        return

    for kitap in kitaplar:

        print(
            f"ID: {kitap[0]} | "
            f"Kitap: {kitap[1]} | "
            f"Yazar: {kitap[2]} | "
            f"Stok: {kitap[3]}"
        )


def kitap_sil():

    kitaplari_listele()

    kitap_id = input("\nSilinecek kitap ID: ")

    vt.cursor.execute("""
        DELETE FROM Books
        WHERE BookID = ?
    """, (kitap_id,))

    vt.conn.commit()

    print("Kitap silindi.")

def uye_ekle():

    print("\n=== ÜYE EKLE ===")

    ad = input("Ad: ")
    soyad = input("Soyad: ")

    vt.cursor.execute("""
        INSERT INTO Members
        (FirstName, LastName)
        VALUES (?, ?)
    """, (ad, soyad))

    vt.conn.commit()

    print("Üye başarıyla eklendi.")


def uyeleri_listele():

    print("\n=== ÜYELER ===")

    vt.cursor.execute("""
        SELECT *
        FROM Members
    """)

    uyeler = vt.cursor.fetchall()

    if len(uyeler) == 0:
        print("Kayıtlı üye bulunamadı.")
        return

    for uye in uyeler:

        print(
            f"ID: {uye[0]} | "
            f"Ad: {uye[1]} | "
            f"Soyad: {uye[2]}"
        )


def uye_sil():

    uyeleri_listele()

    uye_id = input("\nSilinecek üye ID: ")

    vt.cursor.execute("""
        DELETE FROM Members
        WHERE MemberID = ?
    """, (uye_id,))

    vt.conn.commit()

    print("Üye silindi.")

def kitap_odunc_ver():

    print("\n=== KİTAP ÖDÜNÇ VER ===")

    kitaplari_listele()
    uyeleri_listele()

    kitap_id = input("\nKitap ID: ")
    uye_id = input("Üye ID: ")

    vt.cursor.execute("""
        SELECT Quantity
        FROM Books
        WHERE BookID = ?
    """, (kitap_id,))

    kitap = vt.cursor.fetchone()

    if kitap is None:
        print("Kitap bulunamadı.")
        return

    if kitap[0] <= 0:
        print("Bu kitap stokta yok.")
        return

    tarih = datetime.now().strftime("%d.%m.%Y")

    vt.cursor.execute("""
        INSERT INTO Loans
        (BookID, MemberID, BorrowDate)
        VALUES (?, ?, ?)
    """, (kitap_id, uye_id, tarih))

    vt.cursor.execute("""
        UPDATE Books
        SET Quantity = Quantity - 1
        WHERE BookID = ?
    """, (kitap_id,))

    vt.conn.commit()

    print("Kitap ödünç verildi.")

def kitap_iade_al():

    print("\n=== KİTAP İADE AL ===")

    vt.cursor.execute("""
        SELECT *
        FROM Loans
        WHERE ReturnDate IS NULL
    """)

    oduncler = vt.cursor.fetchall()

    if len(oduncler) == 0:
        print("Aktif ödünç kaydı bulunamadı.")
        return

    for odunc in oduncler:

        print(
            f"Ödünç ID: {odunc[0]} | "
            f"Kitap ID: {odunc[1]} | "
            f"Üye ID: {odunc[2]} | "
            f"Tarih: {odunc[3]}"
        )

    odunc_id = input("\nİade edilecek Ödünç ID: ")

    vt.cursor.execute("""
        SELECT BookID
        FROM Loans
        WHERE LoanID = ?
    """, (odunc_id,))

    kitap = vt.cursor.fetchone()

    if kitap is None:
        print("Ödünç kaydı bulunamadı.")
        return

    kitap_id = kitap[0]

    tarih = datetime.now().strftime("%d.%m.%Y")

    vt.cursor.execute("""
        UPDATE Loans
        SET ReturnDate = ?
        WHERE LoanID = ?
    """, (tarih, odunc_id))

    vt.cursor.execute("""
        UPDATE Books
        SET Quantity = Quantity + 1
        WHERE BookID = ?
    """, (kitap_id,))

    vt.conn.commit()

    print("Kitap başarıyla iade alındı.")

while True:

    print("\n")
    print("===== KÜTÜPHANE YÖNETİM SİSTEMİ =====")
    print("1 - Kitap Ekle")
    print("2 - Kitapları Listele")
    print("3 - Kitap Sil")
    print("4 - Üye Ekle")
    print("5 - Üyeleri Listele")
    print("6 - Üye Sil")
    print("7 - Kitap Ödünç Ver")
    print("8 - Kitap İade Al")
    print("9 - Çıkış")

    secim = input("\nSeçiminiz: ")

    if secim == "1":
        kitap_ekle()

    elif secim == "2":
        kitaplari_listele()

    elif secim == "3":
        kitap_sil()

    elif secim == "4":
        uye_ekle()

    elif secim == "5":
        uyeleri_listele()

    elif secim == "6":
        uye_sil()

    elif secim == "7":
        kitap_odunc_ver()

    elif secim == "8":
        kitap_iade_al()

    elif secim == "9":

        print("Program sonlandırıldı.")

        vt.baglantiyi_kapat()

        break

    else:

        print("Geçersiz seçim yaptınız.")