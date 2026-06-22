class Kitap:
 def __init__(self, kitap_id, kitap_adi, yazar, stok):

    self.kitap_id = kitap_id
    self.kitap_adi = kitap_adi
    self.yazar = yazar
    self.stok = stok

def bilgileri_getir(self):

    return {
        "kitap_id": self.kitap_id,
        "kitap_adi": self.kitap_adi,
        "yazar": self.yazar,
        "stok": self.stok
    }

def __str__(self):

    return (
        f"Kitap ID: {self.kitap_id} | "
        f"Kitap Adı: {self.kitap_adi} | "
        f"Yazar: {self.yazar} | "
        f"Stok: {self.stok}"
    )
class Uye:
 def __init__(self, uye_id, ad, soyad):

    self.uye_id = uye_id
    self.ad = ad
    self.soyad = soyad

def bilgileri_getir(self):

    return {
        "uye_id": self.uye_id,
        "ad": self.ad,
        "soyad": self.soyad
    }

def __str__(self):

    return (
        f"Üye ID: {self.uye_id} | "
        f"Ad: {self.ad} | "
        f"Soyad: {self.soyad}"
    )
class Odunc:
 def __init__(
    self,
    odunc_id,
    kitap_id,
    uye_id,
    odunc_tarihi,
    iade_tarihi=None
):

    self.odunc_id = odunc_id
    self.kitap_id = kitap_id
    self.uye_id = uye_id
    self.odunc_tarihi = odunc_tarihi
    self.iade_tarihi = iade_tarihi

def bilgileri_getir(self):

    return {
        "odunc_id": self.odunc_id,
        "kitap_id": self.kitap_id,
        "uye_id": self.uye_id,
        "odunc_tarihi": self.odunc_tarihi,
        "iade_tarihi": self.iade_tarihi
    }

def __str__(self):

    return (
        f"Ödünç ID: {self.odunc_id} | "
        f"Kitap ID: {self.kitap_id} | "
        f"Üye ID: {self.uye_id} | "
        f"Ödünç Tarihi: {self.odunc_tarihi} | "
        f"İade Tarihi: {self.iade_tarihi}"
    )