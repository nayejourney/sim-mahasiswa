"""Program console Sistem Informasi Mahasiswa."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .models import DaftarMahasiswa, Mahasiswa

console = Console()
db = DaftarMahasiswa()


def tampilkan_menu() -> None:
    menu = (
        "[bold cyan]SISTEM INFORMASI MAHASISWA[/]\n\n"
        "1. Tambah mahasiswa\n"
        "2. Tampilkan semua mahasiswa\n"
        "3. Cari mahasiswa berdasarkan NIM\n"
        "4. Hapus mahasiswa\n"
        "5. Edit IPK mahasiswa\n"
        "0. Keluar"
    )
    console.print(Panel(menu, title="Menu Utama", border_style="cyan"))


def baca_ipk(prompt: str = "IPK (0.0-4.0): ") -> float:
    try:
        ipk = float(console.input(prompt))
    except ValueError as exc:
        raise ValueError("IPK harus berupa angka.") from exc
    Mahasiswa.validasi_ipk(ipk)
    return ipk


def tambah_mahasiswa() -> None:
    console.print("\n[bold]Tambah Mahasiswa[/]")
    try:
        nim = console.input("NIM: ")
        nama = console.input("Nama: ")
        prodi = console.input("Program studi: ")
        try:
            angkatan = int(console.input("Angkatan: "))
        except ValueError as exc:
            raise ValueError("Angkatan harus berupa angka tahun.") from exc
        ipk = baca_ipk()
        db.tambah(Mahasiswa(nim, nama, prodi, angkatan, ipk))
        console.print(f"[green]Berhasil menambahkan {nama}.[/]")
    except ValueError as exc:
        console.print(f"[red]Gagal: {exc}[/]")


def tampilkan_semua() -> None:
    if not db.data:
        console.print("[yellow]Belum ada data mahasiswa.[/]")
        return
    tabel = Table(title="Daftar Mahasiswa")
    for kolom in ("NIM", "Nama", "Program Studi", "Angkatan", "IPK"):
        tabel.add_column(kolom)
    for m in db.semua():
        tabel.add_row(m.nim, m.nama, m.program_studi, str(m.angkatan), f"{m.ipk:.2f}")
    console.print(tabel)


def cari_mahasiswa() -> None:
    nim = console.input("Masukkan NIM yang dicari: ")
    mahasiswa = db.cari(nim)
    if mahasiswa:
        console.print(f"[green]Ditemukan:[/] {mahasiswa}")
    else:
        console.print("[yellow]Data mahasiswa tidak ditemukan.[/]")


def hapus_mahasiswa() -> None:
    nim = console.input("Masukkan NIM yang akan dihapus: ")
    if db.hapus(nim):
        console.print("[green]Data mahasiswa berhasil dihapus.[/]")
    else:
        console.print("[yellow]Data mahasiswa tidak ditemukan.[/]")


def edit_ipk() -> None:
    nim = console.input("Masukkan NIM mahasiswa: ")
    try:
        ipk = baca_ipk("IPK baru (0.0-4.0): ")
        if db.edit_ipk(nim, ipk):
            console.print("[green]IPK berhasil diperbarui.[/]")
        else:
            console.print("[yellow]Data mahasiswa tidak ditemukan.[/]")
    except ValueError as exc:
        console.print(f"[red]Gagal: {exc}[/]")


def main() -> None:
    while True:
        tampilkan_menu()
        pilihan = console.input("\nPilih menu [0-5]: ").strip()
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            edit_ipk()
        elif pilihan == "0":
            console.print("[bold]Terima kasih. Sampai jumpa![/]")
            break
        else:
            console.print("[red]Pilihan tidak valid. Pilih angka 0 sampai 5.[/]")


if __name__ == "__main__":
    main()
