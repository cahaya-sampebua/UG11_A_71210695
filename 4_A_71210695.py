#Soal 4
def ambildanbalik(kal,kal1,kal2,kal3):
    if kal3==True:
        return kal[kal1-1:kal2][::-1]
    else:
        return kal[kal1-1:kal2]
    
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))

