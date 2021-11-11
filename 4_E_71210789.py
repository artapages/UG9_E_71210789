#input
a = int(input("Masukkan nilai suku pertama : "))
n = int(input("Masukkan suku yang dicari : "))
r = int(input("Masukkan rasio tiap suku : "))

#proses
Sn = (a*(r**n-1))/(r-1)

#cetak layar
print("Hasil jumlah suku ke-11 dari deret 1,3,9,27,81,.. adalah",Sn)
