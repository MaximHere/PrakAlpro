'''While pilihan != 3:
	if pilihan 1:
		append list
	elif pilihan == 2:
		print daftar belanja
		input edit
		if edit == 0:
			kembali ke main menu (continue)
		else:
			hapus list yang dipilih'''

daftarlist = ["Apel", "Jambu"]
pilihan = 0
while pilihan != 3:
    print("Pilihan:")
    print("1. Tambah daftar belanja")
    print("2. Lihat/Hapus daftar belanja")
    print("3. Keluar")
    pilihan = int(input("Masukan pilihan anda: "))
    if pilihan == 1:
        tambah = str(input("Masukan item yang ingin ditambah: "))
        daftarlist.append(tambah)
    elif pilihan == 2:
        print("Daftar belanjaan:")
        for i in range (len(daftarlist)):
            print(i+1,". ", daftarlist[i])
        edit = int(input("Masukan nomor item yang akan dihapus (0 = Main Menu): "))
        if edit == 0:
            continue
        else:
            daftarlist.pop(edit-1)
    elif pilihan == 3:
        break
    else:
        print("Input salah/tidak ada opsinya")

