from datetime import datetime

class TokoMaterial:
    
    def __init__(self):
        self.daftar_harga = [
            {"Nama" : "Semen", "Harga" : 65000,  "Stok" : 50},
            {"Nama" : "Paku",  "Harga" : 15000,  "Stok" : 50},
            {"Nama" : "Cat",   "Harga" : 120000, "Stok" : 50},
            {"Nama" : "Pipa",  "Harga" : 25000,  "Stok" : 50},
            {"Nama" : "Pasir", "Harga" : 200000, "Stok" : 50}
        ]
        self.riwayat = []
        self.fitur = ["Lihat daftar", "Kasir", "Tambah stok", "Ubah Harga", "Lihat Riwayat", "Keluar"]

    def lihat_stok(self):
        print("Menu Barang & Harga:")
        for item in self.daftar_harga:
            print(f"Barang : {item['Nama']}: Rp{item['Harga']} stok : {item['Stok']}")

    def kasir(self):
        print("Transaksi Kasir")

        while True:
            nama_beli = input("Masukan Nama Barang Yang Ingin Dibeli = ").capitalize()
            barang_ditemukan = None

            for item in self.daftar_harga:
                if item["Nama"] == nama_beli:
                    barang_ditemukan = item
                    break

            if barang_ditemukan:
                break
            else:
                print(f"Barang '{nama_beli}' tidak ditemukan, silakan coba lagi!")
                self.lihat_stok()

        while True:
            try:
                jumlah = int(input(f"Berapa Banyak {nama_beli} Yang Ingin Dibeli? : "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                elif jumlah > barang_ditemukan["Stok"]:
                    print(f"GAGAL: Stok tersisa {barang_ditemukan['Stok']}")
                else:
                    break
            except ValueError:
                print("Jumlah harus berupa angka!")

        total = barang_ditemukan["Harga"] * jumlah
        print(f"Total Bayar : Rp{total}")

        while True:
            try:
                uang = int(input("Masukan Uang Pembeli : Rp"))
                if uang <= 0:
                    print("Uang harus lebih dari 0!")
                elif uang < total:
                    print(f"GAGAL: Uang Anda kurang Rp{total - uang}")
                else:
                    break
            except ValueError:
                print("Nominal uang harus berupa angka!")

        barang_ditemukan["Stok"] -= jumlah
        kembalian = uang - total
        print(f"Kembalian : Rp{kembalian}")
        print(f"Transaksi Berhasil")

        self.riwayat.append({
            "No"       : len(self.riwayat) + 1,
            "Barang"   : nama_beli,
            "Jumlah"   : jumlah,
            "Total"    : total,
            "Kembalian": kembalian,
            "Waktu"    : datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

    def tambah_stok(self):
        print("Menambah Stok Barang")

        while True:
            nama_tambah = input("Masukan Nama Barang Yang Datang = ").capitalize()
            barang_ditemukan = None

            for item in self.daftar_harga:
                if item["Nama"] == nama_tambah:
                    barang_ditemukan = item
                    break

            if barang_ditemukan:
                break
            else:
                print(f"Barang '{nama_tambah}' tidak ditemukan, silakan coba lagi!")
                self.lihat_stok()

        while True:
            try:
                jumlah_masuk = int(input("Masukan Jumlah Barang Yang Datang = "))
                if jumlah_masuk <= 0:
                    print("Jumlah harus lebih dari 0!")
                else:
                    break
            except ValueError:
                print("Jumlah harus berupa angka!")

        barang_ditemukan["Stok"] += jumlah_masuk
        print(f"BERHASIL: Stok {nama_tambah} sekarang {barang_ditemukan['Stok']}.")

    def lihat_riwayat(self):
        print("Riwayat Transaksi:")
        if not self.riwayat:
            print("Belum ada transaksi.")
            return

        for transaksi in self.riwayat:
            print(f"  [{transaksi['No']}] {transaksi['Barang']} x{transaksi['Jumlah']}"
                  f" | Total: Rp{transaksi['Total']} | Kembalian: Rp{transaksi['Kembalian']}"
                  f" | Waktu: {transaksi['Waktu']}")

        total_pemasukan = sum(t["Total"] for t in self.riwayat)
        print(f"Total Pemasukan : Rp{total_pemasukan}")

    def ubah_harga(self):
        print("Ubah Harga Barang")
        self.lihat_stok()

        while True:
            nama_ubah = input("Masukan Nama Barang Yang Ingin Diubah Harganya = ").capitalize()
            barang_ditemukan = None

            for item in self.daftar_harga:
                if item["Nama"] == nama_ubah:
                    barang_ditemukan = item
                    break

            if barang_ditemukan:
                break
            else:
                print(f"Barang '{nama_ubah}' tidak ditemukan, silakan coba lagi!")
                self.lihat_stok()

        print(f"Harga {nama_ubah} saat ini : Rp{barang_ditemukan['Harga']}")

        while True:
            try:
                harga_baru = int(input(f"Masukan Harga Baru {nama_ubah} = Rp"))
                if harga_baru <= 0:
                    print("Harga harus lebih dari 0!")
                else:
                    break
            except ValueError:
                print("Harga harus berupa angka!")

        barang_ditemukan["Harga"] = harga_baru
        print(f"BERHASIL: Harga {nama_ubah} sekarang Rp{barang_ditemukan['Harga']}")

    def jalankan(self):
        while True:
            print(f"\nSistem Kasir Toko Bangunan")
            print(f"Tanggal : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
            for i, nama_menu in enumerate(self.fitur, start=1):
                print(f"{i}. {nama_menu}")

            try:
                pilih = int(input("Masukan Fitur yang ingin dijalankan = "))
                match pilih:
                    case 1: self.lihat_stok()
                    case 2: self.kasir()
                    case 3: self.tambah_stok()
                    case 4: self.ubah_harga()
                    case 5: self.lihat_riwayat()
                    case 6:
                        print("Sistem Selesai. Terima Kasih")
                        break
                    case _:
                        print("Pilihan Tidak Tersedia")
            except ValueError:
                print("Harus Input Angka")

toko = TokoMaterial()
toko.jalankan()