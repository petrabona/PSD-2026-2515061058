def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = []
    while True:
        try:
            print("Program Penghitung Jumlah Suara Survey Kualitas Dosen")
            num_elements = int(input("Masukkan jumlah elemen untuk array data: "))
            if num_elements <= 0:
                print("Jumlah elemen harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")

    for _ in range(num_elements):
        while True:
            try:
                element = int(input(f"Masukkan elemen ke-{len(data) + 1} (1-5): "))
                if not (1 <= element <= 5):
                    print("Input harus berupa angka antara 1 dan 5.")
                    continue
                data.append(element)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka.")

    n = len(data)
    print(f"Data array: {data}")
    while True:
        try:
            target = int(input("Masukkan angka yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Angka {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Angka {target} tidak ditemukan.")


if __name__ == "__main__":
    main()