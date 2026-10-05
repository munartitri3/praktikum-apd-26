# Setup data kredensial valid (Atur sesuai data Anda)
NAMA_VALID = "Budi"
NIM_VALID = "123"  # 2 atau 3 digit terakhir

# 1. Validasi Login
print("="*35)
print("     RENTAL PS LOGIN SYSTEM     ")
print("="*35)
nama = input("Tri: ")
nim = input("98: ")

# Percabangan Validasi
if nama != NAMA_VALID or nim != NIM_VALID:
    print("\nLogin Gagal! Nama atau NIM salah. Program Berhenti.")
else:
    print(f"\nLogin Berhasil! Selamat datang, {nama}.")
    
    # 2. Pilihan Jenis Konsol
    print("\n" + "="*35)
    print("      MENU PILIHAN KONSOL      ")
    print("="*35)
    print("1. PS4     : Rp 10.000 / Jam")
    print("2. PS4 Pro : Rp 15.000 / Jam")
    print("3. PS5     : Rp 20.000 / Jam")
    print("="*35)
    
    pilihan_konsol = input("Pilih Konsol (1-3): ")
    
    # Menentukan Tarif berdasarkan Pilihan
    if pilihan_konsol == '1':
        harga_per_jam = 10000
        nama_konsol = "PS4"
    elif pilihan_konsol == '2':
        harga_per_jam = 15000
        nama_konsol = "PS4 Pro"
    elif pilihan_konsol == '3':
        harga_per_jam = 20000
        nama_konsol = "PS5"
    else:
        harga_per_jam = 0 # Penanda pilihan salah
        nama_konsol = ""
    
    # Percabangan Validasi Pilihan Konsol
    if harga_per_jam == 0:
        print("\nPilihan Tidak Valid! Program Berhenti.")
    else:
        # Lanjut jika pilihan valid
        jam_sewa = int(input("\nSewa berapa jam? : "))
        
        # 3. Ketentuan Diskon Durasi
        if jam_sewa >= 5:
            persen_diskon = 0.08
            nama_diskon = "8%"
        elif jam_sewa >= 3:
            persen_diskon = 0.05
            nama_diskon = "5%"
        else:
            persen_diskon = 0.0
            nama_diskon = "0%"
            
        # Poin Plus (+): Tambahan Biaya Weekend
        print("\nWaktu sewa (Weekend / Weekday)?")
        print("1. Weekday (Senin-Jumat)")
        print("2. Weekend (Sabtu-Minggu)")
        pilihan_hari = input("Masukkan pilihan (1-2): ")
        
        # Menentukan Tambahan Weekend
        if pilihan_hari == '2':
            persen_weekend = 0.10
            status_hari = "Weekend (Tambahan 10%)"
        else:
            persen_weekend = 0.0
            status_hari = "Weekday (Normal)"
            
        # 4. Perhitungan Akhir Berdasarkan Rumus
        # Hitung masing-masing bagian dulu dari total harga awal
        total_harga = harga_per_jam * jam_sewa
        nominal_diskon = total_harga * persen_diskon
        nominal_weekend = total_harga * persen_weekend
        
        # Total bayar = total harga - potongan diskon + tambahan weekend
        total_bayar = total_harga - nominal_diskon + nominal_weekend
        
        # 5. Menampilkan Output Rapi (Tanpa Library Tambahan)
        print("\n" + "="*40)
        print("          NOTA TRANSAKSI SEWA PS        ")
        print("="*40)
        print(f"Nama Penyewa  : {nama}")
        print(f"NIM Penyewa   : {nim}")
        print(f"Jenis Konsol  : {nama_konsol}")
        print(f"Durasi Sewa   : {jam_sewa} Jam")
        print(f"Waktu Sewa    : {status_hari}")
        print("-" * 40)
        # Menggunakan formatting :.0f untuk menghilangkan desimal dan :; untuk pemisah ribuan
        print(f"TOTAL AWAL    : Rp {total_harga:,.0f}")
        print(f"Diskon {nama_diskon}      : Rp {nominal_diskon:,.0f} (-)")
        print(f"Extra Weekend : Rp {nominal_weekend:,.0f} (+)")
        print("-" * 40)
        print(f"TOTAL BAYAR   : Rp {total_bayar:,.0f}")
        print("="*40)
        