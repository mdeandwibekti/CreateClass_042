class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
#__init__ adalah metode konstruktor dalam Python yang otomatis dipanggil saat Anda membuat objek dari kelas.
#Dalam __init__, self adalah referensi ke instance (objek) dari kelas. self.panjang dan self.lebar adalah atribut instance yang menyimpan nilai panjang dan lebar, yang diterima sebagai parameter.
#Dengan ini, setiap objek PersegiPanjang akan memiliki atribut panjang dan lebar.
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
#keliling adalah metode yang menghitung keliling persegi panjang.
#Menggunakan atribut panjang dan lebar dari objek, metode ini mengembalikan hasil perhitungan keliling dengan rumus 2 * (panjang + lebar).

    def luas(self):
        return self.panjang * self.lebar
#luas adalah metode yang menghitung luas persegi panjang.
#Menggunakan atribut panjang dan lebar dari objek, metode ini mengembalikan hasil perkalian panjang * lebar.

    def __str__(self):
        return f"Persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"
#__str__ adalah metode spesial yang menentukan bagaimana objek PersegiPanjang akan direpresentasikan dalam bentuk string saat dicetak.
#Dalam metode ini, f"..." adalah f-string (formatted string) yang menghasilkan teks dengan informasi panjang dan lebar objek persegi panjang.
    
def main():
    try:   
        panjang = int(input("Masukkan panjang persegi panjang (cm): "))
        lebar = int(input("Masukkan lebar persegi panjang (cm): "))

        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar harus lebih dari 0")
        else:
            persegi_panjang = PersegiPanjang(panjang, lebar)
            print(persegi_panjang)  
            print("Keliling:", persegi_panjang.keliling(), "cm")  
            print("Luas:", persegi_panjang.luas(), "cm²")
    except ValueError:
        print("Input harus berupa angka yang valid.")          

if __name__ == "__main__":
    main()
#Ini adalah bagian penting dalam Python untuk menjalankan kode hanya ketika file dijalankan langsung, bukan saat diimpor sebagai modul di file lain.
#Saat file dijalankan langsung, main() akan dipanggil dan program akan berjalan dari sana.