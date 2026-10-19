import pytest
from src.models import DaftarMahasiswa, Mahasiswa


def mahasiswa(nim="2024SI001", nama="Andi Pratama", prodi="Sistem Informasi", angkatan=2024, ipk=3.5):
    return Mahasiswa(nim, nama, prodi, angkatan, ipk)


def test_buat_mahasiswa_valid():
    m = mahasiswa()
    assert m.nim == "2024SI001"
    assert m.ipk == 3.5


def test_nim_kurang_dari_enam_karakter_ditolak():
    with pytest.raises(ValueError):
        mahasiswa(nim="abc")


def test_nim_kosong_ditolak():
    with pytest.raises(ValueError):
        mahasiswa(nim="   ")


def test_nama_kosong_ditolak():
    with pytest.raises(ValueError):
        mahasiswa(nama=" ")


@pytest.mark.parametrize("ipk", [-0.1, 4.1, 5.0])
def test_ipk_di_luar_rentang_ditolak(ipk):
    with pytest.raises(ValueError):
        mahasiswa(ipk=ipk)


@pytest.mark.parametrize("ipk", [0.0, 4.0])
def test_ipk_batas_valid(ipk):
    assert mahasiswa(ipk=ipk).ipk == ipk


def test_tambah_dan_cari_mahasiswa():
    db = DaftarMahasiswa()
    m = mahasiswa()
    db.tambah(m)
    assert db.cari(m.nim) == m
    assert db.jumlah == 1


def test_nim_duplikat_ditolak():
    db = DaftarMahasiswa()
    db.tambah(mahasiswa())
    with pytest.raises(ValueError, match="sudah terdaftar"):
        db.tambah(mahasiswa(nama="Budi"))


def test_hapus_mahasiswa_berhasil():
    db = DaftarMahasiswa()
    db.tambah(mahasiswa())
    assert db.hapus("2024SI001") is True
    assert db.jumlah == 0


def test_hapus_nim_tidak_ada():
    assert DaftarMahasiswa().hapus("2024SI999") is False


def test_cari_nim_tidak_ada():
    assert DaftarMahasiswa().cari("2024SI999") is None


def test_edit_ipk_berhasil():
    db = DaftarMahasiswa()
    db.tambah(mahasiswa())
    assert db.edit_ipk("2024SI001", 3.9) is True
    assert db.cari("2024SI001").ipk == 3.9


def test_edit_ipk_nim_tidak_ada():
    assert DaftarMahasiswa().edit_ipk("2024SI999", 3.0) is False


def test_edit_ipk_tidak_valid_ditolak():
    with pytest.raises(ValueError):
        DaftarMahasiswa().edit_ipk("2024SI001", 4.5)


def test_nama_panjang_dapat_disimpan():
    nama = "Nama Mahasiswa " * 30
    assert mahasiswa(nama=nama).nama == nama.strip()
