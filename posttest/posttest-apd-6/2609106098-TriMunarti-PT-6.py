database_user = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

database_karyawan = {
    "K01": {"nama": "Beni", "gol": "A", "hadir": 0, "alpa": 0, "lembur": 0, "gaji_bersih": 0},
    "K02": {"nama": "Siti", "gol": "B", "hadir": 0, "alpa": 0, "lembur": 0, "gaji_bersih": 0},
    "K03": {"nama": "Rian", "gol": "C", "hadir": 0, "alpa": 0, "lembur": 0, "gaji_bersih": 0}
}

def menu_login():
    print("\n" + "="*30)
    print("=== LOGIN & REGISTER SISTEM ===")
    print("="*30)
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

def main():
    while True:
        pilihan = menu_login()
        
        if pilihan == "1":
            print("\n--- LOGIN AKUN ---")
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            
            if username in database_user and database_user[username]["password"] == password:
                role = database_user[username]["role"]
                print(f"\n[SUKSES] Berhasil login sebagai {role.upper()}!")
                
                while True:
                    if role == "admin":
                        print("\n" + "="*30)
                        print("--- MENU UTAMA ADMIN ---")
                        print("="*30)
                        print("1. Tambah Data Karyawan (Create)")
                        print("2. Input Absensi & Hitung Gaji (Update)")
                        print("3. Tampilkan Rekap Gaji (Read)")
                        print("4. Hapus Data Karyawan (Delete)")
                        print("5. Logout")
                        pilih_admin = input("Pilih menu admin (1-5): ")
                        
                        if pilih_admin == "1":
                            print("\n--- TAMBAH KARYAWAN ---")
                            id_kar = input("Masukkan ID Karyawan (Contoh: K04): ")
                            if id_kar in database_karyawan:
                                print("[ERROR] ID Karyawan sudah terdaftar!")
                            else:
                                nama = input("Masukkan Nama Karyawan: ")
                                gol = input("Masukkan Golongan (A/B/C): ").upper()
                                database_karyawan[id_kar] = {
                                    "nama": nama, "gol": gol, 
                                    "hadir": 0, "alpa": 0, "lembur": 0, "gaji_bersih": 0
                                }
                                print(f"[SUKSES] Karyawan '{nama}' berhasil ditambahkan!")
                                
                        elif pilih_admin == "2":
                            print("\n--- INPUT ABSENSI & HITUNG GAJI ---")
                            if len(database_karyawan) == 0:
                                print("[INFO] Belum ada data karyawan.")
                            else:
                                id_cari = input("Masukkan ID Karyawan yang ingin diupdate: ")
                                if id_cari in database_karyawan:
                                    hadir_str = input("Masukkan jumlah hadir: ")
                                    alpa_str = input("Masukkan jumlah alpa: ")
                                    lembur_str = input("Masukkan jumlah lembur (jam): ")
                                    
                                    if hadir_str.isdigit() and alpa_str.isdigit() and lembur_str.isdigit():
                                        hadir = int(hadir_str)
                                        alpa = int(alpa_str)
                                        lembur = int(lembur_str)
                                        
                                        gol = database_karyawan[id_cari]["gol"]
                                        if gol == "A":
                                            gaji_pokok = 4000000
                                            tunjangan = 500000
                                        elif gol == "B":
                                            gaji_pokok = 3000000
                                            tunjangan = 300000
                                        else:
                                            gaji_pokok = 2000000
                                            tunjangan = 200000
                                            
                                        gaji_bersih = gaji_pokok + tunjangan + (lembur * 50000) - (alpa * 100000)
                                        if gaji_bersih < 0:
                                            gaji_bersih = 0
                                            
                                        database_karyawan[id_cari]["hadir"] = hadir
                                        database_karyawan[id_cari]["alpa"] = alpa
                                        database_karyawan[id_cari]["lembur"] = lembur
                                        database_karyawan[id_cari]["gaji_bersih"] = gaji_bersih
                                        
                                        print(f"[SUKSES] Data absensi dan gaji untuk {database_karyawan[id_cari]['nama']} berhasil diperbarui!")
                                    else:
                                        print("[ERROR] Input kehadiran, alpa, dan lembur harus berupa angka!")
                                else:
                                    print("[ERROR] ID Karyawan tidak ditemukan!")
                                    
                        elif pilih_admin == "3":
                            print("\n" + "="*65)
                            print(f"{'REKAPITULASI GAJI KARYAWAN (ADMIN)':^65}")
                            print("="*65)
                            if len(database_karyawan) == 0:
                                print("Belum ada data karyawan.")
                            else:
                                print(f"{'ID':<6} | {'Nama':<10} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<6} | {'Lembur':<6} | {'Gaji Bersih':<10}")
                                print("-" * 65)
                                for id_kar, k in database_karyawan.items():
                                    print(f"{id_kar:<6} | {k['nama']:<10} | {k['gol']:<4} | {k['hadir']:<6} | {k['alpa']:<6} | {k['lembur']:<6} | Rp{k['gaji_bersih']:<8}")
                            print("="*65)
                            
                        elif pilih_admin == "4":
                            print("\n--- HAPUS DATA KARYAWAN ---")
                            if len(database_karyawan) == 0:
                                print("[INFO] Belum ada data karyawan.")
                            else:
                                id_hapus = input("Masukkan ID Karyawan yang akan dihapus: ")
                                if id_hapus in database_karyawan:
                                    del database_karyawan[id_hapus]
                                    print(f"[SUKSES] Data karyawan dengan ID {id_hapus} berhasil dihapus!")
                                else:
                                    print("[ERROR] ID Karyawan tidak ditemukan!")
                                    
                        elif pilih_admin == "5":
                            print("[INFO] Logout berhasil.")
                            break
                        else:
                            print("[ERROR] Pilihan menu admin tidak valid!")
                            
                    elif role == "user":
                        print("\n" + "="*30)
                        print("--- MENU UTAMA USER ---")
                        print("="*30)
                        print("1. Tampilkan Rekap Gaji (Read)")
                        print("2. Logout")
                        pilih_user = input("Pilih menu user (1-2): ")
                        
                        if pilih_user == "1":
                            print("\n" + "="*65)
                            print(f"{'REKAPITULASI GAJI KARYAWAN (USER)':^65}")
                            print("="*65)
                            if len(database_karyawan) == 0:
                                print("Belum ada data karyawan.")
                            else:
                                print(f"{'ID':<6} | {'Nama':<10} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<6} | {'Lembur':<6} | {'Gaji Bersih':<10}")
                                print("-" * 65)
                                for id_kar, k in database_karyawan.items():
                                    print(f"{id_kar:<6} | {k['nama']:<10} | {k['gol']:<4} | {k['hadir']:<6} | {k['alpa']:<6} | {k['lembur']:<6} | Rp{k['gaji_bersih']:<8}")
                            print("="*65)
                            
                        elif pilih_user == "2":
                            print("[INFO] Logout berhasil.")
                            break
                        else:
                            print("[ERROR] Pilihan menu user tidak valid!")
            else:
                print("\n[ERROR] Username atau password salah!")
                
        elif pilihan == "2":
            print("\n--- REGISTER AKUN BARU ---")
            new_user = input("Buat Username baru: ")
            if new_user in database_user:
                print("[ERROR] Username sudah terdaftar, silakan gunakan username lain.")
            else:
                new_pass = input("Buat Password baru: ")
                database_user[new_user] = {"password": new_pass, "role": "user"}
                print(f"[SUKSES] Akun dengan username '{new_user}' berhasil didaftarkan! Silakan login.")
                
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program ini. Keluar program...")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1 sampai 3.")

if __name__ == "__main__":
    main()