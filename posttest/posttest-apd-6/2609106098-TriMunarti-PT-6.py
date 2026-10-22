database_user = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

database_karyawan = {
    "K001": {"nama": "Beni", "gol": "A", "hadir": 20, "alpa": 0, "lembur": 5, "gaji_bersih": 5250000},
    "K002": {"nama": "Siti", "gol": "B", "hadir": 18, "alpa": 2, "lembur": 3, "gaji_bersih": 7950000},
    "K003": {"nama": "Rian", "gol": "C", "hadir": 22, "alpa": 0, "lembur": 10, "gaji_bersih": 12500000}
}

while True:
    print("\n" + "="*45)
    print(f"{'SISTEM PENGGAJIAN & ABSENSI KARYAWAN':^45}")
    print("="*45)
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    pilihan_utama = input("Pilih menu (1-3): ")

    if pilihan_utama == "1":
        print("\n--- MENU LOGIN ---")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        if username in database_user and database_user[username]["password"] == password:
            role = database_user[username]["role"]
            print(f"\n[BERHASIL] Login sukses sebagai {role.upper()}!")

            if role == "admin":
                while True:
                    print("\n" + "="*50)
                    print(f"{'MENU ADMIN (CRUD & KELOLA KARYAWAN)':^50}")
                    print("="*50)
                    print("1. Tambah Data Karyawan (Create)")
                    print("2. Input Absensi & Hitung Gaji (Update)")
                    print("3. Tampilkan Daftar & Rekap Gaji (Read)")
                    print("4. Hapus Data Karyawan (Delete)")
                    print("5. Logout")
                    pilihan_admin = input("Pilih menu admin (1-5): ")

                    if pilihan_admin == "1":
                        print("\n--- Tambah Karyawan Baru (Create) ---")
                        id_kar = input("Masukkan ID Karyawan (Contoh K04): ")
                        if id_kar in database_karyawan:
                            print(f"[GAGAL] Karyawan dengan ID '{id_kar}' sudah terdaftar!")
                        else:
                            nama = input("Masukkan Nama Lengkap: ")
                            print("Pilih Golongan:")
                            print(" A. Gaji Pokok Rp 4.000.000 (Tunjangan Rp 1.000.000)")
                            print(" B. Gaji Pokok Rp 6.000.000 (Tunjangan Rp 2.000.000)")
                            print(" C. Gaji Pokok Rp 8.500.000 (Tunjangan Rp 3.500.000)")
                            gol = input("Masukkan Golongan (A/B/C): ").upper()

                            if gol == 'A':
                                gaji_pokok = 4000000
                                tunjangan = 1000000
                            elif gol == 'B':
                                gaji_pokok = 6000000
                                tunjangan = 2000000
                            elif gol == 'C':
                                gaji_pokok = 8500000
                                tunjangan = 3500000
                            else:
                                gaji_pokok = 4000000
                                tunjangan = 1000000
                                gol = 'A'

                            gaji_bersih = gaji_pokok + tunjangan
                            database_karyawan[id_kar] = {
                                "nama": nama,
                                "gol": gol,
                                "hadir": 0,
                                "alpa": 0,
                                "lembur": 0,
                                "gaji_bersih": gaji_bersih
                            }
                            print(f"[BERHASIL] Karyawan {nama} berhasil disimpan ke sistem.")

                    elif pilihan_admin == "2":
                        print("\n--- Input Absensi & Hitung Gaji (Update) ---")
                        if len(database_karyawan) == 0:
                            print("Belum ada data karyawan!")
                        else:
                            id_cari = input("Masukkan ID Karyawan yang ingin di-input (misal: K01, K02, K03): ")
                            if id_cari in database_karyawan:
                                print(f"Karyawan Ditemukan: {database_karyawan[id_cari]['nama']}")
                                hadir = int(input("Masukkan jumlah hari hadir: "))
                                alpa = int(input("Masukkan jumlah hari alpa: "))
                                lembur = int(input("Masukkan total jam lembur: "))

                                gol = database_karyawan[id_cari]['gol']
                                if gol == 'A':
                                    gaji_pokok = 4000000
                                    tunjangan = 1000000
                                elif gol == 'B':
                                    gaji_pokok = 6000000
                                    tunjangan = 2000000
                                elif gol == 'C':
                                    gaji_pokok = 8500000
                                    tunjangan = 3500000
                                else:
                                    gaji_pokok = 4000000
                                    tunjangan = 1000000

                                total_lembur = lembur * 50000
                                potongan_alpa = alpa * 100000
                                gaji_kotor = gaji_pokok + tunjangan + total_lembur
                                gaji_bersih = gaji_kotor - potongan_alpa

                                if gaji_bersih < 0:
                                    gaji_bersih = 0

                                database_karyawan[id_cari]['hadir'] = hadir
                                database_karyawan[id_cari]['alpa'] = alpa
                                database_karyawan[id_cari]['lembur'] = lembur
                                database_karyawan[id_cari]['gaji_bersih'] = gaji_bersih

                                print(f"\n[BERHASIL] Absensi & perhitungan gaji telah diperbarui!")
                                print(f"Total Gaji Bersih untuk {database_karyawan[id_cari]['nama']} adalah: Rp {gaji_bersih:,}")
                            else:
                                print(f"Karyawan dengan ID '{id_cari}' tidak ditemukan.")

                    elif pilihan_admin == "3":
                        print("\n" + "="*85)
                        print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (Read - Admin)':^85}")
                        print("="*85)
                        print(f"{'ID':<6} | {'Nama Karyawan':<18} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<15}")
                        print("-" * 85)
                        if len(database_karyawan) == 0:
                            print(f"{'Belum ada data karyawan yang tersimpan.':^85}")
                        else:
                            for k, v in database_karyawan.items():
                                print(f"{k:<6} | {v['nama']:<18} | {v['gol']:<4} | {v['hadir']:<6} | {v['alpa']:<5} | {v['lembur']:<8} | Rp {v['gaji_bersih']:,}")
                        print("="*85)

                    elif pilihan_admin == "4":
                        print("\n--- Hapus Data Karyawan (Delete) ---")
                        id_hapus = input("Masukkan ID Karyawan yang ingin dihapus: ")
                        if id_hapus in database_karyawan:
                            nama_hapus = database_karyawan[id_hapus]['nama']
                            database_karyawan.pop(id_hapus)
                            print(f"[BERHASIL] Data karyawan {nama_hapus} telah dihapus dari sistem.")
                        else:
                            print(f"Karyawan dengan ID '{id_hapus}' tidak ditemukan.")

                    elif pilihan_admin == "5":
                        print("[INFO] Logout dari akun Admin berhasil.")
                        break
                    else:
                        print("[SALAH] Pilihan menu tidak valid!")

            else:
                while True:
                    print("\n" + "="*40)
                    print(f"{'MENU PENGGUNA BIASA (USER)':^40}")
                    print("="*40)
                    print("1. Tampilkan Daftar & Rekap Gaji (Read)")
                    print("2. Logout")
                    pilihan_user = input("Pilih menu pengguna (1-2): ")

                    if pilihan_user == "1":
                        print("\n" + "="*85)
                        print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (Read - User)':^85}")
                        print("="*85)
                        print(f"{'ID':<6} | {'Nama Karyawan':<18} | {'Gol':<4} | {'Hadir':<6} | {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<15}")
                        print("-" * 85)
                        if len(database_karyawan) == 0:
                            print(f"{'Belum ada data karyawan yang tersimpan.':^85}")
                        else:
                            for k, v in database_karyawan.items():
                                print(f"{k:<6} | {v['nama']:<18} | {v['gol']:<4} | {v['hadir']:<6} | {v['alpa']:<5} | {v['lembur']:<8} | Rp {v['gaji_bersih']:,}")
                        print("="*85)
                    elif pilihan_user == "2":
                        print("[INFO] Logout dari akun Pengguna berhasil.")
                        break
                    else:
                        print("[SALAH] Pilihan menu tidak valid!")
        else:
            print("[GAGAL] Username atau Password salah!")

    elif pilihan_utama == "2":
        print("\n--- REGISTER AKUN BARU ---")
        new_user = input("Buat Username baru: ")
        if new_user in database_user:
            print(f"[GAGAL] Username '{new_user}' sudah terdaftar!")
        else:
            new_pass = input("Buat Password baru: ")
            database_user[new_user] = {"password": new_pass, "role": "user"}
            print(f"[BERHASIL] Akun baru dengan username '{new_user}' berhasil didaftarkan sebagai pengguna biasa!")

    elif pilihan_utama == "3":
        print("\nKeluar dari program. Terima kasih!")
        break
    else:
        print("[SALAH] Pilihan menu utama tidak valid!")