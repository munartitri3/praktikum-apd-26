import os
from prettytable import PrettyTable
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_bonus_rekursif(hari):
    bonus_per_hari = 10000
    if hari <= 0:
        return 0
    else:
        return bonus_per_hari + hitung_bonus_rekursif(hari - 1)

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
    bonus_hadir = hitung_bonus_rekursif(hadir)
    
    gaji_kotor = gaji_pokok + tunjangan + total_lembur + bonus_hadir
    gaji_bersih_val = gaji_kotor - total_potongan
    
    if gaji_bersih_val < 0:
        gaji_bersih_val = 0
    return int(gaji_bersih_val)

def cek_id_karyawan(id_kry, db):
    return id_kry in db

def tampilkan_header_utama():
    return "SISTEM PENGGAJIAN & ABSENSI KARYAWAN"

def ambil_info_versi():
    return "Posttest 8 - Modular & PrettyTable"

def cetak_tabel_karyawan(db):
    table = PrettyTable()
    table.field_names = ["ID", "Nama Karyawan", "Gol", "Hadir", "Alpa", "Lembur", "Gaji Bersih"]
    
    table.align["ID"] = "c"
    table.align["Nama Karyawan"] = "l"
    table.align["Gol"] = "c"
    table.align["Hadir"] = "c"
    table.align["Alpa"] = "c"
    table.align["Lembur"] = "c"
    table.align["Gaji Bersih"] = "r"
    
    if not db:
        print(Fore.YELLOW + "Belum ada data karyawan yang tersimpan.")
    else:
        for k, v in db.items():
            gaji_f = f"Rp {v['gaji_bersih']:,}"
            table.add_row([k, v['nama'], v['gol'], v['hadir'], v['alpa'], v['lembur'], gaji_f])
        print(table)

def tampilkan_pesan_penutup():
    print(Fore.GREEN + "\nKeluar dari program. Terima kasih!")