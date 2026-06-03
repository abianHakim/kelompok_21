import os
import json


class NodeBuku:
    def __init__(self, id_buku, judul, penulis, stok):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
        self.next = None


class LinkedListBuku:
    def __init__(self):
        self.head = None
        self.path_file = "data/buku.json"
        self.path_riwayat = "data/riwayat.json"
        self.riwayat = []
        self.muat_dari_file()
        self.muat_riwayat_dari_file()

    # TAMBAH BUKU
    def tambah_buku(self, id_buku, judul, penulis, stok):

        id_buku = id_buku.upper()

        node_baru = NodeBuku(id_buku, judul, penulis, stok)

        if not self.head:
            self.head = node_baru
        else:
            sementara = self.head
            while sementara.next:
                sementara = sementara.next
            sementara.next = node_baru

        self.simpan_ke_file()

    # CARI BUKU BERDASARKAN ID
    def cari_buku(self, id_buku):
        id_buku = id_buku.upper()

        sementara = self.head

        while sementara:
            if sementara.id_buku == id_buku:
                return True
            sementara = sementara.next

        return False

    # AMBIL DATA BUKU BERDASARKAN ID
    def get_buku(self, id_buku):
        id_buku = id_buku.upper()

        sementara = self.head

        while sementara:
            if sementara.id_buku == id_buku:
                return sementara

            sementara = sementara.next

        return None

    # EDIT BUKU
    def edit_buku(self, id_buku, judul=None, penulis=None, stok=None):
        id_buku = id_buku.upper()
        sementara = self.head

        while sementara:
            if sementara.id_buku == id_buku:
                if judul is not None and judul != "":
                    sementara.judul = judul
                if penulis is not None and penulis != "":
                    sementara.penulis = penulis
                if stok is not None:
                    sementara.stok = stok
                self.simpan_ke_file()
                return True
            sementara = sementara.next

        return False

    # GENERATE ID PEMINJAMAN
    def generate_id_peminjaman(self):

        nomor = len(self.riwayat) + 1

        return f"P{nomor:03}"
    

    # CEK STOK BUKU
    def cek_stok_buku(self, id_buku):
        id_buku = id_buku.upper()

        sementara = self.head

        while sementara:
            if sementara.id_buku == id_buku:
                return sementara.stok

            sementara = sementara.next

        return None

    # PINJAM BUKU
    def pinjam_buku(self, id_buku, nama_peminjam):
        id_buku = id_buku.upper()
        nama_peminjam = nama_peminjam.lower()

        sementara = self.head

        while sementara:

            if sementara.id_buku == id_buku:

                if sementara.stok <= 0:
                    return None

                sementara.stok -= 1

                id_peminjaman = self.generate_id_peminjaman()

                self.riwayat.append({
                    "id_peminjaman": id_peminjaman,
                    "id_buku": sementara.id_buku,
                    "judul": sementara.judul,
                    "penulis": sementara.penulis,
                    "nama_peminjam": nama_peminjam,
                    "status": "Dipinjam"
                })

                self.simpan_ke_file()
                self.simpan_riwayat_ke_file()

                return id_peminjaman

            sementara = sementara.next

        return False
    
    # HAPUS BUKU
    def hapus_buku(self, id_buku):
        id_buku = id_buku.upper()

        if not self.head:
            print("Data buku kosong.")
            return False

        # jika yang dihapus adalah head
        if self.head.id_buku == id_buku:
            self.head = self.head.next
            self.simpan_ke_file()
            return True

        sebelumnya = self.head
        sekarang = self.head.next

        while sekarang:
            if sekarang.id_buku == id_buku:
                sebelumnya.next = sekarang.next
                self.simpan_ke_file()
                return True

            sebelumnya = sekarang
            sekarang = sekarang.next

        return False

    # TAMPILKAN BUKU
    def tampilkan_buku(self):
        if not self.head:
            print("Belum ada buku.")
            return

        print("\n=== DAFTAR BUKU ===")
        print("-" * 60)

        nomor = 1
        sementara = self.head

        while sementara:
            print(f"{nomor}. ID: {sementara.id_buku}")
            print(f"   Judul   : {sementara.judul}")
            print(f"   Penulis : {sementara.penulis}")
            print(f"   Stok    : {sementara.stok}")
            print("-" * 60)
            sementara = sementara.next
            nomor += 1

            # PROSES PENGEMBALIAN
    def proses_pengembalian(self):

        while True:

            print("\n=== PENGEMBALIAN BUKU ===")
            print("1. Gunakan ID Peminjaman")
            print("2. Gunakan Nama Peminjam")

            pilihan = input("Pilih opsi: ")

            # PENGEMBALIAN DENGAN ID
            if pilihan == "1":

                while True:

                    id_peminjaman = input(
                        "Masukkan ID Peminjaman (0 untuk kembali): "
                    ).upper()

                    if id_peminjaman == "0":
                        break

                    data = self.cari_peminjaman(id_peminjaman)

                    if data:
                        break

                    print("ID peminjaman tidak ditemukan.")

                if id_peminjaman == "0":
                    continue

            # PENGEMBALIAN DENGAN NAMA
            elif pilihan == "2":

                while True:

                    nama = input(
                        "Masukkan Nama Peminjam (0 untuk kembali): "
                    ).strip().lower()

                    if nama == "0":
                        break

                    daftar_pinjaman = self.cari_pinjaman_nama(nama)

                    if daftar_pinjaman:
                        break

                    print("Data peminjaman tidak ditemukan.")

                if nama == "0":
                    continue

                print("\n=== DAFTAR PINJAMAN ===")

                for item in daftar_pinjaman:
                    print(
                        f"{item['id_peminjaman']} - "
                        f"{item['judul']}"
                    )

                while True:

                    id_peminjaman = input(
                        "Masukkan ID Peminjaman (0 untuk kembali): "
                    ).upper()

                    if id_peminjaman == "0":
                        break

                    data = self.cari_peminjaman(id_peminjaman)

                    if data and data["nama_peminjam"] == nama:
                        break

                    print("ID peminjaman tidak sesuai.")

                if id_peminjaman == "0":
                    continue

            else:
                print("Pilihan tidak valid.")
                continue

            # KONFIRMASI
            print("\n=== DATA PEMINJAMAN ===")
            print(f"ID Peminjaman : {data['id_peminjaman']}")
            print(f"Judul Buku    : {data['judul']}")
            print(f"Nama Peminjam : {data['nama_peminjam']}")

            print("\n1. Setuju")
            print("2. Batal")

            konfirmasi = input("Pilih opsi: ")

            if konfirmasi == "1":

                if self.kembalikan_buku(
                    data["id_peminjaman"]
                ):
                    print("Buku berhasil dikembalikan.")

                return

            elif konfirmasi == "2":
                print("Pengembalian dibatalkan.")
                return

            else:
                print("Pilihan tidak valid.")

        # CARI PEMINJAMAN BERDASARKAN ID
    def cari_peminjaman(self, id_peminjaman):

        id_peminjaman = id_peminjaman.upper()

        for item in self.riwayat:

            if (
                item["id_peminjaman"] == id_peminjaman
                and item["status"] == "Dipinjam"
            ):
                return item

        return None
    
    # CARI PINJAMAN BERDASARKAN NAMA
    def cari_pinjaman_nama(self, nama):

        nama = nama.lower()

        hasil = []

        for item in self.riwayat:

            if (
                item["nama_peminjam"] == nama
                and item["status"] == "Dipinjam"
            ):
                hasil.append(item)

        return hasil

        # logika pegenmablian buku
    def kembalikan_buku(self, id_peminjaman):

        id_peminjaman = id_peminjaman.upper()

        for item in self.riwayat:

            if (
                item["id_peminjaman"] == id_peminjaman
                and item["status"] == "Dipinjam"
            ):

                sementara = self.head
                while sementara:
                    if sementara.id_buku == item["id_buku"]:

                        sementara.stok += 1
                        item["status"] = "Dikembalikan"

                        self.simpan_ke_file()
                        self.simpan_riwayat_ke_file()

                        return True

                    sementara = sementara.next
        return False

    # TAMPILKAN RIWAYAT
    def tampilkan_riwayat(self, status=None):
        if not self.riwayat:
            print("Belum ada riwayat peminjaman.")
            return

        ditemukan = False
        print("-" * 60)

        for i, item in enumerate(self.riwayat, start=1):
            # Filter berdasarkan status jika diberikan
            if status is None or item["status"] == status:
                ditemukan = True
                print(f"{i}. ID Buku       : {item['id_buku']}")

                if "judul" in item:
                    print(f"   Judul         : {item['judul']}")

                if "penulis" in item:
                    print(f"   Penulis       : {item['penulis']}")

                if "nama_peminjam" in item:
                    print(f"   Nama Peminjam : {item['nama_peminjam']}")

                print(f"   Status        : {item['status']}")
                print("-" * 60)

        if not ditemukan:
            print("Data riwayat tidak ditemukan.")
            print("-" * 60)
    # File Handling
    # SIMPAN KE JSON
    def simpan_ke_file(self):
        os.makedirs("data", exist_ok=True)

        data = []
        sementara = self.head

        while sementara:
            data.append({
                "id_buku": sementara.id_buku,
                "judul": sementara.judul,
                "penulis": sementara.penulis,
                "stok": sementara.stok
            })
            sementara = sementara.next

        with open(self.path_file, "w") as file:
            json.dump(data, file, indent=4)
    # FIle Handling
    # MUAT DARI JSON 
    def muat_dari_file(self):
        if not os.path.exists(self.path_file):
            return

        if os.path.getsize(self.path_file) == 0:
            return  # file kosong → abaikan

        with open(self.path_file, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return

        for item in data:
            node_baru = NodeBuku(
                item["id_buku"],
                item["judul"],
                item["penulis"],
                item["stok"]
            )

            if not self.head:
                self.head = node_baru
            else:
                sementara = self.head
                while sementara.next:
                    sementara = sementara.next
                sementara.next = node_baru

    # SIMPAN RIWAYAT KE JSON
    # Digunakan untuk menyimpan data riwayat peminjaman ke file riwayat.json
    def simpan_riwayat_ke_file(self):
        os.makedirs("data", exist_ok=True)

        with open(self.path_riwayat, "w") as file:
            json.dump(self.riwayat, file, indent=4)

    # MUAT RIWAYAT DARI JSON
    # Digunakan untuk membaca riwayat peminjaman saat program dijalankan
    def muat_riwayat_dari_file(self):
        if not os.path.exists(self.path_riwayat):
            return

        if os.path.getsize(self.path_riwayat) == 0:
            return

        with open(self.path_riwayat, "r") as file:
            try:
                self.riwayat = json.load(file)
            except json.JSONDecodeError:
                self.riwayat = []
