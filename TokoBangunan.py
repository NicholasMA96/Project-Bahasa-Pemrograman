# Daftar harga barang di toko bangunan
# simpan dalam format Dictionary agar mudah dipanggil harganya
daftar_harga = [
    {"Nama" : "Semen", "Harga" : 65000, "Stok" : 50},
    {"Nama" : "Paku", "Harga" : 15000, "Stok" : 50},
    {"Nama" : "Cat", "Harga" : 120000, "Stok" : 50},
    {"Nama" : "Pipa", "Harga" : 25000, "Stok" : 50},
    {"Nama" : "Pasir", "Harga" : 200000, "Stok" : 50}
    ]

riwayat = []

fitur = ["Lihat daftar", "Kasir", "Tambah stok", "Ubah Harga", "Lihat Riwayat", "Keluar"]

def lihat_stok():
    print("Menu Barang & Harga:")
# Menampilkan daftar barang yang tersedia
    for item in daftar_harga:
        print(f"Barang : {item['Nama']}: Rp{item['Harga']} stok : {item['Stok']}")

def kasir():
    print("Transaksi Kasir")
    nama_beli = input("Masukan Nama Barang Yang Ingin Dibeli = ").capitalize()
    for item in daftar_harga:
        if item["Nama"] == nama_beli:
            jumlah = int(input(f"Berapa Banyak {nama_beli} Yang Ingin Dibeli? : "))
            
            if item["Stok"]>= jumlah:
                total = item["Harga"] * jumlah
                print(f"Total Bayar : Rp{total}")
                
                uang = int(input("Masukan Uang Pembeli : Rp"))
                if uang >= total:
                    item["Stok"] -= jumlah
                    kembalian = uang - total
                    print (f"Kembalian : {uang-total}")
                    print (f"Transaksi Berhasil")
                    
                    riwayat.append({
                        "No"        : len(riwayat) + 1,
                        "Barang"    : nama_beli,
                        "Jumlah"    : jumlah,
                        "Total"     : total,
                        
                        "Kembalian" : kembalian
                    })
                else:
                    print(f"GAGAL: Uang Anda kurang")
            
            else:
                print (f"GAGAL: Stok tersisa {item['Stok']}")
            return
    print ("GAGAL: Barang Tidak Tersedia Di Toko")
        
def tambah_stok():
    print ("Menambah Stok Barang")
    nama_tambah = input("Masukan Nama Barang Yang Datang = ").capitalize()
    
    for item in daftar_harga:
        if item["Nama"] == nama_tambah:
            jumlah_masuk = int(input("Masukan Jumlah Barang Yang Datang = "))
            item["Stok"] += jumlah_masuk
            print (f"BERHASIL: Stok {nama_tambah} sekarang {item['Stok']}.")
            return
    print ("GAGAL: Barang Tidak Ditemukan")
    
def lihat_riwayat():
    print("Riwayat Transaksi:")
    if not riwayat:
        print("Belum ada transaksi.")
        return
    
    for transaksi in riwayat:
        print(f"  [{transaksi['No']}] {transaksi['Barang']} x{transaksi['Jumlah']}"
              f" | Total: Rp{transaksi['Total']} | Kembalian: Rp{transaksi['Kembalian']}")
        
    total_pemasukan = sum(t["Total"] for t in riwayat) #total_pemasukan = 0
    print (f"Total Pemasukan : Rp.{total_pemasukan}")  #for t in riwayat:
                                                            #total_pemasukan += t["Total"]
                                                            
def ubah_harga():
    print("Ubah Harga Barang")
    lihat_stok()
    nama_ubah = input("Masukan Nama Barang Yang Ingin Diubah Harganya = ").capitalize()

    for item in daftar_harga:
        if item["Nama"] == nama_ubah:
            print(f"Harga {nama_ubah} saat ini : Rp{item['Harga']}")
            harga_baru = int(input(f"Masukan Harga Baru {nama_ubah} = Rp"))
            item["Harga"] = harga_baru
            print(f"BERHASIL: Harga {nama_ubah} sekarang Rp{item['Harga']}")
            return
    print("GAGAL: Barang Tidak Ditemukan")
    
    
while True:
    for i, nama_menu in enumerate(fitur, start=1):
        print (f"{i}. {nama_menu}")
        
    try:
        pilih = int(input("Masukan Fitur yang ingin dijalankan = "))
        match pilih:
            case 1:
                lihat_stok()

            case 2:
                kasir()
    
            case 3:
                tambah_stok()
                
            case 4:
                ubah_harga()
            
            case 5:
                lihat_riwayat()
        
            case 6:
                print ("Sistem Selesai. Terima Kasih")
                break
            case _:
                print("Pilihan Tidak Tersedia")
    except ValueError:
        print ("Harus Input Angka")
    