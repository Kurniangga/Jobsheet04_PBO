# 1. CLASS INDUK (PARENT)
class Person:
    def __init__(self, nama, usia):
        print(f"(Memanggil __init__ Person untuk '{nama}')")
        self.nama = nama
        self.usia = usia  # Diperbaiki: sebelumnya self.nama = usia

    def perkenalkan_diri(self):
        print(f"Halo, nama saya {self.nama}, usia saya {self.usia} tahun.")

# 2. CLASS ANAK (CHILD) YANG MEWARISI PERSON
class Student(Person):
    # Student butuh __init__ sendiri untuk menampung id dan jurusan
    def __init__(self, nama, usia, student_id, jurusan):
        # Memanggil __init__ dari class induk (Person) untuk nama dan usia
        super().__init__(nama, usia) 
        self.student_id = student_id
        self.jurusan = jurusan
        print(f"(Inisialisasi atribut Student selesai untuk '{nama}')")

    def info_akademik(self):
        print(f"ID Mahasiswa: {self.student_id}")
        print(f"Jurusan: {self.jurusan}")

    def perkenalkan_diri(self):
        # Memanggil perkenalkan_diri dari class induk (Person)
        super().perkenalkan_diri() 
        # Menambahkan kalimat spesifik untuk mahasiswa
        print(f"Saya adalah mahasiswa dengan ID {self.student_id}, jurusan {self.jurusan}.")


# ==========================================
# DRIVER CODE (PROGRAM UTAMA)
# ==========================================
if __name__ == "__main__":
    # Membuat objek dari class induk (Person)
    dosen = Person("Pak Arif", 45)
    print("-" * 20)
    dosen.perkenalkan_diri()
    print("\n" + "=" * 30 + "\n")

    # Membuat objek dari class anak (Student)
    mahasiswa = Student("Dewi", 20, "MHS001", "Teknik Komputer")
    print("-" * 20)
    mahasiswa.perkenalkan_diri()
    print("-" * 20)
    mahasiswa.info_akademik()
    
    print(f"\nUsia mahasiswa {mahasiswa.nama}: {mahasiswa.usia}")