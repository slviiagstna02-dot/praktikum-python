
# halo.py - program Python pertama
from datetime import date
from colorama import Fore, Style, init

init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")

tahun_ini = date.today().year

# Ulangi sampai pengguna memasukkan tahun lahir yang valid
while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    except ValueError:
        print(
            Fore.RED
            + "Input harus berupa angka, misalnya 2005. Coba lagi."
        )
        continue

    if tahun_lahir > tahun_ini:
        print(
            Fore.RED
            + f"Tahun lahir tidak boleh lebih dari {tahun_ini}. Coba lagi."
        )
        continue

    break

usia = tahun_ini - tahun_lahir

print(Fore.CYAN + f"Perkiraan usia Anda saat ini {usia} tahun.")
print(Fore.YELLOW + Style.BRIGHT + "Semoga sukses!")
