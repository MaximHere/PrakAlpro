'''
Input  :Aldi = 1,5,12,10,13
	Irfan = 3,5,12,17,21

Proses :1. irisan = Aldi & Irfan <---> irisan = aldi.intersection(irfan)
	2. unikaldi = aldi - irfan <----> unikaldi = aldi.differnce(irfan)
	3. unikirfan = irfan - aldi <----> inikirfan = irfan.difference(aldi)
	4. gabungan = aldi | irfan <----> gabungan = aldi.union(irfan)


Output :1. Angka keberuntungan yang sama dari kedua orang tersebut (Irisan/Intersection)
	2. Angka keberuntungan yang hanya dimiliki Aldi
	3. Angka keberuntungan yang hanya dimiliki Irfan
	4. Gabungan dari angka keberuntungan Aldi dan Irfan (Union)
'''

aldi = {1,5,12,10,13}
irfan = {3,5,12,17,21}

irisan = aldi & irfan
unikaldi = aldi - irfan
unikirfan = irfan - aldi
gabungan = irfan | aldi

print ("Angka keberuntungan yang sama dari kedua orang tersebut (Irisan/Intersection) adalah ", irisan)
print ("Angka keberuntungan yang hanya dimiliki Aldi adalah ", unikaldi)
print ("Angka keberuntungan yang hanya dimiliki oleh Irfan adalah ", unikirfan)
print ("Gabungan dari angka keberuntungan Aldi dan Irfan adalah ", gabungan)