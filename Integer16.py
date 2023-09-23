#Uch xonalik son berilgan oldin uni o'nliklar xonasidagi raqam bilan birliklar xonasidagi raqamnni o'rnilari almashtirishdan 
# hosil bo'lgan sonni aniqlovchi dastur tuzilsin

a=int(input("Uch xonalik son kiriting"))
yuzlik=int(a/100)
onlik=int((a-yuzlik*100)/10)
birlik=int(a%10)
natija=(yuzlik*100+birlik*10+onlik*1) 
print (natija)
