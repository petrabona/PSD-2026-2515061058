class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nDaftar Titipan Barang (Loker):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("KOSONG")

    def clear_all(self):
        self.table = [None] * self.SIZE
        print("Semua titipan barang telah dibersihkan.")

def main():
    hashmap = HashMapSeparateChaining()

    while True:
        print("\n--- Menu Penitipan Barang Mall ---")
        print("1. Titip Barang")
        print("2. Lihat Daftar Barang Dititipkan")
        print("3. Cari Barang")
        print("4. Ambil Barang")
        print("5. Bersihkan Semua Titipan")
        print("6. Akhiri Sesi")

        choice = input("Masukkan pilihan Anda (1-6): ")

        if choice == '1':
            try:
                key = int(input("Masukkan nomor loker (kunci): "))
                value = input("Masukkan deskripsi barang: ")
                hashmap.insert(key, value)
                print(f"Barang dengan nomor loker '{key}' dan deskripsi '{value}' berhasil dititipkan.")
            except ValueError:
                print("Nomor loker tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '2':
            hashmap.display()
        elif choice == '3':
            try:
                key_to_search = int(input("Masukkan nomor loker yang dicari: "))
                result = hashmap.search(key_to_search)
                if result is not None:
                    print(f"Barang dengan nomor loker '{key_to_search}' ditemukan: {result}")
                else:
                    print(f"Barang dengan nomor loker '{key_to_search}' tidak ditemukan.")
            except ValueError:
                print("Nomor loker tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '4':
            try:
                key_to_remove = int(input("Masukkan nomor loker barang yang akan diambil: "))
                if hashmap.remove_key(key_to_remove):
                    print(f"Barang dengan nomor loker '{key_to_remove}' berhasil diambil.")
                else:
                    print(f"Barang dengan nomor loker '{key_to_remove}' tidak ditemukan.")
            except ValueError:
                print("Nomor loker tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '5':
            hashmap.clear_all()
        elif choice == '6':
            print("Sesi manajemen penitipan barang diakhiri.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 6.")

if __name__ == "__main__":
    main()
