# Sistem Penggajian & Absensi Karyawan (Procedural Style)

    {
        "id": "K01",
        "nama": "Beni",
        "gol": "A",
        "gaji_pokok": 4000000,
        "tunjangan": 1000000,
        "hadir": 20,
        "alpa": 0,
        "lembur": 5,
        "gaji_bersih": 5250000
    },
    {
        "id": "K02",
        "nama": "Siti",
        "gol": "B",
        "gaji_pokok": 6000000,
        "tunjangan": 2000000,
        "hadir": 18,
        "alpa": 2,
        "lembur": 3,
        "gaji_bersih": 7950000
    },
    {
        "id": "K03",
        "nama": "Rian",
        "gol": "C",
        "gaji_pokok": 8500000,
        "tunjangan": 3500000,
        "hadir": 22,
        "alpa": 0,
        "lembur": 10,
        "gaji_bersih": 12500000
    }
]

print("=== SISTEM PENGGAJIAN & ABSENSI KARYAWAN ===")

while True:
    print("\nMENU UTAMA:")
    print("1. Tambah Data Karyawan Baru (Create)")
    print("2. Input Absensi & Hitung Gaji (Update)")
    print("3. Tampilkan Daftar & Rekap Gaji (Read)")
    print("4. Hapus Data Karyawan (Delete)")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        print("\n--- Tambah Karyawan Baru (Create) ---")
        id_kar = input("Masukkan ID Karyawan (Contoh K04): ")
        nama = input("Masukkan Nama Lengkap: ")
        
        print("Pilih Golongan:")
        print("  A. Gaji Pokok Rp 4.000.000 (Tunjangan Rp 1.000.000)")
        print("  B. Gaji Pokok Rp 6.000.000 (Tunjangan Rp 2.000.000)")
        print("  C. Gaji Pokok Rp 8.500.000 (Tunjangan Rp 3.500.000)")
        gol = input("Masukkan Golongan (A/B/C): ").upper()
        
        if gol == "A":
            gaji_pokok = 4000000
            tunjangan = 1000000
        elif gol == "B":
            gaji_pokok = 6000000
            tunjangan = 2000000
        elif gol == "C":
            gaji_pokok = 8500000
            tunjangan = 3500000
        else:
            print("Golongan tidak valid! Otomatis diset ke Golongan A.")
            gol = "A"
            gaji_pokok = 4000000
            tunjangan = 1000000
            
        data_baru = {
            "id": id_kar,
            "nama": nama,
            "gol": gol,
            "gaji_pokok": gaji_pokok,
            "tunjangan": tunjangan,
            "hadir": 0,
            "alpa": 0,
            "lembur": 0,
            "gaji_bersih": gaji_pokok + tunjangan
        }
        
        database_karyawan.append(data_baru)
        print(f"Sukses! Karyawan {nama} berhasil disimpan.")

    elif pilihan == "2":
        print("\n--- Input Absensi & Hitung Gaji (Update) ---")
        if len(database_karyawan) == 0:
            print("Belum ada data karyawan!")
            continue
            
        id_cari = input("Masukkan ID Karyawan yang ingin di-input (misal: K01, K02, K03): ")
        
        ketemu = False
        for karyawan in database_karyawan:
            if karyawan["id"] == id_cari:
                ketemu = True
                print(f"Karyawan Ditemukan: {karyawan['nama']}")
                
                try:
                    hadir = int(input("Jumlah Masuk Hadir (hari): "))
                    alpa = int(input("Jumlah Tanpa Keterangan/Alpa (hari): "))
                    lembur = int(input("Total Jam Lembur: "))
                except ValueError:
                    print("Input harus berupa angka bulat! Proses dibatalkan.")
                    break
                
                tarif_lembur = 50000   
                potongan_alpa = 100000 
                
                total_lembur = lembur * tarif_lembur
                total_potongan = alpa * potongan_alpa
                
                gaji_kotor = karyawan["gaji_pokok"] + karyawan["tunjangan"] + total_lembur
                gaji_bersih = gaji_kotor - total_potongan
                
                if gaji_bersih < 0:
                    gaji_bersih = 0
                    
                karyawan["hadir"] = hadir
                karyawan["alpa"] = alpa
                karyawan["lembur"] = lembur
                karyawan["gaji_bersih"] = gaji_bersih
                
                print("\n[BERHASIL] Absensi & perhitungan gaji telah diperbarui!")
                print(f"Total Gaji Bersih untuk {karyawan['nama']} adalah: Rp {gaji_bersih:,.0f}")
                break
                
        if not ketemu:
            print(f"Maaf, Karyawan dengan ID '{id_cari}' tidak ditemukan.")

    elif pilihan == "3":
        print("\n" + "="*85)
        print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (Read)':^85}")
        print("="*85)
        print(f"{'ID':<6} | {'Nama Karyawan':<18} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<15}")
        print("-" * 85)
        
        if len(database_karyawan) == 0:
            print(f"{'Belum ada data karyawan yang tersimpan.':^85}")
        else:
            for k in database_karyawan:
                print(f"{k['id']:<6} | {k['nama']:<18} | {k['gol']:<4} | {k['hadir']:<6} | {k['alpa']:<5} | {k['lembur']:<8} jam | Rp {k['gaji_bersih']:,.0f}")
                
        print("="*85)

    elif pilihan == "4":
        print("\n--- Hapus Data Karyawan (Delete) ---")
        if len(database_karyawan) == 0:
            print("Belum ada data karyawan!")
            continue
            
        id_hapus = input("Masukkan ID Karyawan yang ingin dihapus: ")
        ketemu = False
        for i, k in enumerate(database_karyawan):
            if k["id"] == id_hapus:
                ketemu = True
                database_karyawan.pop(i)
                print(f"[BERHASIL] Data karyawan {k['nama']} telah dihapus dari sistem.")
                break
        if not ketemu:
            print(f"Karyawan dengan ID '{id_hapus}' tidak ditemukan.")

    elif pilihan == "5":
        print("Keluar dari program. Terima kasih!")
        break
        
    else:
        print("Pilihan menu tidak valid! Silakan masukkan angka 1 sampai 5.")