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
        node_baru = NodeBuku(id_buku, judul, penulis, stok)

        if not self.head:
            self.head = node_baru
        else:
            sementara = self.head
            while sementara.next:
                sementara = sementara.next
            sementara.next = node_baru

        self.simpan_ke_file()

    # EDIT BUKU
    def edit_buku(self, id_buku, judul, penulis, stok):
        sementara = self.head
        
        while sementara:
            if sementara.id_buku == id_buku:
                sementara.judul = judul
                sementara.penulis = penulis
                sementara.stok = stok
                self.simpan_ke_file()  # simpan setelah edit
                return True
            sementara = sementara.next
        
        return False
    
    # HAPUS BUKU
    def hapus_buku(self, id_buku):
        if not self.head:
            print("data buku kosong")
            return
        
        # Jika yang di hapus adalah head
        if self.head.id_buku == id_buku:
            self.head = self.head.next
            self.simpan_ke_file()
            print("Buku berhasil Dihapus")
            return
        
        # cari node yang mau dihapus
        sebelumnya = self.head
        sekarang = self.head.next

        while sekarang:
            if sekarang.id_buku == id_buku:
                sebelumnya.next = sekarang.next
                self.simpan_ke_file()
                print("buku berhasil dihapus")
                return
            sebelumnya = sekarang
            sekarang = sekarang.next

        print("buku tidak ditemukan")

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

    # KEMBALIKAN BUKU
    def kembalikan_buku(self, id_buku):
        sementara = self.head

        while sementara:
            if sementara.id_buku == id_buku:
                # Mencari riwayat peminjaman terakhir dengan status "Dipinjam"
                for item in reversed(self.riwayat):
                    if item["id_buku"] == id_buku and item["status"] == "Dipinjam":
                        item["status"] = "Dikembalikan"  # ubah status
                        sementara.stok += 1              # tambah stok buku
                        self.simpan_ke_file()            # simpan perubahan buku
                        self.simpan_riwayat_ke_file()    # simpan perubahan riwayat
                        return True
                return False
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