'''
Input  = Tambahan daftar belanjaan / kosong / "exit"
Proses = while:
		if input == kosong:
			print(tuple)
		if input == exit:
			keluar
		else:
			Penambahan tuple
Output = penambahan dilakukan di tipe data tuple
	 Print (tuple)
	 Keluar'''

daftar = ('Apel', 'Pisang','Tomat')
inputan = input("Tambah daftar belanjaan (exit --> Keluar, tekan enter untuk melihat daftar belanja) : ")
while inputan != "exit":
    if inputan == "":
        print ("Daftar belanjaan anda: ")
        print (daftar)
        print ()
    else:
        daftar = daftar + (inputan,)
        print ("Daftar belanjaan anda: ")
        print (daftar)
        print ()
    inputan = input("Tambah daftar belanjaan (exit --> Keluar, tekan enter untuk melihat daftar belanja) : ")