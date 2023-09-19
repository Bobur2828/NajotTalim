##Uch xonalik son berilgan uni raqamlar yig'indisini aniqlovchi dastur tuzing
#chiqaruvchi dastur tuzing
a=int(input("Uch xonalik son kiriting"))
birlik=int(a%10)
b=int(a/10)
onlik=int(b%10)
yuzlik=int(a/100)

print(a,"sonlarining raqamlar yig'indisi ",birlik+onlik+yuzlik)