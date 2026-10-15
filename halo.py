# halo.py - program Python pertama
from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

tahun_ini = date.today().year

# Ulangi sampai pengguna memasukkan tahun lahir yang valid
while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    except ValueError:
        print("Input harus berupa angka, misalnya 2005. Coba lagi.")
        continue

    if tahun_lahir > tahun_ini:
        print(f"Tahun lahir tidak boleh lebih dari {tahun_ini}. Coba lagi.")
        continue

    if tahun_lahir < 1900:
        print("Tahun lahir tidak valid. Coba lagi.")
        continue

    break

usia = tahun_ini - tahun_lahir

print(f"Perkiraan usia Anda saat ini {usia} tahun.")
print("Semoga sukses!")
