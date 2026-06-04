Judul Program  :  Program Manajemen Penitipan Barang di Mall

Program ini merupakan contoh implementasi dari _Hash Map_ pada Python. Program ini berfungsi sebagai sistem yang memungkinkan pengguna untuk melakuka proses penanganan barang titipan pengunjung pada sebuah mall dengan fitur kategorisasi indeks berdasarkan kunci (_key_) dari barang (_value_) tersebut, sehingga dapat dengan mudah dicari dan dikembalikan kepada pengunjung yang terkait tanpa perlu melakukan pencarian barang secara manual. Alasan dari pemilihan tema ini adalah karena saya terinspirasi oleh sistem penanganan barang titipan pelanggan yang ada pada suatu mall yang saya kunjungi beberapa hari sebelumnya.

Gambar Source Code:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-06-04%20222209.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-06-04%20222230.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-06-04%20222230.png)

Baris 1 - 5 merupakan bagian di mana class Node didefinisikan, di mana di dalamnya terdapat fungsi "**init**(self, key, value)" yang berperan untuk menginisialisasi key (nomor loker), value (deskripsi barang), dan next yang digunakan untuk menghubungkan node satu dengan node lainnya pada metode Separate Chaining.

Baris 7 - 10 merupakan bagian yang mendefinisikan class HashMapSeparateChaining. Pada bagian ini terdapat fungsi "**init**(self, size=10)" yang bertanggung jawab untuk menginisialisasi ukuran tabel hash sebesar 10 serta membuat tabel berupa list yang seluruh elemennya berisi None.

Baris 12 - 13 merupakan bagian yang mendefinisikan fungsi hash_function. Fungsi ini bertanggung jawab dalam menentukan indeks penyimpanan data berdasarkan key yang dimasukkan pengguna. Program menggunakan operasi modulus (%) terhadap ukuran tabel sehingga menghasilkan indeks yang berada dalam rentang 0 hingga ukuran tabel dikurangi satu.

Baris 15 - 25 merupakan bagian yang mendefinisikan fungsi insert, di mana bagian ini berfungsi untuk menangani proses penitipan barang ke dalam sistem. Program mula-mula menentukan indeks menggunakan hash_function. Setelah itu program memuat node pada indeks tersebut ke dalam variabel current. Kemudian program menjalankan while loop yang akan terus berjalan selama current tidak kosong. Di dalam perulangan tersebut, program memeriksa apakah key yang dimasukkan sudah ada. Jika ditemukan key yang sama, maka value akan diperbarui dan fungsi dihentikan menggunakan return. Jika tidak ditemukan, program akan membuat node baru, menetapkan node tersebut pada awal linked list di indeks yang sesuai, lalu menjadikannya elemen pertama pada bucket tersebut.

Baris 27 - 34 merupakan bagian yang mendefinisikan fungsi search. Fungsi ini bertanggung jawab dalam menangani pencarian barang berdasarkan nomor loker. Program terlebih dahulu menentukan indeks menggunakan hash_function, kemudian memuat node pada indeks tersebut ke dalam current. Setelah itu program menjalankan while loop yang akan membandingkan key yang dicari dengan key pada setiap node. Jika ditemukan kecocokan, maka program mengembalikan value dari node tersebut. Jika seluruh node telah diperiksa dan tidak ditemukan kecocokan, maka program mengembalikan None.

Baris 36 - 49 merupakan bagian yang mendefinisikan fungsi remove_key. Fungsi ini bertanggung jawab dalam menangani pengambilan barang dari sistem penitipan. Program menentukan indeks dari key yang dimasukkan, kemudian menginisialisasi current dan prev. Selanjutnya program menjalankan while loop untuk menelusuri linked list pada bucket tersebut. Apabila key ditemukan, program akan memeriksa apakah node yang ditemukan merupakan node pertama. Jika ya, maka program akan mengubah isi bucket menjadi node berikutnya. Jika tidak, maka program akan menghubungkan node sebelumnya langsung ke node setelahnya sehingga node yang dihapus tidak lagi terhubung. Setelah proses berhasil, program mengembalikan nilai True. Jika key tidak ditemukan hingga akhir pencarian, maka program mengembalikan nilai False.

Baris 51 - 59 merupakan bagian yang mendefinisikan fungsi display. Fungsi ini bertanggung jawab dalam menampilkan seluruh daftar barang yang dititipkan pada sistem. Program akan menampilkan setiap indeks pada tabel hash beserta seluruh node yang tersimpan di dalamnya. Untuk setiap bucket, program menjalankan while loop yang akan menampilkan pasangan key dan value hingga tidak ada node lagi yang terhubung. Setelah semua node ditampilkan, program akan mencetak tulisan "KOSONG" sebagai penanda akhir bucket.

Baris 61 - 63 merupakan bagian yang mendefinisikan fungsi clear_all. Fungsi ini bertanggung jawab dalam menangani fitur penghapusan seluruh data titipan barang. Program membuat ulang tabel hash dengan seluruh elemennya berisi None sehingga seluruh data yang sebelumnya tersimpan akan hilang. Setelah itu program menampilkan notifikasi bahwa semua titipan barang telah dibersihkan.

Baris 65 - 66 merupakan bagian yang mendefinisikan fungsi main. Pada bagian ini program membuat objek hashmap dari class HashMapSeparateChaining yang akan digunakan untuk menyimpan seluruh data penitipan barang.

Baris 68 - 113 merupakan bagian yang berfungsi sebagai antarmuka interaksi dengan pengguna. Program akan terus berjalan menggunakan while loop hingga pengguna memilih untuk mengakhiri sesi. Pada bagian ini program menampilkan enam pilihan menu, yaitu Titip Barang, Lihat Daftar Barang Dititipkan, Cari Barang, Ambil Barang, Bersihkan Semua Titipan, dan Akhiri Sesi. 
Jika pengguna memasukkan angka 1, maka program akan meminta nomor loker dan deskripsi barang. Setelah itu program akan memanggil fungsi insert untuk menyimpan data tersebut ke dalam hash map. Jika nomor loker yang dimasukkan bukan bilangan bulat, maka program akan menampilkan pesan kesalahan. 
Jika pengguna memasukkan angka 2, maka program akan memanggil fungsi display untuk menampilkan seluruh barang yang sedang dititipkan beserta posisi bucket tempat data tersebut disimpan. 
Jika pengguna memasukkan angka 3, maka program akan meminta nomor loker yang ingin dicari. Selanjutnya program menjalankan fungsi search untuk mencari barang tersebut. Apabila ditemukan, program akan menampilkan deskripsi barang yang tersimpan. Jika tidak ditemukan, program akan menampilkan pesan bahwa barang tidak ditemukan. Program juga akan menampilkan pesan kesalahan apabila input bukan bilangan bulat. 
Jika pengguna memasukkan angka 4, maka program akan meminta nomor loker barang yang akan diambil. Selanjutnya program menjalankan fungsi remove_key untuk menghapus data tersebut dari hash map. Apabila berhasil, program akan menampilkan notifikasi keberhasilan. Jika nomor loker tidak ditemukan, program akan menampilkan pesan bahwa barang tidak ditemukan. Program juga akan menampilkan pesan kesalahan apabila input bukan bilangan bulat. 
Jika pengguna memasukkan angka 5, maka program akan menjalankan fungsi clear_all yang akan menghapus seluruh data titipan barang dari sistem. 
Jika pengguna memasukkan angka 6, maka program akan menampilkan pesan bahwa sesi manajemen penitipan barang telah diakhiri dan menghentikan perulangan menggunakan break.
Apabila pengguna memasukkan pilihan selain angka 1 sampai 6, maka program akan menampilkan pesan bahwa pilihan tidak valid dan meminta pengguna untuk memasukkan pilihan yang benar.

Baris 115 - 116 merupakan bagian yang menjalankan program utama. Pada bagian ini fungsi main() akan dipanggil apabila file dijalankan secara langsung, yaitu ketika kondisi **name** == "**main**" terpenuhi.


Gambar Output Program:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-22%20133742.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-22%20133758.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-22%20133908.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-22%20133924.png)

Pada gambar output program, terlihat pengguna menggunakan fungsi nomor 1 untuk memasukkan pasien pasien baru dalam urutan berikut: 1, 2, 3, 4, 5, 6, 7. Setelah pengguna memasukkan semua informasi antrean pasien yang diinginkan, pengguna lanjut dengan menggunakan fitur pada nomor 3 yang memuat daftar yang berisikan pasien-pasien yang telah diisi sebelumnya. Setelah itu, pengguna menggunakan fitur nomor 4 untuk mencari nomor pasien setelah pasien ke 6, di mana program menunjukkan bahwa pasien setelah nomor 6 adalah nomor 7. Lalu, pengguna menggunakan fitur nomor 5 untuk mencari nomor pasien sebelum 6, di mana program menunjukkan bahwa pasien sebelum nomor 6 adalah nomor 5. Pengguna kemudian menggunakan fitur nomor 2 untuk menghapus beberapa antrean pasien yang telah dilayani, yaitu 7 dan 6, di mana program menunjukkan keberhasilan dalam menghapus data-data tersebut dengan menunjukkan daftar pasien setelah penghapusan (pada penghapusan nomor 7, daftar menjadi [6, 5, 4, 3, 2, 1], dan setelah penghapusan nomor 6, daftar menjadi [5, 4, 3, 2, 1]. Terakhir, setelah pengguna merasa ingin menyelesaikan sesi penggunaan program, pengguna memasukkan nomor 6 pada sistem yang merupakan opsi yang akan menghentikan sesi penggunaan sistem.

Link YouTube: 
