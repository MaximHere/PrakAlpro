''''Input=	input "Saya"
	input "suka"
	input "makan"
Proses=	while input != "keluar/exit":
		input
		total = total + inputan
	print total
output= "Saya suka makan"'''

kata = ""
total = ""

while kata != "exit":
    total = total + " " + kata
    kata = str(input("Masukan kata: "))
print (total)