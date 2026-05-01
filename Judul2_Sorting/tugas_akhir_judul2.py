def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(peserta):
    n = len(peserta)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if peserta[j]['sampah'] < peserta[j + 1]['sampah']:
                tukar(peserta, j, j + 1)

def main():
    try:
        num_kontributor = int(input("Masukkan jumlah kontributor: "))
        if num_kontributor <= 0:
            print("Jumlah kontributor harus lebih dari 0!")
            return
    except ValueError:
        print("Input tidak valid, harap masukkan angka untuk jumlah kontributor.")
        return

    peserta = []
    print("Masukkan data kontributor:")
    for i in range(num_kontributor):
        print(f"\nData Kontributor ke-{i + 1}:")
        nama = input("Nama kontributor: ")
        while True:
            try:
                sampah_kg = float(input("Jumlah sampah dikumpulkan (kg): "))
                if sampah_kg < 0:
                    print("Jumlah sampah tidak boleh negatif. Silakan masukkan angka yang valid.")
                    continue
                peserta.append({'nama': nama, 'sampah': sampah_kg})
                break
            except ValueError:
                print("Input tidak valid! Harap masukkan angka untuk jumlah sampah.")

    print("\n--- Data Kontributor Sebelum Diurutkan ---")
    for kontributor in peserta:
        print(f"Nama: {kontributor['nama']}, Sampah: {kontributor['sampah']:.2f} kg")

    bubble_sort(peserta)

    print("\n--- Data Kontributor Setelah Diurutkan (Berdasarkan Sampah Terbanyak) ---")
    for i, kontributor in enumerate(peserta):
        print(f"{i + 1}. Nama: {kontributor['nama']}, Sampah: {kontributor['sampah']:.2f} kg")


if __name__ == "__main__":
    main()
