#Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab qancha 
# soat,  va qancha sekund  o'tganini aniqlovchi dastur tuzing.
N=int(input("Kun boshidan boshlab qancha sekund o'tganini kiriting"))
MINUTE=int(N/60)
MINUTE1=int(N%60)
SOAT=int(MINUTE/60)
print("Kun boshidan boshlab to'liq",SOAT,"soat va ",MINUTE1,"sekund o'tdi")