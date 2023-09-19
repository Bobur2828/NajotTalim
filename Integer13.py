#Uch xonalik son berilgan oldin uni chapdan birinchi raqamni o'chirib o'ng tarafiga yozishdan hosil 
# bo'lgan sonni aniqlovchi dastur tuzing

a=int(input("Uch xonalik son kiriting"))
yuzlik=int(a/100)
onlik=int((a-yuzlik*100)/10)
birlik=int(a%10)
natija=(onlik*100+birlik*10+yuzlik)
print (natija)
