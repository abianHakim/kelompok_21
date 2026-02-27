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
        self.muat_dari_file()

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