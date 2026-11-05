import os
from prettytable import PrettyTable
from colorama import Fore, init

init(autoreset=True)

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
    """Membersihkan layar terminal sesuai sistem operasi."""
    os.system('cls' if os.name == 'nt' else 'clear')


def hitung_bonus_rekursif(hari):
    """Menghitung bonus kehadiran secara rekursif."""
    bonus_per_hari = 10000
    if hari <= 0:
        return 0
    else:
        return bonus_per_hari + hitung_bonus_rekursif(hari - 1)


def hitung_gaji_bersih(gol, hadir, alpa, lembur):
    """Menghitung total gaji bersih berdasarkan golongan dan absensi."""
    gaji_pokok_standar = 4000000
    tunjangan_standar = 1000000
    tarif_lembur = 50000
    potongan_per_alpa = 100000
    
    if gol == 'B':
        gaji_pokok_standar = 6000000
        tunjangan_standar = 2000000
    elif gol == 'C':
        gaji_pokok_standar = 8500000
        tunjangan_standar = 3500000
        
    total_lembur = lembur * tarif_lembur
    total_potongan = alpa * potongan_per_alpa
    bonus_hadir = hitung_bonus_rekursif(hadir)
    
    gaji_kotor = gaji_pokok_standar + tunjangan_standar + total_lembur + bonus_hadir
    gaji_bersih_val = gaji_kotor - total_potongan

    if gaji_bersih_val < 0:
        gaji_bersih_val = 0
    return int(gaji_bersih_val)


def cek_id_karyawan(id_kry):
    """Memeriksa apakah ID Karyawan sudah ada di database."""
    return id_kry in database_karyawan


def tampilkan_header_utama():
    """Mengembalikan teks header program."""
    return "SISTEM PENGGAJIAN & ABSENSI KARYAWAN"


def ambil_info_versi():
    """Mengembalikan informasi versi program."""
    return "Posttest 8 - Single File & PrettyTable"


def cetak_tabel_karyawan():
    """Menampilkan data karyawan dalam bentuk tabel rapi (PrettyTable)."""
    table = PrettyTable()
    table.field_names = ["ID", "Nama Karyawan", "Gol", "Hadir", "Alpa", "Lembur", "Gaji Bersih"]
    
    table.align["ID"] = "c"            
    table.align["Nama Karyawan"] = "l"  
    table.align["Gol"] = "c"           
    table.align["Hadir"] = "c"          
    table.align["Alpa"] = "c"          
    table.align["Lembur"] = "c"         
    table.align["Gaji Bersih"] = "r"    
    
    if not database_karyawan:
        print(Fore.YELLOW + "Belum ada data karyawan yang tersimpan.")
    else:
        for k, v in database_karyawan.items():
            gaji_f = f"Rp {v['gaji_bersih']:,}"
            table.add_row([k, v['nama'], v['gol'], v['hadir'], v['alpa'], v['lembur'], gaji_f])
        print(table)


def tampilkan_pesan_penutup():
    """Menampilkan pesan saat program berakhir."""
    print(Fore.GREEN + "\nKeluar dari program. Terima kasih!")


def menu_login():
    """Menangani proses login pengguna."""
    clear_screen()
    print("=" * 45)
    print(f"{'MENU LOGIN':^45}")
    print("=" * 45)
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if username in database_user and database_user[username]["password"] == password:
        role = database_user[username]["role"]
        print(Fore.GREEN + f"\n[BERHASIL] Login sukses sebagai {role.upper()}!")
        input("\nTekan Enter untuk masuk ke menu...")
        return role 
    else:
        print(Fore.RED + "\n[SALAH] Username atau Password salah!")
        input("\nTekan Enter untuk kembali...")
        return None 


def menu_register():
    """Menangani proses pendaftaran akun baru."""
    clear_screen()
    print("=" * 45)
    print(f"{'REGISTER AKUN BARU':^45}")
    print("=" * 45)
    new_user = input("Buat Username baru: ")
    if new_user in database_user:
        print(Fore.RED + f"[GAGAL] Username '{new_user}' sudah terdaftar!")
    else:
        new_pass = input("Buat Password baru: ")
        database_user[new_user] = {"password": new_pass, "role": "user"}
        print(Fore.GREEN + f"[BERHASIL] Akun baru dengan username '{new_user}' berhasil didaftarkan sebagai pengguna biasa!")
    input("\nTekan Enter untuk kembali...")


def menu_admin():
    """Menampilkan Menu Admin dengan akses penuh fitur CRUD."""
    while True:
        clear_screen()
        print("=" * 50)
        print(f"{'MENU ADMIN (CRUD & KELOLA KARYAWAN)':^50}")
        print("=" * 50)
        print("1. Tambah Data Karyawan (Create)")
        print("2. Input Absensi & Hitung Gaji (Update)")
        print("3. Tampilkan Daftar & Rekap Gaji (Read)")
        print("4. Hapus Data Karyawan (Delete)")
        print("5. Logout")
        
        pilihan = input("Pilih menu admin (1-5): ")
        if pilihan == '1':
            clear_screen()
            print("--- TAMBAH DATA KARYAWAN (CREATE) ---")
            id_kry = input("Masukkan ID Karyawan baru (cth: K04): ").upper()
            if cek_id_karyawan(id_kry):
                print(Fore.RED + f"[GAGAL] ID Karyawan '{id_kry}' sudah terdaftar!")
            else:
                nama = input("Nama Karyawan: ")
                gol = input("Golongan (A/B/C): ").upper()
                if gol not in ['A', 'B', 'C']:
                    print(Fore.RED + "[SALAH] Golongan tidak valid! Default ke A.")
                    gol = 'A'
                try:
                    hadir = int(input("Jumlah Hadir: "))
                    alpa = int(input("Jumlah Alpa: "))
                    lembur = int(input("Jam Lembur: "))
                    gaji_bersih = hitung_gaji_bersih(gol, hadir, alpa, lembur)
                    database_karyawan[id_kry] = {
                        "nama": nama,
                        "gol": gol,
                        "hadir": hadir,
                        "alpa": alpa,
                        "lembur": lembur,
                        "gaji_bersih": gaji_bersih
                    }
                    print(Fore.GREEN + f"[BERHASIL] Data karyawan '{nama}' berhasil ditambahkan!")
                except ValueError:
                    print(Fore.RED + "[SALAH] Input absensi harus berupa angka!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '2':
            clear_screen()
            print("--- UPDATE ABSENSI & HITUNG GAJI (UPDATE) ---")
            cetak_tabel_karyawan()
            id_kry = input("\nMasukkan ID Karyawan yang ingin diupdate: ").upper()
            if not cek_id_karyawan(id_kry):
                print(Fore.RED + f"[GAGAL] ID Karyawan '{id_kry}' tidak ditemukan!")
            else:
                print(f"Mengupdate data untuk: {database_karyawan[id_kry]['nama']}")
                gol = input("Golongan baru (A/B/C): ").upper()
                if gol not in ['A', 'B', 'C']:
                    print(Fore.RED + "[SALAH] Golongan tidak valid! Default ke A.")
                    gol = 'A'
                try:
                    hadir = int(input("Jumlah Hadir baru: "))
                    alpa = int(input("Jumlah Alpa baru: "))
                    lembur = int(input("Jam Lembur baru: "))
                    gaji_bersih = hitung_gaji_bersih(gol, hadir, alpa, lembur)
                    database_karyawan[id_kry].update({
                        "gol": gol,
                        "hadir": hadir,
                        "alpa": alpa,
                        "lembur": lembur,
                        "gaji_bersih": gaji_bersih
                    })
                    print(Fore.GREEN + f"[BERHASIL] Data absensi dan gaji karyawan '{id_kry}' berhasil diperbarui!")
                except ValueError:
                    print(Fore.RED + "[SALAH] Input absensi harus berupa angka!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '3':
            clear_screen()
            print("=" * 90)
            print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (READ)':^90}")
            print("=" * 90)
            cetak_tabel_karyawan()
            print("=" * 90)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '4':
            clear_screen()
            print("--- HAPUS DATA KARYAWAN (DELETE) ---")
            cetak_tabel_karyawan()
            id_kry = input("\nMasukkan ID Karyawan yang ingin dihapus: ").upper()
            if cek_id_karyawan(id_kry):
                nama_dihapus = database_karyawan[id_kry]['nama']
                del database_karyawan[id_kry]
                print(Fore.GREEN + f"[BERHASIL] Data karyawan '{nama_dihapus}' berhasil dihapus!")
            else:
                print(Fore.RED + f"[GAGAL] ID Karyawan '{id_kry}' tidak ditemukan!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '5':
            print(Fore.YELLOW + "Logout dari Menu Admin...")
            input("\nTekan Enter untuk kembali ke menu utama...")
            break 
        else:
            print(Fore.RED + "[SALAH] Pilihan menu tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")


def menu_user():
    """Menampilkan Menu User biasa (Hanya akses Read data)."""
    while True:
        clear_screen()
        print("=" * 50)
        print(f"{'MENU PENGGUNA (USER)':^50}")
        print("=" * 50)
        print("1. Tampilkan Daftar & Rekap Gaji (Read)")
        print("2. Logout")
        
        pilihan = input("Pilih menu user (1-2): ")
        if pilihan == '1':
            clear_screen()
            print("=" * 90)
            print(f"{'REKAPITULASI GAJI & ABSENSI KARYAWAN (READ)':^90}")
            print("=" * 90)
            cetak_tabel_karyawan()
            print("=" * 90)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '2':
            print(Fore.YELLOW + "Logout dari Menu Pengguna...")
            input("\nTekan Enter untuk kembali ke menu utama...")
            break
        else:
            print(Fore.RED + "[SALAH] Pilihan menu tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")


if __name__ == "__main__":
    while status_program:
        clear_screen()
        print("=" * 45)
        print(f"{tampilkan_header_utama():^45}")
        print(f"{ambil_info_versi():^45}")
        print("=" * 45)
        print("1. Login")
        print("2. Register Akun Baru")
        print("3. Keluar Program")
        print("=" * 45)
        
        pilihan_utama = input("Pilih menu (1-3): ")
        
        if pilihan_utama == '1':
            role = menu_login()
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
        elif pilihan_utama == '2':
            menu_register()
        elif pilihan_utama == '3':
            clear_screen()
            tampilkan_pesan_penutup()
            status_program = False
            break
        else:
            print(Fore.RED + "[SALAH] Pilihan menu utama tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")