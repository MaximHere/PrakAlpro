'''Input = baris (banyak baris)
Proses= for n kali (baris+1):
		for (baris, 0):
			Print spasi
		for (1, n+1)
			print *
		for (1, n):
			print *
Output= Segitiga seperti pada soal'''

baris = int(input("Masukan jumlah baris: "))
x = baris
for a in range (1, baris+1):
    for b in range (x,0, -1):
        print (" ", end=" ")
    for c in range (1, a+1):
        print ("*", end=" ")
    for d in range (1,a):
        print ("*", end=" ")

    x -= 1
    print ()
