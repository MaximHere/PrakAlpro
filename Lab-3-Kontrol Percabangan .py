print ("Program Kalkulator")
print ("Pilih pilihan menu berikut: \n 1. Penambahan \n 2. Pengurangan \n 3. Perkalian \n 4. Pembagian")
pilihan = int(input("Input menu pilihan dengan menuliskan nomernya: "))
if pilihan == 1:
    print ("Menambahkan bilangan A + B:")
    a = float(input("Masukan bilangan A = "))
    b = float(input("Masukan bilangan B = "))
    hasil = a + b
    print ("Hasil A + B adalah ", hasil)
elif pilihan == 2:
    print ("Pengurangan bilangan A - B")
    a = float(input("Masukan bilangan A = "))
    b = float(input("Masukan Bilangan B = "))
    hasil = a - b
    print ("Hasil dari A - B adalah ", hasil)
elif pilihan == 3:
    print ("Perkalian bilangan A * B")
    a = float(input("Masukan bilangan A = "))
    b = float(input("Masukan bilangan B = "))
    hasil = a * b
    print ("Hasil dari A * B adalah ", hasil)
elif pilihan == 4:
    print ("Pembagian bilangan A / B")
    a = float(input("Masukan bilangan A = "))
    b = float(input("Masukan bilangan B = "))
    hasil = a / b
    print ("Hasil dari A / B adalah ", hasil)
else:
    print ("Pilihan salah / Pilihan tidak tersedia")