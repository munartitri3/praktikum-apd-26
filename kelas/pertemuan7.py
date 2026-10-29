import sys

data_karyawan = {}       
status_login = False     
role_login = ""          

data_akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def tampilkan_header():
    print("=" * 50)
    print("   SISTEM MANAJEMEN DATA KARYAWAN DAN PENGGAJIAN   ")
    print("=" * 50)

def tampilkan_menu():
    print("\n--- MENU UTAMA ---")
    if role_login == "admin":
        print("1. Tambah Data Karyawan")
        print("2. Lihat Data Karyawan")
        print("3. Ubah Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Logout")
        print("6. Keluar Aplikasi")
    else:
        print("1. Lihat Data Karyawan")
        print("2. Logout")
        print("3. Keluar Aplikasi")

def fungsi_login():
    global status_login, role_login
    print("\n--- SILAKAN LOGIN ---")
    username = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()

    if username in data_akun and data_akun[username]["password"] == password:
        status_login = True
        role_login = data_akun[username]["role"]
        print(f"\n[SUKSES] Login berhasil! Selamat datang, {username.upper()} ({role_login.upper()}).")
        return True
    else:
        print("\n[GAGAL] Username atau password salah!")
        return False

def fungsi_input_id():
    while True:
        try:
            id_input = int(input("Masukkan ID Karyawan (Angka): "))
            if id_input <= 0:
                raise ValueError("ID Karyawan harus berupa bilangan bulat positif!")
            return id_input
        except ValueError as err:
            print(f"[ERROR INVALID INPUT]: {err}. Silakan coba lagi.")

def hitung_gaji_bersih(gaji_pokok, tunjangan):
    total_kotor = gaji_pokok + tunjangan
    potongan_pajak = total_kotor * 0.05
    gaji_bersih = total_kotor - potongan_pajak
    return gaji_bersih

def cari_karyawan(id_karyawan):
    data_ditemukan = data_karyawan.get(id_karyawan, None)
    return data_ditemukan

def tambah_karyawan():
    print("\n--- TAMBAH DATA KARYAWAN ---")
    id_karyawan = fungsi_input_id()

    if id_karyawan in data_karyawan:
        print(f"[PERINGATAN] Data dengan ID {id_karyawan} sudah ada!")
        return

    nama = input("Masukkan Nama Karyawan : ").strip()
    if not nama:
        print("[ERROR]: Nama karyawan tidak boleh kosong!")
        return

    try:
        gaji_pokok = float(input("Masukkan Gaji Pokok (Rp) : "))
        tunjangan = float(input("Masukkan Tunjangan (Rp) : "))
        if gaji_pokok < 0 or tunjangan < 0:
            raise ValueError("GajiPokok dan Tunjangan tidak boleh bernilai negatif!")
    except ValueError as e:
        print(f"[ERROR INPUT GAJI]: {e}")
        return

    gaji_total = hitung_gaji_bersih(gaji_pokok, tunjangan)

    data_karyawan[id_karyawan] = {
        "nama": nama,
        "gaji_pokok": gaji_pokok,
        "tunjangan": tunjangan,
        "gaji_bersih": gaji_total
    }
    print(f"[BERHASIL] Data karyawan {nama} berhasil ditambahkan!")

def lihat_karyawan():
    print("\n--- DAFTAR DATA KARYAWAN ---")
    try:
        if not data_karyawan:
            print("[INFO] Belum ada data karyawan yang tersimpan.")
            return

        print("-" * 65)
        print(f"{'ID':<6} | {'Nama Karyawan':<20} | {'Gaji Pokok':<12} | {'Gaji Bersih':<12}")
        print("-" * 65)
        for id_k, info in data_karyawan.items():
            print(f"{id_k:<6} | {info['nama']:<20} | Rp{info['gaji_pokok']:<10.0f} | Rp{info['gaji_bersih']:<10.0f}")
        print("-" * 65)
    except Exception as err:
        print(f"[ERROR SYSTEM]: Terjadi kesalahan saat menampilkan data ({err})")

def ubah_karyawan():
    print("\n--- UBAH DATA KARYAWAN ---")
    id_karyawan = fungsi_input_id()
    karyawan = cari_karyawan(id_karyawan)

    if not karyawan:
        print(f"[ERROR]: Data karyawan dengan ID {id_karyawan} tidak ditemukan!")
        return

    print(f"Data ditemukan: {karyawan['nama']}")
    nama_baru = input("Masukkan Nama Baru (Tekan Enter jika tidak diubah): ").strip()
    
    try:
        gaji_input = input("Masukkan Gaji Pokok Baru (Tekan Enter jika tidak diubah): ").strip()
        tunjangan_input = input("Masukkan Tunjangan Baru (Tekan Enter jika tidak diubah): ").strip()

        gaji_pokok_baru = float(gaji_input) if gaji_input else karyawan['gaji_pokok']
        tunjangan_baru = float(tunjangan_input) if tunjangan_input else karyawan['tunjangan']

        if gaji_pokok_baru < 0 or tunjangan_baru < 0:
            raise ValueError("Nominal tidak boleh negatif!")

    except ValueError as err:
        print(f"[ERROR INPUT]: {err}")
        return

    if nama_baru:
        karyawan['nama'] = nama_baru
    karyawan['gaji_pokok'] = gaji_pokok_baru
    karyawan['tunjangan'] = tunjangan_baru
    karyawan['gaji_bersih'] = hitung_gaji_bersih(gaji_pokok_baru, tunjangan_baru)

    print(f"[BERHASIL] Data karyawan ID {id_karyawan} berhasil diperbarui!")

def hapus_karyawan():
    print("\n--- HAPUS DATA KARYAWAN ---")
    id_karyawan = fungsi_input_id()

    try:
        if id_karyawan in data_karyawan:
            del data_karyawan[id_karyawan]
            print(f"[BERHASIL] Data karyawan ID {id_karyawan} berhasil dihapus.")
        else:
            print(f"[ERROR]: ID {id_karyawan} tidak ditemukan dalam database!")
    except KeyError as err:
        print(f"[ERROR KEY]: Data kunci {err} tidak ditemukan.")

def main():
    global status_login, role_login
    tampilkan_header()

    while True:
        if not status_login:
            if not fungsi_login():
                pilihan_retry = input("Coba login lagi? (y/n): ").strip().lower()
                if pilihan_retry != 'y':
                    print("\nTerima kasih telah menggunakan program ini.")
                    sys.exit()
                continue

        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if role_login == "admin":
            if pilihan == "1":
                tambah_karyawan()
            elif pilihan == "2":
                lihat_karyawan()
            elif pilihan == "3":
                ubah_karyawan()
            elif pilihan == "4":
                hapus_karyawan()
            elif pilihan == "5":
                status_login = False
                role_login = ""
                print("\n[LOGOUT] Anda telah keluar dari akun.")
            elif pilihan == "6":
                print("\nTerima kasih telah menggunakan sistem ini!")
                sys.exit()
            else:
                print("[ERROR]: Pilihan menu tidak valid!")

        elif role_login == "user":
            if pilihan == "1":
                lihat_karyawan()
            elif pilihan == "2":
                status_login = False
                role_login = ""
                print("\n[LOGOUT] Anda telah keluar dari akun.")
            elif pilihan == "3":
                print("\nTerima kasih telah menggunakan sistem ini!")
                sys.exit()
            else:
                print("[ERROR]: Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()