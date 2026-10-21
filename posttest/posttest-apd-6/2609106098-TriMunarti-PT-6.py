import os

database_user = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

database_karyawan = {
    "K01": {
        "nama": "Beni",
        "gol": "A",
        "hadir": 20,
        "alpa": 0,
        "lembur": 5,
        "gaji_bersih": 5250000,
    },
    "K02": {
        "nama": "Siti",
        "gol": "B",
        "hadir": 18,
        "alpa": 2,
        "lembur": 3,
        "gaji_bersih": 7950000,
    },
    "K03": {
        "nama": "Rian",
        "gol": "C",
        "hadir": 22,
        "alpa": 0,
        "lembur": 10,
        "gaji_bersih": 12500000,
    },
}


def bersihkan_layar():
  os.system("cls" if os.name == "nt" else "clear")


def menu_login():
  while True:
    bersihkan_layar()
    print("=" * 45)
    print(f"{'LOGIN & REGISTER SISTEM KARYAWAN':^45}")
    print("=" * 45)
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
      print("\n--- LOGIN AKUN ---")
      username = input("Masukkan Username: ")
      password = input("Masukkan Password: ")

      if (
          username in database_user
          and database_user[username]["password"] == password
      ):
        print(f"\n[SUKSES] Login berhasil! Selamat datang, {username}.")
        input("Tekan Enter untuk masuk ke menu utama...")
        return username, database_user[username]["role"]
      else:
        print("\n[GAGAL] Username atau Password salah!")
        input("Tekan Enter untuk mencoba kembali...")

    elif pilihan == "2":
      print("\n--- REGISTER AKUN BARU ---")
      username = input("Buat Username baru: ")
      if username in database_user:
        print(
            "\n[GAGAL] Username tersebut sudah terdaftar! Gunakan nama lain."
        )
      else:
        password = input("Buat Password baru: ")
        database_user[username] = {"password": password, "role": "user"}
        print(
            f"\n[SUKSES] Akun dengan username '{username}' berhasil"
            " didaftarkan!"
        )
      input("Tekan Enter untuk kembali...")

    elif pilihan == "3":
      print("\nKeluar dari program. Terima kasih!")
      exit()
    else:
      print("\n[SALAH] Pilihan menu tidak valid, silakan masukkan angka 1-3.")
      input("Tekan Enter untuk melanjutkan...")


def program_utama(username, role):
  while True:
    bersihkan_layar()
    print("=" * 50)
    print(f"{'SISTEM PENGGAJIAN & ABSENSI KARYAWAN':^50}")
    print(f"{'Login sebagai: ' + username + ' (' + role.upper() + ')':^50}")
    print("=" * 50)

    if role == "admin":
      print("1. Tambah Data Karyawan Baru (Create)")
      print("2. Input Absensi & Hitung Gaji (Update)")
      print("3. Tampilkan Daftar & Rekap Gaji (Read)")
      print("4. Hapus Data Karyawan (Delete)")
      print("5. Logout / Ganti Akun")
      pilihan = input("Pilih menu (1-5): ")

      if pilihan == "1":
        print("\n--- Tambah Karyawan Baru (Create) ---")
        id_kar = input("Masukkan ID Karyawan (Contoh K04): ")
        if id_kar in database_karyawan:
          print(f"[GAGAL] ID Karyawan '{id_kar}' sudah terdaftar di database!")
        else:
          nama = input("Masukkan Nama Lengkap: ")
          print("Pilih Golongan:")
          print("  A. Gaji Pokok Rp 4.000.000 (Tunjangan Rp 1.000.000)")
          print("  B. Gaji Pokok Rp 6.000.000 (Tunjangan Rp 2.000.000)")
          print("  C. Gaji Pokok Rp 8.500.000 (Tunjangan Rp 3.500.000)")
          gol = input("Masukkan Golongan (A/B/C): ").upper()

          if gol in ["A", "B", "C"]:
            database_karyawan[id_kar] = {
                "nama": nama,
                "gol": gol,
                "hadir": 0,
                "alpa": 0,
                "lembur": 0,
                "gaji_bersih": 0,
            }
            print(f"[SUKSES] Karyawan {nama} berhasil ditambahkan.")
          else:
            print("[GAGAL] Golongan yang dimasukkan tidak valid!")
        input("\nTekan Enter untuk kembali ke menu...")

      elif pilihan == "2":
        print("\n--- Input Absensi & Hitung Gaji (Update) ---")
        if len(database_karyawan) == 0:
          print("Belum ada data karyawan!")
        else:
          id_cari = input("Masukkan ID Karyawan yang ingin di-input: ")
          if id_cari in database_karyawan:
            k = database_karyawan[id_cari]
            print(f"Karyawan Ditemukan: {k['nama']}")

            hadir_str = input("Masukkan jumlah hari hadir: ")
            alpa_str = input("Masukkan jumlah hari alpa: ")
            lembur_str = input("Masukkan total jam lembur: ")

            if (
                hadir_str.isdigit()
                and alpa_str.isdigit()
                and lembur_str.isdigit()
            ):
              hadir = int(hadir_str)
              alpa = int(alpa_str)
              lembur = int(lembur_str)

              if k["gol"] == "A":
                gaji_pokok, tunjangan = 4000000, 1000000
              elif k["gol"] == "B":
                gaji_pokok, tunjangan = 6000000, 2000000
              elif k["gol"] == "C":
                gaji_pokok, tunjangan = 8500000, 3500000

              tarif_lembur = 50000
              potongan_alpa = 100000

              total_lembur = lembur * tarif_lembur
              total_potongan = alpa * potongan_alpa
              gaji_kotor = gaji_pokok + tunjangan + total_lembur
              gaji_bersih = gaji_kotor - total_potongan

              if gaji_bersih < 0:
                gaji_bersih = 0

              database_karyawan[id_cari]["hadir"] = hadir
              database_karyawan[id_cari]["alpa"] = alpa
              database_karyawan[id_cari]["lembur"] = lembur
              database_karyawan[id_cari]["gaji_bersih"] = gaji_bersih

              print(
                  "\n[BERHASIL] Absensi & perhitungan gaji telah diperbarui!"
              )
              print(
                  f"Total Gaji Bersih untuk {k['nama']}: Rp"
                  f" {gaji_bersih:,}".replace(",", ".")
              )
            else:
              print(
                  "[GAGAL] Kehadiran, alpa, dan lembur harus diisi dengan angka!"
              )
          else:
            print(f"Karyawan dengan ID '{id_cari}' tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")

      elif pilihan == "3":
        print("\n" + "=" * 90)
        print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (Read)':^90}")
        print("=" * 90)
        print(
            f"{'ID':<6} | {'Nama Karyawan':<18} | {'Gol':<4} | {'Hadir':<6} |"
            f" {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<15}"
        )
        print("-" * 90)

        if len(database_karyawan) == 0:
          print(f"{'Belum ada data karyawan yang tersimpan.':^90}")
        else:
          for id_kar, k in database_karyawan.items():
            gaji_format = f"Rp {k['gaji_bersih']:,}".replace(",", ".")
            print(
                f"{id_kar:<6} | {k['nama']:<18} | {k['gol']:<4} |"
                f" {k['hadir']:<6} | {k['alpa']:<5} | {k['lembur']:<8} |"
                f" {gaji_format:<15}"
            )
        print("=" * 90)
        input("\nTekan Enter untuk kembali ke menu...")

      elif pilihan == "4":
        print("\n--- Hapus Data Karyawan (Delete) ---")
        if len(database_karyawan) == 0:
          print("Belum ada data karyawan!")
        else:
          id_hapus = input("Masukkan ID Karyawan yang ingin dihapus: ")
          if id_hapus in database_karyawan:
            nama_terhapus = database_karyawan[id_hapus]["nama"]
            del database_karyawan[id_hapus]
            print(
                f"[BERHASIL] Data karyawan {nama_terhapus} telah dihapus dari"
                " sistem."
            )
          else:
            print(f"Karyawan dengan ID '{id_hapus}' tidak ditemukan.")
        input("\nTekan Enter untuk kembali ke menu...")

      elif pilihan == "5":
        print("\nLogout berhasil.")
        input("Tekan Enter untuk melanjutkan...")
        break
      else:
        print("\nPilihan menu tidak valid!")
        input("Tekan Enter untuk kembali ke menu...")

    elif role == "user":
      print("1. Tampilkan Daftar & Rekap Gaji (Read)")
      print("2. Logout / Ganti Akun")
      pilihan = input("Pilih menu (1-2): ")

      if pilihan == "1":
        print("\n" + "=" * 90)
        print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (Read)':^90}")
        print("=" * 90)
        print(
            f"{'ID':<6} | {'Nama Karyawan':<18} | {'Gol':<4} | {'Hadir':<6} |"
            f" {'Alpa':<5} | {'Lembur':<8} | {'Gaji Bersih':<15}"
        )
        print("-" * 90)

        if len(database_karyawan) == 0:
          print(f"{'Belum ada data karyawan yang tersimpan.':^90}")
        else:
          for id_kar, k in database_karyawan.items():
            gaji_format = f"Rp {k['gaji_bersih']:,}".replace(",", ".")
            print(
                f"{id_kar:<6} | {k['nama']:<18} | {k['gol']:<4} |"
                f" {k['hadir']:<6} | {k['alpa']:<5} | {k['lembur']:<8} |"
                f" {gaji_format:<15}"
            )
        print("=" * 90)
        input("\nTekan Enter untuk kembali ke menu...")

      elif pilihan == "2":
        print("\nLogout berhasil.")
        input("Tekan Enter untuk melanjutkan...")
        break
      else:
        print("\nPilihan menu tidak valid!")
        input("Tekan Enter untuk kembali ke menu...")


while True:
  user_aktif, role_aktif = menu_login()
  program_utama(user_aktif, role_aktif)