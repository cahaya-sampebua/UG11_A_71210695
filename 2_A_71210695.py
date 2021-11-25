#Soal 2
def ambil_huruf(kalimat,brt):       
    return kalimat[int(len(kalimat)/2+brt)]

print(ambil_huruf("abcdefg",1))
print(ambil_huruf("abcdefg",2))
print(ambil_huruf("abcd",0))
