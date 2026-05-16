class SearchHistory:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.history = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def tambah_pencarian(self, search_query):
        if self.is_full():
            print("Riwayat pencarian penuh. Tidak dapat menambahkan pencarian baru.")
            return
        self.top_idx += 1
        self.history[self.top_idx] = search_query
        print(f"Menambahkan '{search_query}' ke riwayat.")

    def batalkan_pencarian(self):
        if self.is_empty():
            print("Riwayat pencarian kosong. Tidak ada yang bisa dibatalkan.")
            return None
        removed_query = self.history[self.top_idx]
        self.top_idx -= 1
        print(f"Membatalkan pencarian terakhir: '{removed_query}'.")
        return removed_query

    def lihat_pencarian_terbaru(self):
        if self.is_empty():
            print("Riwayat pencarian kosong.")
            return None
        print(f"Pencarian terbaru: '{self.history[self.top_idx]}'")
        return self.history[self.top_idx]

    def tampilkan_riwayat(self):
        if self.is_empty():
            print("Riwayat pencarian kosong.")
            return
        print("\n=== Riwayat Pencarian (terbaru ke terlama) ===")
        for i in range(self.top_idx, -1, -1):
            print(f"{self.top_idx - i + 1}. {self.history[i]}")
        print("===========================================")


def main():
    history_manager = SearchHistory()
    pilih = 0
    while pilih != 5:
        print("\n=== MANAJEMEN RIWAYAT PENCARIAN ===")
        print("1. Tambah Pencarian Baru")
        print("2. Batalkan Pencarian Terakhir")
        print("3. Lihat Pencarian Terbaru")
        print("4. Tampilkan Semua Riwayat")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue

        if pilih == 1:
            search_query = input("Masukkan pencarian baru: ")
            if search_query:
                history_manager.tambah_pencarian(search_query)
            else:
                print("Pencarian tidak boleh kosong.")
        elif pilih == 2:
            history_manager.batalkan_pencarian()
        elif pilih == 3:
            history_manager.lihat_pencarian_terbaru()
        elif pilih == 4:
            history_manager.tampilkan_riwayat()
        elif pilih == 5:
            print("Program manajemen riwayat pencarian selesai.")
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


if __name__ == "__main__":
    main()