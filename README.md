# Sistem Informasi Mahasiswa (SIM)

Aplikasi console berbasis Python untuk mengelola data mahasiswa Program Studi Sistem Informasi. Proyek ini dibuat untuk praktikum **Pemrograman Python — Setup Tools**.

## Identitas Mahasiswa

- **Nama:** Khanaya Salsabila
- **NIM:** 20241320021
- **Kelas Praktikum:** A1
- **GitHub:** [@nayejourney](https://github.com/nayejourney)


## Fitur

- Menambah data mahasiswa (NIM, nama, program studi, angkatan, dan IPK).
- Menampilkan seluruh data mahasiswa dalam tabel.
- Mencari mahasiswa berdasarkan NIM.
- Menghapus data mahasiswa berdasarkan NIM.
- Mengubah IPK berdasarkan NIM.
- Validasi NIM, nama, program studi, tahun angkatan, dan IPK (0.0–4.0).
- Menolak NIM duplikat.
- Pengujian otomatis dengan `pytest`.

**Catatan:** Data disimpan di memori selama program berjalan; data akan kembali kosong ketika program ditutup. Penyimpanan database belum termasuk ruang lingkup praktikum setup tools ini.

## Persyaratan

- Python 3.10 atau lebih baru.
- pip.
- Git (untuk version control).

## Instalasi

### Windows PowerShell

```powershell
git clone https://github.com/nayejourney/sim-mahasiswa.git
cd sim-mahasiswa
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Jika PowerShell memblokir aktivasi script, gunakan Command Prompt dan jalankan `venv\Scripts\activate.bat`, atau ikuti kebijakan eksekusi yang ditetapkan pada perangkatmu.

## Menjalankan Program

Jalankan dari direktori root proyek dengan virtual environment aktif:

```bash
python -m src.main
```

Pilih menu 1–5 untuk mengelola data dan 0 untuk keluar.

## Menjalankan Pengujian

```bash
python -m pytest tests/ -v
```

## Struktur Proyek

```text
sim-mahasiswa/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
│   ├── README.md
│   └── demo-output.txt
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup Checklist

- [ ] Python 3.10+ terinstal (`python --version` atau `py --version`).
- [ ] pip terinstal (`python -m pip --version`).
- [ ] Virtual environment dibuat dan diaktivasi.
- [ ] Paket terinstal dari `requirements.txt`.
- [ ] `.gitignore` dikonfigurasi.
- [ ] Program berjalan tanpa error.
- [ ] Seluruh unit test lulus.
- [ ] Repository Git diinisiasi.
- [ ] Remote GitHub `origin` terhubung.
- [ ] Perubahan berhasil di-push ke GitHub.
- [ ] README sudah dilengkapi dengan NIM dan kelas.
- [ ] Minimal 3 commit bermakna tersedia.
- [ ] Screenshot output program disimpan di `docs/` (pengayaan).


## Riwayat Pengembangan yang Disarankan

```text
chore: inisiasi struktur proyek Python
feat: implementasi model dan operasi data mahasiswa
feat: implementasi menu CRUD dan edit IPK
test: tambah pengujian validasi dan operasi mahasiswa
 docs: lengkapi README dan panduan penggunaan
```

