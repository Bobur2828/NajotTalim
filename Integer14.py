#Uch xonalik son berilgan oldin uni o'ngdan birinchi raqamni o'chirib chap tarafiga yozishdan hosil 
# bo'lgan sonni aniqlovchi dastur tuzing

a=int(input("Uch xonalik son kiriting"))
yuzlik=int(a/100)
onlik=int((a-yuzlik*100)/10)
birlik=int(a%10)
natija=(birlik*100+yuzlik*10+onlik)
print (natija)
