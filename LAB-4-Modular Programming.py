#Tugas Video

def cekprima (x):
    for i in range (2,x):
        if x % i == 0:
            print (x, " adalah bukan bilangan Prima")
            break
    else:
        print (x, " adalah bilangan Prima")

cekprima(5)
cekprima(4)
cekprima(456)
cekprima(5009)