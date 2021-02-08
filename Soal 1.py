print("====================================================")
print("****************** Justice League ******************")
print("====================================================")
username = input("Masukan username anda: ")
anggotalst = []
if username == "brucewyne" or username ==  "victorstone" or username == "ciscoramon":
    print("======== WELCOME ", username, " ==========")
    
    pilihan = 0
    while pilihan != 4:
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. Tampilkan Anggota Justice League")
        print("4. Exit")
        pilihan = int(input("Masukan pilihan anda: "))
        if pilihan == 4:
            break
        else:
            if pilihan == 1:
                inputanggota = input("Nama Anggota baru: ")
                anggotalst.append(inputanggota)
                print("data '", inputanggota, "' berhasil ditambahkan")
            elif pilihan == 2:
                anggotahapus = input("Anggota yang akan dihapus: ")
                if anggotalst.count(anggotahapus) == 1:
                    anggotalst.pop(anggotalst.index(anggotahapus))
                    print("data '", anggotahapus, "' berhasil dihapus")
                else:
                    print("data '", anggotahapus, "' tidak ditemukan")
            elif pilihan == 3:
                print("Daftar anggota Justice League")
                print(anggotalst)
    if username == "brucewyne" or username ==  "victorstone":
        print("see u next time MR. ", username, ", GLHF")
    elif username == "ciscoramon":
        print("see u next time MS. ", username, ", GLHF")
else:
    print("Acces Denied")