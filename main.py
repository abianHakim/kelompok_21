from linked_list_buku import LinkedListBuku
daftar_buku = LinkedListBuku()

def tambah_buku():
    id_buku = input("Masukkan ID Buku: ")
    judul = input("Masukkan Judul: ")
    penulis = input("Masukkan Penulis: ")
    stok = int(input("Masukkan Stok Buku: "))

    daftar_buku.tambah_buku(id_buku, judul, penulis, stok)
    print("Buku berhasil ditambahkan.")

def edit_buku():
    id_buku = input("Masukkan ID Buku yang ingin diedit: ")

    print("Kosongkan input jika tidak ingin mengubah data.")
    judul = input("Masukkan Judul Baru: ").strip()
    penulis = input("Masukkan Penulis Baru: ").strip()
    stok_input = input("Masukkan Stok Baru: ").strip()

    stok = None
    if stok_input:
        try:
            stok = int(stok_input)
        except ValueError:
            print("Stok harus berupa angka.")
            return

    if daftar_buku.edit_buku(
        id_buku,
        judul if judul else None,
        penulis if penulis else None,
        stok
    ):
        print("Buku berhasil diperbarui.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan.")
        

def pinjam_buku():
    id_buku = input("Masukkan ID Buku yang ingin dipinjam: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ").strip()

    if not nama_peminjam:
        print("Nama peminjam tidak boleh kosong.")
        return

    hasil = daftar_buku.pinjam_buku(id_buku, nama_peminjam)
    if hasil is True:
        print("Buku berhasil dipinjam.")
    elif hasil is None:
        print("Stok buku habis.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan.")
        
        
def tampilkan_riwayat(status=None):
    daftar_buku.tampilkan_riwayat(status)
    
def hapus_buku():

    id_buku = input("Masukkan ID buku yang ingin dihapus: ")

    daftar_buku.hapus_buku(id_buku)
        
def kembalikan_buku():
    id_buku = input("Masukkan ID Buku yang ingin dikembalikan: ")

    if daftar_buku.kembalikan_buku(id_buku):
        print("Buku berhasil dikembalikan.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan atau belum dipinjam.")
        
def menu_utama():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Pinjam Buku")
        print("6. Kembalikan Buku")
        print("7. Lihat Semua Riwayat")
        print("8. Lihat Yang Masih Dipinjam")
        print("9. Lihat Yang Sudah Dikembalikan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            daftar_buku.tampilkan_buku()
        elif pilihan == "3":
            daftar_buku.tampilkan_buku()
            edit_buku()
        elif pilihan == "4":
            daftar_buku.tampilkan_buku()
            hapus_buku()
        elif pilihan == "5":
            daftar_buku.tampilkan_buku()
            pinjam_buku()
        elif pilihan == "6":
            kembalikan_buku()
        elif pilihan == "7":
            tampilkan_riwayat()
        elif pilihan == "8":
            tampilkan_riwayat("Dipinjam")
        elif pilihan == "9":
            tampilkan_riwayat("Dikembalikan")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid.")

# ini utama
if __name__ == "__main__":
    menu_utama()
