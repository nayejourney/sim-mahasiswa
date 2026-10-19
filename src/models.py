"""Model data dan operasi pengelolaan mahasiswa."""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Mahasiswa:
    """Merepresentasikan satu data mahasiswa."""
    nim: str
    nama: str
    program_studi: str
    angkatan: int
    ipk: float = 0.0

    def __post_init__(self) -> None:
        self.nim = self.nim.strip()
        self.nama = self.nama.strip()
        self.program_studi = self.program_studi.strip()
        if not self.nim or len(self.nim) < 6:
            raise ValueError("NIM wajib diisi dan minimal 6 karakter.")
        if not self.nama:
            raise ValueError("Nama tidak boleh kosong.")
        if not self.program_studi:
            raise ValueError("Program studi tidak boleh kosong.")
        if not isinstance(self.angkatan, int) or self.angkatan < 1900:
            raise ValueError("Angkatan harus berupa tahun yang valid.")
        self.validasi_ipk(self.ipk)

    @staticmethod
    def validasi_ipk(ipk: float) -> None:
        if not isinstance(ipk, (int, float)) or not 0.0 <= float(ipk) <= 4.0:
            raise ValueError("IPK harus berada pada rentang 0.0 sampai 4.0.")

    def __str__(self) -> str:
        return (f"{self.nim} | {self.nama} | {self.program_studi} | "
                f"{self.angkatan} | IPK: {self.ipk:.2f}")


@dataclass
class DaftarMahasiswa:
    """Menyimpan data mahasiswa selama program berjalan."""
    data: list[Mahasiswa] = field(default_factory=list)

    def tambah(self, mahasiswa: Mahasiswa) -> None:
        if self.cari(mahasiswa.nim) is not None:
            raise ValueError(f"NIM {mahasiswa.nim} sudah terdaftar.")
        self.data.append(mahasiswa)

    def semua(self) -> list[Mahasiswa]:
        return list(self.data)

    def cari(self, nim: str) -> Optional[Mahasiswa]:
        nim = nim.strip()
        return next((m for m in self.data if m.nim == nim), None)

    def hapus(self, nim: str) -> bool:
        mahasiswa = self.cari(nim)
        if mahasiswa is None:
            return False
        self.data.remove(mahasiswa)
        return True

    def edit_ipk(self, nim: str, ipk_baru: float) -> bool:
        Mahasiswa.validasi_ipk(ipk_baru)
        mahasiswa = self.cari(nim)
        if mahasiswa is None:
            return False
        mahasiswa.ipk = float(ipk_baru)
        return True

    @property
    def jumlah(self) -> int:
        return len(self.data)
