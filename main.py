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

    print("Data ditemukan. Masukkan data baru.")
    judul = input("Masukkan Judul Baru: ")
    penulis = input("Masukkan Penulis Baru: ")
    stok = int(input("Masukkan Stok Baru: "))

    if daftar_buku.edit_buku(id_buku, judul, penulis, stok):
        print("Buku berhasil diperbarui.")
    else:
        print("Buku dengan ID tersebut tidak ditemukan.")
        
        
def tampilkan_riwayat(status=None):
    pass
    
        
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
            edit_buku()
        # elif pilihan == "4":
        #     hapus_buku()
        # elif pilihan == "5":
        #     pinjam_buku()
        # elif pilihan == "6":
        #     kembalikan_buku()
        # elif pilihan == "7":
        #     tampilkan_riwayat()
        # elif pilihan == "8":
        #     tampilkan_riwayat("Dipinjam")
        # elif pilihan == "9":
        #     tampilkan_riwayat("Dikembalikan")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    menu_utama()