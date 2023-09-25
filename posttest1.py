print("SELAMAT DATANG DI KONVERSI MATA UANG")
print("=" *40)

login = str(input("KETIK NAMA : "))
nim = int(input("KETIK NIM : "))

Masukan_Nominal = int(input("Jumlah (IDR) : "))
print("pilihan Konversi Mata Uang : ")
print("1.USD")
print("2.Yen")
print("3.Ringgit Malaysia")
 
mata_uang_tujuan = int(input("Masukan Mata Uang Tujuan : "))
if mata_uang_tujuan == 1: 
    USD = Masukan_Nominal * 0.00006 
    print("Hasil Konversi : ", USD, "$")

elif mata_uang_tujuan == 2:
    Yen = Masukan_Nominal * 0.0097
    print("hasil Konversi : ", Yen, "¥")
elif mata_uang_tujuan == 3:
    ringgit = Masukan_Nominal * 0.00030
    print("hasil Konversi : ", "RM", ringgit )

