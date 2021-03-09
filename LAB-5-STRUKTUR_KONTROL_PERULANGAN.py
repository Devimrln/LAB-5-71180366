#Devi Marline Muhammad (71180366)
'''
buatlah program yang dapat melakukan penjumlahan pada perulangan
case:
masukkan angka: 5
1 2 3 4 5
total = 15
'''
#input
angka = int(input("masukkan angka: "))
total = 0
#proses
for i in range(1, angka+1):
    print(i, end=" ")
    total = total + i

#output
print("total :", total)
