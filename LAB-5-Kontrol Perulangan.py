jumlah_baris = int(input("Masukan jumlah baris: "))
for a in range (1, jumlah_baris + 1):
    angka = 1
    for b in range (1, a+1):
        print (angka, end=" ")
        angka = angka + 1
    print ("\r")

# print ("coba", end="")
# print ("coba")