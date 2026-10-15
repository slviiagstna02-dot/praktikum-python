# praktikum-python

Proyek praktikum Pemrograman Berorientasi Objek: program Python pertama,
virtual environment, dan repositori Git/GitHub.

## Deskripsi

Proyek ini berisi dua program kecil:

- `halo.py` - menyapa pengguna, menanyakan **tahun lahir**, lalu menampilkan
  perkiraan usia. Input yang bukan angka atau tahun yang tidak masuk akal
  ditangani dengan `try/except` sehingga program meminta input ulang.
  Keluaran diberi warna dengan paket `colorama`.
- `tampil.py` - menampilkan tabel alat praktikum dengan paket `rich`.

## Prasyarat

- Python 3.10 atau lebih baru
- Git

## Membuat dan mengaktifkan virtual environment

Buat environment (sekali saja) di folder proyek:

```bash
# Windows
py -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

Aktifkan environment:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Environment aktif jika prompt terminal diawali `(.venv)`. Untuk keluar,
jalankan `deactivate`.

## Menginstal dependensi

Setelah environment aktif:

```bash
pip install -r requirements.txt
```

## Menjalankan program

```bash
python halo.py      # Windows dapat memakai: py halo.py
python tampil.py
```

Contoh keluaran `halo.py`:

```
Masukkan nama Anda: Budi
Halo, Budi! Selamat datang di praktikum Python.
Masukkan tahun lahir Anda: 2005
Perkiraan usia Anda saat ini 21 tahun.
Semoga sukses!
```

## Struktur proyek

```
praktikum-python/
├── .gitignore
├── README.md
├── halo.py
├── requirements.txt
└── tampil.py
```
