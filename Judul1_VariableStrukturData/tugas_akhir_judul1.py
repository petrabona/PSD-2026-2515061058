def menu():
    print("\n=== Manajer Daftar Tugas ===")
    print("1. Tambah Tugas Baru")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

def main():
    tugas = []
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Input tidak valid, mohon masukkan angka.")
            continue

        if choice == 1:
            nama = input("Masukkan nama tugas baru: ")
            tugas.append({'pr': nama, 'completed': False})
            print(f"Tugas '{nama}' telah ditambahkan.")
        elif choice == 2:
            if not tugas:
                print("Daftar tugas kosong.")
            else:
                print("\n--- Daftar Tugas ---")
                for i, daftartugas in enumerate(tugas):
                    status = "[X]" if daftartugas['completed'] else "[ ]"
                    print(f"{i+1}. {status} {daftartugas['pr']}") 
        elif choice == 3:
            if not tugas:
                print("Daftar tugas kosong.")
                continue
            try:
                indeks = int(input("Masukkan nomor tugas yang ingin ditandai selesai: ")) - 1
                if 0 <= indeks < len(tugas):
                    tugas[indeks]['completed'] = True
                    print(f"Tugas '{tugas[indeks]['pr']}' telah ditandai selesai.")
                else:
                    print("Nomor tugas tidak valid.")
            except ValueError:
                print("Input tidak valid.")
        elif choice == 4:
            if not tugas:
                print("Daftar tugas kosong.")
                continue
            try:
                indeks = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
                if 0 <= indeks < len(tugas):
                    hapus_tugas = tugas.pop(indeks)
                    print(f"Tugas '{hapus_tugas['pr']}' telah dihapus.")
                else:
                    print("Nomor tugas tidak valid.")
            except ValueError:
                print("Input tidak valid.")
        elif choice == 5:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid, mohon pilih antara 1-5.")


if __name__ == "__main__":
    main()