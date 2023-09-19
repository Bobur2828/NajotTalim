#Uch xonalik son berilgan oldin uni raqamlarini teskari yozishdan hosil bo'lgan sonni aniqlovchi dastur tuzing

a=int(input("Uch xonalik son kiriting"))
yuzlik=int(a/100)
onlik=int((a-yuzlik*100)/10)
birlik=int(a%10)
natija=(birlik*100+onlik*10+yuzlik)
print (natija)
