handle = open("diary.txt", "a")
hari = str(input("Hari: "))
tanggal = str(input("Tanggal (dd month yyyy): "))
isi = str(input("Masukan Diary: "))
handle.write("======== " + hari + ", " + tanggal + "\t========= \n")
handle.write(isi + "\n")
handle.write("\n")
handle.close