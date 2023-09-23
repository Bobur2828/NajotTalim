#Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab qancha minut va sekund
# to'la  o'tganligini aniqlovchi dastur tuzing.
N=int(input("Kun boshidan boshlab nechchi sekund o'tganligini kiriting"))
MINUTE=int(N/60)
SECOND=int(N%60)
print("Kun boshidan boshlab to'liq", MINUTE,"minut  va  ",SECOND," sekund o'tdi ")