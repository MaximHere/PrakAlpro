# input = r / jari
# proses: hitung Luas dan Keliling
# Output= LUas dan Keliling

#Formula: Luas = pi*r^2
#        Keliling = 2*pi*r = pi*d

print ("================ Program Menghitung Luas dan Keliling Lingkaran ===========")
pi = 3.14159
r = int(input("Masukan jari-jari lingkaran (cm) = "))

luas = pi*(r**2)
keliling = 2*pi*r

print ("Luas Lingkaran dengan jari-jari ", r, " adalah ", luas, " cm^2")
print ("Keliling Lingkaran dengan jari-jari ", r, "adalah ", keliling, " cm")
