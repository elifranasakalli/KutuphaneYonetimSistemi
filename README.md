# Kütüphane Yönetim Sistemi

## Proje Hakkında

Bu proje, Python ve SQLite kullanılarak geliştirilmiş bir Kütüphane Yönetim Sistemi uygulamasıdır. Projenin amacı kitap, üye ve ödünç alma işlemlerini dijital ortamda yönetmektir.

Sistem üzerinden kitap ve üye kayıtları tutulabilmekte, kitap ödünç verme ve iade alma işlemleri gerçekleştirilebilmektedir.

---

## Kullanılan Teknolojiler

* Python
* SQLite
* SQL
* GitHub

---

## Proje Yapısı

```text
KutuphaneYonetimSistemi

├── database.py
├── models.py
├── main.py
├── test_project.py
├── kutuphane.sql
└── README.md
```

---

## Veritabanı Tabloları

### Books

Kitap bilgilerini tutar.

| Alan     | Açıklama       |
| -------- | -------------- |
| BookID   | Kitap numarası |
| Title    | Kitap adı      |
| Author   | Yazar          |
| Quantity | Stok miktarı   |

### Members

Üye bilgilerini tutar.

| Alan      | Açıklama     |
| --------- | ------------ |
| MemberID  | Üye numarası |
| FirstName | Ad           |
| LastName  | Soyad        |

### Loans

Ödünç alma ve iade işlemlerini tutar.

| Alan       | Açıklama          |
| ---------- | ----------------- |
| LoanID     | İşlem numarası    |
| BookID     | Kitap numarası    |
| MemberID   | Üye numarası      |
| BorrowDate | Ödünç alma tarihi |
| ReturnDate | İade tarihi       |

---

## Uygulama Özellikleri

* Kitap ekleme
* Kitap listeleme
* Kitap silme
* Üye ekleme
* Üye listeleme
* Üye silme
* Kitap ödünç verme
* Kitap iade alma

---

## Çalışma Mantığı

Program çalıştırıldığında kullanıcıya bir menü sunulur.

Menü üzerinden:

1. Kitap işlemleri
2. Üye işlemleri
3. Ödünç verme işlemleri
4. İade alma işlemleri

gerçekleştirilebilir.

Ödünç verilen kitapların stok miktarı bir azaltılır. Kitap iade edildiğinde stok miktarı tekrar artırılır.

---

## Testler

Projede temel test işlemleri `test_project.py` dosyasında gerçekleştirilmiştir.

Testler:

* Kitap oluşturma
* Stok kontrolü
* Üye oluşturma
* Ödünç verme işlemi
* İade alma işlemi

---

## Geliştirici

Elif Rana Sakallı

Bilgisayar Mühendisliği
