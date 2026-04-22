import locale

# Set locale ke Indonesia untuk format mata uang
try:
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
except locale.Error:
    print("Locale id_ID.UTF-8 tidak tersedia, menggunakan locale default.")

# Fungsi helper untuk format mata uang
def format_rupiah(angka):
    return locale.currency(angka, grouping=True, symbol='Rp ')

# Kelas Induk
class Pegawai:
    def __init__(self, nama, id_pegawai, gaji_pokok):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        # Gaji dasar, bisa di-override
        return self.gaji_pokok

    def tampilkan_info(self):
        print(f"ID: {self.id_pegawai}, Nama: {self.nama}")
        print(f"  Gaji Pokok: {format_rupiah(self.gaji_pokok)}")

# Kelas Anak 1
class Manager(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    # Override hitung_gaji
    def hitung_gaji(self):
        gaji_total = super().hitung_gaji() + self.tunjangan_jabatan
        return gaji_total

    # Override tampilkan_info (memanggil versi induk)
    def tampilkan_info(self):
        print("--- Info Manager ---")
        super().tampilkan_info() # Panggil info dasar dari Pegawai
        print(f"  Tunjangan Jabatan: {format_rupiah(self.tunjangan_jabatan)}")
        print(f"  Total Gaji: {format_rupiah(self.hitung_gaji())}")

# Kelas Anak 2
class StafTeknis(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, keahlian, bonus_keahlian):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.keahlian = keahlian
        self.bonus_keahlian = bonus_keahlian

    # Override hitung_gaji
    def hitung_gaji(self):
        gaji_total = super().hitung_gaji() + self.bonus_keahlian
        return gaji_total

    # Override tampilkan_info (memanggil versi induk)
    def tampilkan_info(self):
        print("--- Info Staf Teknis ---")
        super().tampilkan_info() # Panggil info dasar dari Pegawai
        print(f"  Keahlian: {self.keahlian}")
        print(f"  Bonus Keahlian: {format_rupiah(self.bonus_keahlian)}")
        print(f"  Total Gaji: {format_rupiah(self.hitung_gaji())}")

# --- Kode Utama ---
if __name__ == "__main__":
    manager1 = Manager("Budi Santoso", "M001", 10000000, 5000000)
    staf1 = StafTeknis("Citra Lestari", "S001", 7000000, "Python Programming", 1500000)
    pegawai_baru = Pegawai("Rian", "P005", 5000000) # Pegawai biasa

    print("Menampilkan Informasi Pegawai:")
    manager1.tampilkan_info()
    print("-" * 30)

    staf1.tampilkan_info()
    print("-" * 30)

    print("--- Info Pegawai Baru ---")
    pegawai_baru.tampilkan_info()
    print(f"  Total Gaji: {format_rupiah(pegawai_baru.hitung_gaji())}") # Memanggil versi Pegawai
    print("-" * 30)