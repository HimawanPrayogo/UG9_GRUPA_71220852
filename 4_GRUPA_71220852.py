print("""==================CAFE==================
      ==========MASUKKAN JUMLAH PESANAN==========""")
a=int(input("CAPPUCINO\tDISKON 50%\tRp 25.000\t:"))
b=int(input("VANILLA LATTE\tDISKON 65%\tRp 22.000\t:"))
c=int(input("AMERICANO\tDISKON 35%\tRp 30.000\t:"))
d=int(input("BREWED COFFEE\tDISKON 40%\tRp 20.000\t:"))

e=25000*50/100
f=22000*65/100
g=30000*35/100
h=20000*40/100

e1=a*e
f1=b*f
g1=c*g
h1=d*h
i=e1+f1+g1+h1

print("===============TOTAL===============")
print("TOTAL CAPPUCINO\t: Rp",e1)
print("TOTAL VANILLA LATTE\t: Rp",f1)
print("TOTAL AMERICANO\t: Rp",g1)
print("TOTAL BREWED COFFEE\t: Rp",h1)
print("Jumlah total biaya yang harus dibayar adalah Rp",i)

            
