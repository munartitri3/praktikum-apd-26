import os

database_user = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

database_karyawan = {
    "K01": {"nama": "Beni", "gol": "A", "hadir": 20, "alpa": 0, "lembur": 5, "gaji_bersih": 5250000},
    "K02": {"nama": "Siti", "gol": "B", "hadir": 18, "alpa": 2, "lembur": 3, "gaji_bersih": 7950000},
    "K03": {"nama": "Rian", "gol": "C", "hadir": 22, "alpa": 0, "lembur": 10, "gaji_bersih": 12500000}
}

status_program = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_gaji_bersih(gol, hadir, alpa, lembur):
    gaji_pokok = 4000000
    tunjangan = 1000000
    tarif_lembur = 50000
    potongan_per_alpa = 100000

    if gol == 'B':
        gaji_pokok = 6000000
        tunjangan = 2000000
    elif gol == 'C':
        gaji_pokok = 8500000
        tunjangan = 3500000
    
    total_lembur = lembur * tarif_lembur
    total_potongan = alpa * potongan_per_alpa
    gaji_kotor = gaji_pokok + tunjangan + total_lembur
    gaji_bersih_val = gaji_kotor - total_potongan

    if gaji_bersih_val < 0:
        gaji_bersih_val = 0
    return gaji_bersih_val

def cek_id_karyawan(id_kry, db):
    return id_kry in db

def tampilkan_header_utama():
    return "SISTEM PENGGAJIAN & ABSENSI KARYAWAN"

def ambil_info_versi():
    return "Posttest 6 - Praktikum APD"

def cetak_tabel_karyawan(db):
    print("="*90)
    print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN':^90}")
    print("="*90)
    print(f"{'ID':<6} | {'Nama Karyawan':<20} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<18}")
    print("-" * 90)
    if len(db) == 0:
        print(f"{'Belum ada data karyawan yang tersimpan.':^90}")
    else:
        for k, v in db.items():
            gaji_f = f"Rp {v['gaji_bersih']:,}"
            print(f"{k:<6} | {v['nama']:<20} | {v['gol']:<4} | {v['hadir']:<6} | {v['alpa']:<5} | {v['lembur']:<8} | {gaji_f:<18}")
    print("="*90)

def tampilkan_pesan_penutup():
    print("\nKeluar dari program. Terima kasih!")

def hitung_bonus_rekursif(hari):
    bonus_per_hari = 10000
    if hari <= 0:
        return 0
    else:
        return bonus_per_hari + hitung_bonus_rekursif(hari - 1)

while status_program:
    clear_screen()
    print("="*45)
    print(f"{tampilkan_header_utama():^45}")
    print(f"{ambil_info_versi():^45}")
    print("="*45)
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    
    try:
        pilihan_utama = int(input("Pilih menu (1-3): "))
    except ValueError:
        print("[ERROR] Masukkan angka yang valid (1-3)!")
        input("\nTekan Enter untuk melanjutkan...")
        continue

    if pilihan_utama == 1:
        clear_screen()
        print("--- MENU LOGIN ---")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        if username in database_user and database_user[username]["password"] == password:
            role = database_user[username]["role"]
            print(f"\n[BERHASIL] Login sukses sebagai {role.upper()}!")
            input("\nTekan Enter untuk masuk ke menu...")

            if role == "admin":
                while True:
                    clear_screen()
                    print("="*50)
                    print(f"{'MENU ADMIN (CRUD & KELOLA KARYAWAN)':^50}")
                    print("="*50)
                    print("1. Tambah Data Karyawan (Create)")
                    print("2. Input Absensi & Hitung Gaji (Update)")
                    print("3. Tampilkan Daftar & Rekap Gaji (Read)")
                    print("4. Hapus Data Karyawan (Delete)")
                    print("5. Logout")
                    
                    try:
                        pilihan_admin = int(input("Pilih menu admin (1-5): "))
                    except ValueError:
                        print("[ERROR] Masukkan angka antara 1 sampai 5!")
                        input("\nTekan Enter untuk melanjutkan...")
                        continue

                    if pilihan_admin == 1:
                        clear_screen()
                        print("--- Tambah Karyawan Baru (Create) ---")
                        id_kar = input("Masukkan ID Karyawan (Contoh K04): ")
                        if cek_id_karyawan(id_kar, database_karyawan):
                            print(f"[GAGAL] Karyawan dengan ID '{id_kar}' sudah terdaftar!")
                        else:
                            nama = input("Masukkan Nama Lengkap: ")
                            print("Pilih Golongan (A/B/C):")
                            gol = input("Masukkan Golongan: ").upper()
                            
                            if gol not in ['A', 'B', 'C']:
                                gol = 'A'
                                print("[INFO] Golongan tidak valid, diset default ke A.")
                            
                            gaji_bersih_awal = hitung_gaji_bersih(gol, 0, 0, 0)
                            database_karyawan[id_kar] = {
                                "nama": nama,
                                "gol": gol,
                                "hadir": 0,
                                "alpa": 0,
                                "lembur": 0,
                                "gaji_bersih": gaji_bersih_awal
                            }
                            print(f"[BERHASIL] Karyawan {nama} berhasil disimpan ke sistem.")
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_admin == 2:
                        clear_screen()
                        print("--- Input Absensi & Hitung Gaji (Update) ---")
                        if len(database_karyawan) == 0:
                            print("Belum ada data karyawan!")
                        else:
                            id_cari = input("Masukkan ID Karyawan yang ingin di-input: ")
                            if cek_id_karyawan(id_cari, database_karyawan):
                                print(f"Karyawan Ditemukan: {database_karyawan[id_cari]['nama']}")
                                try:
                                    hadir = int(input("Masukkan jumlah hari hadir: "))
                                    alpa = int(input("Masukkan jumlah hari alpa: "))
                                    lembur = int(input("Masukkan total jam lembur: "))
                                except ValueError:
                                    print("[ERROR] Input absensi harus berupa angka bulat!")
                                    input("\nTekan Enter untuk kembali...")
                                    continue

                                gol_k = database_karyawan[id_cari]['gol']
                                gaji_hasil = hitung_gaji_bersih(gol_k, hadir, alpa, lembur)
                                bonus_tambahan = hitung_bonus_rekursif(hadir)
                                gaji_total_akhir = gaji_hasil + bonus_tambahan

                                database_karyawan[id_cari]['hadir'] = hadir
                                database_karyawan[id_cari]['alpa'] = alpa
                                database_karyawan[id_cari]['lembur'] = lembur
                                database_karyawan[id_cari]['gaji_bersih'] = gaji_total_akhir

                                print(f"\n[BERHASIL] Absensi & perhitungan gaji telah diperbarui!")
                                print(f"Total Gaji Bersih (termasuk bonus rekursif) untuk {database_karyawan[id_cari]['nama']} adalah: Rp {gaji_total_akhir:,}")
                            else:
                                print(f"Karyawan dengan ID '{id_cari}' tidak ditemukan.")
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_admin == 3:
                        clear_screen()
                        cetak_tabel_karyawan(database_karyawan)
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_admin == 4:
                        clear_screen()
                        print("--- Hapus Data Karyawan (Delete) ---")
                        id_hapus = input("Masukkan ID Karyawan yang ingin dihapus: ")
                        if cek_id_karyawan(id_hapus, database_karyawan):
                            nama_hapus = database_karyawan[id_hapus]['nama']
                            del database_karyawan[id_hapus]
                            print(f"[BERHASIL] Data karyawan {nama_hapus} telah dihapus dari sistem.")
                        else:
                            print(f"Karyawan dengan ID '{id_hapus}' tidak ditemukan.")
                        input("\nTekan Enter untuk kembali...")

                    elif pilihan_admin == 5:
                        print("[INFO] Logout dari akun Admin berhasil.")
                        input("\nTekan Enter untuk kembali ke halaman login...")
                        break
                    else:
                        print("[SALAH] Pilihan menu admin tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")

            else:
                while True:
                    clear_screen()
                    print("="*40)
                    print(f"{'MENU PENGGUNA BIASA (USER)':^40}")
                    print("="*40)
                    print("1. Tampilkan Daftar & Rekap Gaji (Read)")
                    print("2. Logout")
                    
                    try:
                        pilihan_user = int(input("Pilih menu pengguna (1-2): "))
                    except ValueError:
                        print("[ERROR] Masukkan angka 1 atau 2!")
                        input("\nTekan Enter untuk melanjutkan...")
                        continue

                    if pilihan_user == 1:
                        clear_screen()
                        cetak_tabel_karyawan(database_karyawan)
                        input("\nTekan Enter untuk kembali...")
                    elif pilihan_user == 2:
                        print("[INFO] Logout dari akun Pengguna berhasil.")
                        input("\nTekan Enter untuk kembali ke halaman login...")
                        break
                    else:
                        print("[SALAH] Pilihan menu tidak valid!")
                        input("\nTekan Enter untuk melanjutkan...")
        else:
            print("[GAGAL] Username atau Password salah!")
            input("\nTekan Enter untuk mencoba lagi...")

    elif pilihan_utama == 2:
        clear_screen()
        print("--- REGISTER AKUN BARU ---")
        new_user = input("Buat Username baru: ")
        if new_user in database_user:
            print(f"[GAGAL] Username '{new_user}' sudah terdaftar!")
        else:
            new_pass = input("Buat Password baru: ")
            database_user[new_user] = {"password": new_pass, "role": "user"}
            print(f"[BERHASIL] Akun baru dengan username '{new_user}' berhasil didaftarkan sebagai pengguna biasa!")
        input("\nTekan Enter untuk kembali...")

    elif pilihan_utama == 3:
        clear_screen()
        tampilkan_pesan_penutup()
        status_program = False
        break
    else:
        print("[SALAH] Pilihan menu utama tidak valid!")
        input("\nTekan Enter untuk mencoba lagi...")