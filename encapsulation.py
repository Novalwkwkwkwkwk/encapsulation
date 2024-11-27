class Makanan:
    def __init__(self, variabel_privat, variabel_proteksi):
        
        self.__variabel_privat = variabel_privat
       
        self._variabel_proteksi = variabel_proteksi

    def tampilkan(self):
        
        print(f"Variabel Privat: {self.__variabel_privat}")
        print(f"Variabel Proteksi: {self._variabel_proteksi}")


class MakananTurunan(Makanan):
    def akses_proteksi(self):
    
        print(f"Mengakses Variabel Proteksi: {self._variabel_proteksi}")


makanan = Makanan("Rahasia", "Tersedia")
makanan.tampilkan()

makanan_turunan = MakananTurunan("Rahasia Baru", "Proteksi Baru")
makanan_turunan.akses_proteksi()

print(makanan._variabel_proteksi)  