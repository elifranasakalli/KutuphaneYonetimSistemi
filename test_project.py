import unittest


class TestKutuphaneYonetimSistemi(unittest.TestCase):

    def test_kitap_olusturma(self):

        kitap_adi = "Suç ve Ceza"

        self.assertEqual(
            kitap_adi,
            "Suç ve Ceza"
        )

    def test_stok_kontrolu(self):

        stok = 5

        self.assertTrue(stok > 0)

    def test_uye_olusturma(self):

        ad = "Elif"
        soyad = "Sakallı"

        self.assertEqual(ad, "Elif")
        self.assertEqual(soyad, "Sakallı")

    def test_odunc_verme(self):

        stok = 3

        stok -= 1

        self.assertEqual(stok, 2)

    def test_iade_alma(self):

        stok = 2

        stok += 1

        self.assertEqual(stok, 3)


if __name__ == "__main__":
    unittest.main()