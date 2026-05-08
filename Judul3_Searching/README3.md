Judul Program  :  Program Penghitung Jumlah Suara Survey Kualitas Dosen

Program ini merupakan contoh implementasi dari _Searching_ dalam Python. Program ini berfungsi sebagai sistem yang memungkinkan
pengguna untuk menghitung jumlah suara dari mahasiswa yang didapat setelah memberlakukan survey kualitas dosen. Alasan pemilihan tema ini adalah
karena saya mendapatkan ini setelah menerima beberapa permintaan pengisian kuesioner pembelajaran dari dua dosen berbeda, sehingga saya
terinspirasi untuk menggunakan peristiwa ini sebagai referensi dalam pengerjaan tugas akhir ini.

Program ini menggunakan fungsi _Sequential Searching_, yaitu suatu algoritma yang bekerja dengan cara memeriksa setiap elemen secara berurutan
hingga data yang dicari ditemukan.

Gambar Source Code:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-08%20192305.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-08%20192326.png)

Dalam program ini termuat dua definisi fungsi yang membentuk sistem secara keseluruhan, yakni sequential_search(data, n, target) dan main().
Pada baris 1 - 8 merupakan bagian yang berfungsi untuk mendefinisikan fungsi sequential_search(data, n, target) yang akan menjadi mekanisme
pencari pada program ini. i = 0 merupakan baris yang akan menginisialisasi indeks pada program sehingga akan dimulai dari 0. Setelah itu, 
terdapat juga counter = 0 yang berfungsi sebagai bagian penghitung urutan indeks pada tiap elemen. Kemudian, fungsi while loop pada baris
ke-4 digunakan ketika indeks kurang dari n, di mana n merupakan jumlah elemen yang dimasukkan. Ketika kondisi while terpenuhi, program akan
menjalankan kondisi if data[i] == target, di mana apabila isi indeks yang sedang dicari ditemukan sama dengan target, maka akan dijalankan
line counter += 1 diikuti oleh fungsi return counter.

Baris 11 - 48 merupakan bagian yang mendefinisikan fungsi main() yang akan menjadi bagian utama dari program ini. Baris data[] berfungsi
sebagai tempat yang akan menampung semua informasi mengenai elemen-elemen yang dimasukkan oleh pengguna. Setelah itu, terdapat fungsi
while True yang diikuti oleh fungsi try, di mana program akan mencoba untuk meminta input pengguna mengenai jumlah elemen untuk array data
yang ingin diproses. Apabila jumlah yang dimasukkan kurang dari atau sama dengan 0, maka program akan mengembalikan sebuah fungsi print
yang akan memberitahu pengguna bahwa input tidak valid, yang kemudian diikuti oleh continue dan break. Selain itu, terdapat juga fungsi
except yang akan terpanggil jika masukan pada bagian try tidak dalam bentuk angka, di mana program akan mengembalikan pesan eror.
Setelah fungsi while True tersebut, terdapat fungsi for loop yang akan terus berjalan berdasarkan jumlah array yang dimasukkan sebelumnya.
Fungsi ini diikuti oleh kondisi while True di mana program akan mencoba untuk meminta informasi mengenai nilai tiap array dari pengguna
(dari 1 sampai dengan 5). Apabila nomor yang dimasukkan pengguna tidak memenuhi kondisi tersebut, maka program akan mengembalikan notifikasi
bahwa input tidak valid dan pengguna harus memasukkan nomor antara 1 sampai dengan 5, diikuti oleh continue. Kemudian, terdapat fungsi
data.append(element) yang akan menambahkan data yang telah dimasukkan oleh pengguna ke dalam fungsi _data = []_ sebelumnya, ditutup dengan
break. Apabila dalam percobaan try sistem pengguna memasukkan nilai yang bukan angka, maka program akan menjalankan ValueError yang
memberitahu pengguna bahwa input tidak valid.
Setelah fungsi for loop sebelumnya, terdapat deklarasi n yang berfungsi sebagai tempat penampung informasi dalam fungsi data, yang di mana
fungsi ini menyertakan len yang akan mengurutkan tiap elemen yang dimasukkan. Program kemudian akan menjalankan print yang menunjukkan
data array yang telah dimasukkan, diikuti oleh kondisi while True yang akan mencoba untuk meminta pengguna untuk memasukkan nilai angka
yang ingin dicari jumlah totalnya yang diakhiri dengan break. Ketika pengguna memasukkan nilai non-angka, program akan mengembalikan eror
yang menyatakan bahwa input tidak valid. Setelah input try berhasil, program akan menjalankan fungsi sequential_search dengan cara memanggilnya
melalui deklarasi _counter_. Apabila counter menemukan angka yang dicari (counter > 0), maka program akan memberitahu pengguna bahwa angka
telah ditemukan sebanyak {counter} kali. Sebaliknya, jika counter tidak menemukan angka yang diminta, maka program akan mengembalikan notifikasi
bahwa angka {target} tidak ditemukan.

Pada baris 51 - 52, terdapat sebuah kondisi if __name__ == "__main__":, di mana jika terpenuhi, maka program akan memanggil fungsi
main() yang akan memungkinkan program untuk dapat berjalan.

Gambar Output Program:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-08%20192407.png)

Pada output baris pertama terlihat judul dari program yang dibuat diikuti oleh permintaan input dari program ke pengguna untuk memasukkan jumlah
total array yang ingin dimasukkan. Terdapat enam total elemen yang dimasukkan, yakni 4, 4, 5, 4, 3, dan 1. Setelah terinputnya elemen array,
program kemudian menunjukkan data array tersebut setelah digabungkan (4, 4, 5, 4, 3, 1). Selanjutnya, program memuat sebuah permintaan untuk
memasukkan nilai apa yang ingin dicari oleh pengguna (antara 1 sampai dengan 5), di mana pengguna memasukkan angka 4. Terakhir, program
menunjukkan pengeluarannya bahwa angka 4 ditemukan sebanyak tiga kali.

Link Video (YouTube)  : https://youtu.be/PJ5BqbmB4VM

Gambar Pengerjaan Binary Interpolation Searching:
![Gambar Binary](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/binary_interpolation_searching.png)
