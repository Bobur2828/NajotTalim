#Uch xonalik son berilgan oldin uni o'nliklar xonasidagi raqam bilan yuzliklar xonasidagi raqamnni o'rnilari almashtirishdan 
# hosil bo'lgan sonni aniqlovchi dastur tuzilsin

a=int(input("Uch xonalik son kiriting"))
yuzlik=int(a/100)
onlik=int((a-yuzlik*100)/10)
birlik=int(a%10)
natija=(onlik*100+birlik*1+yuzlik*10)
print (natija)
