#Soal 1
print("======== Calculator sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

pilihan = int(input("Masukkan pilihan: "))
bil1 = int(input("Masukkan bilangan 1: "))
bil2 = int(input("Masukkan bilangan 2: "))

def pertambahan(bil1,bil2):
    return bil1+bil2

def pengurangan(bil1,bil2):
    return bil1-bil2

def pembagian(bil1,bil2):
    return bil1/bil2

def perkalian(bil1,bil2):
    return bil1*bil2

def pangkat(bil1,bil2):
    return bil1**bil2

def calculator_sederhana():
    if pilihan ==1:
        print("Hasilnya: ", pertambahan(bil1, bil2))
    elif pilihan ==2:
        print("Hasilnya: ", pengurangan(bil1, bil2))
    elif pilihan ==3:
        print("Hasilnya: ", perkalian(bil1, bil2))
    elif pilihan ==4:
        print("Hasilnya: ", pembagian(bil1, bil2))
    elif pilihan ==5:
        print("Hasilnya: ", pangkat(bil1, bil2))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")
        
calculator_sederhana()





