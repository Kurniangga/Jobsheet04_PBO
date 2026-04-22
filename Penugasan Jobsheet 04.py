class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            predikat = "Dengan Pujian"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        else:
            predikat = "Cukup"
        print(f"Predikat: {predikat}")

class MahasiswaSarjana(Mahasiswa):
    def __init__(self, nama, nim, ipk, semester, sks_lulus):
        super().__init__(nama, nim, ipk)
        self.semester = semester
        self.sks_lulus = sks_lulus

    def tampilkan_info(self):
        super().tampilkan_info()
        # Menambahkan info spesifik Sarjana
        print(f"Semester: {self.semester}")
        print(f"SKS Lulus: {self.sks_lulus}")

class MahasiswaMagister(Mahasiswa):
    def __init__(self, nama, nim, ipk, judul_tesis, nama_pembimbing):
        super().__init__(nama, nim, ipk)
        self.judul_tesis = judul_tesis
        self.nama_pembimbing = nama_pembimbing

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Judul Tesis: {self.judul_tesis}")
        print(f"Pembimbing: {self.nama_pembimbing}")

    def hitung_predikat(self):
        if self.ipk >= 3.75:
            predikat = "Cum Laude (Dengan Pujian)"
        elif self.ipk >= 3.5:
            predikat = "Sangat Memuaskan"
        else:
            predikat = "Memuaskan"
        print(f"Predikat Magister: {predikat}")

if __name__ == "__main__":
    print("--- Info Mahasiswa Sarjana ---")
    mhs1 = MahasiswaSarjana("Andi Pratama", "3.33.24.0.01", 3.65, 5, 110)
    mhs1.tampilkan_info()
    mhs1.hitung_predikat()

    print("\n--- Info Mahasiswa Magister ---")
    mhs2 = MahasiswaMagister("Budi Santoso", "3.33.20.1.99", 3.85, "Analisis Keamanan Jaringan IoT", "Dr. Ir. Prayitno")
    mhs2.tampilkan_info()
    mhs2.hitung_predikat()