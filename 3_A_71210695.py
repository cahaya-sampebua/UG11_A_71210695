#Soal 3
kalimat = input("Masukkan Kalimat: ")
mulai = int(input("Index Start: "))
stop = int(input("Index Stop: "))

def hitung_hapus(kl,p1,p2):
    return max(0,(p2 - p1 + 1)/int(len(kl))*100)
print(hitung_hapus(kalimat,mulai,stop))
