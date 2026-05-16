Judul Program  :  Program Manajemen Riwayat Pencarian

Program ini merupakan contoh implementasi dari _stack array_ pada Python. Program ini berfungsi sebagai suatu sistem
yang memungkinkan pengguna untuk menyimpan informasi mengenai riwayat pencarian yang dilakukan pada suatu mesin
pencarian serta melihat dan/atau menghapus informasi yang diunggah sesuai dengan kebutuhan dari pengguna tersebut.
Alasan pemilihan tema ini adalah karena ketika saya mengikuti pembelajaran mengenai _stack_ dan _queue_ pada
pertemuan ke-empat Praktikum Struktur Data, saya mendapati bahwa fitur _undo_ dan _redo_ memiliki karakteristik yang
sama dengan _stack_, sehingga menjadi inspirasi yang saya gunakan dalam pengerjaan tugas akhir ini.

Gambar Source Code:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-16%20204528.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-16%20204631.png)

Pada program ini, terlihat pada baris pertama sebuah class bernama SearchHistory yang berfungsi sebagai
_template_ untuk menggabungkan semua fungsi pada program ini sehingga dapat memudahkan dalam mengatur dan melihat.
Pada baris ke 2-5 merupakan bagian dimana fungsi "__init__" terdefinisikan, di mana fungsi ini berperan sebagai
bagian dari program yang akan menangani elemen-elemen pada _array_. Fungsi ini mendefinisikan variabel self 
yang terbatasi sehingga hanya dapat memuat sepuluh elemen saja. Kemudian, terdapat variable self.MAX yang
berfungsi untuk menyimpan informasi kapasitas _array_ sehingga tidak dapat diubah, diikuti oleh self.history yang
akan menyimpan informasi pencarian, dan self.top_idx yang berfungsi sebagai inisiator atribut indeks terakhir/teratas.

Pada baris 7-8 terdapat definisi fungsi is_empty(self) yang berfungsi untuk memeriksa apakah _array_ kosong atau tidak. Setelah itu, pada baris 10-11 terdapat definisi fungsi is_full(self) yang berfungsi untuk memeriksa apakah _array_ penuh atau tidak. 

Baris 13-19 merupakan bagian di mana fungsi tambah_pencarian didefinisikan, di mana fungsi
ini berperan untuk meminta input dari pengguna dan merekam informasi yang didapatkan. Dalam fungsi ini, terdapat
suatu kondisi _if_ di mana apabila _array_ penuh, maka akan dikembalikan _print_ yang memberitahu bahwa riwayat pencarian penuh, lalu dijalankan _return_. Bila tidak, maka program akan memasukkan informasi yang dimasukkan
pada self.history[self.top_idx] yang akan menyimpan indeks dan isi dari elemen tersebut, diakhiri dengan _print_ yang menyatakan bahwa penambahan berhasil.

Baris 21-28 merupakan bagian yang mendefinisikan fungsi batalkan_pencarian(self), di mana fungsi ini berperan sebagai fitur penghapus pencarian terakhir. Ketika dijalankan, fungsi ini akan menjalankan fungsi _if_ yang memeriksa apakah _array_ kosong atau tidak. Bila kondisi terpenuhi, maka program akan menjalankan _print_ yang memberitahu bahwa riwayat pencarian kosong dan pembatalan tidak bisa dilakukan, lalu dikembalikan _return_ None. Bila tidak, program akan menghapus masukan terakhir dari pengguna dan menyimpan informasi tersebut dalam _removed_query_ sehingga dapat dipanggil dalam fungsi _print_ dan dikembalikan dengan _return_. 

Baris 30-35 merupakan bagian pendefinisian fungsi lihat_pencarian_baru(self), di mana fungsi ini berperan sebagai fitur bagi pengguna untuk dapat melihat pencarian terakhir yang dilakukan tanpa menghapus informasi tersebut. Kondisi _if_ self.is_empty() akan mengembalikan _print_ yang memberitahukan bahwa riwayat pencarian kosong dan tidak ada informasi untuk dilihat. Bila tidak dipenuhi, maka program akan menjalankan _print_ yang akan memberitahu pencarian terakhir yang dilakukan serta mengembalikan informasi tersebut melalui _return_.

Baris 37-44 merupakan bagian yang mendefinisikan fungsi tampilkan_riwayat(self), di mana fungsi ini berperan untuk menunjukkan riwayat pencarian yang telah dilakukan oleh pengguna. Terdapat kondisi _if_ yang akan mengembalikan _print_ bahwa riwayat pencarian kosong ketika terpenuhi. Apabila tidak, maka program akan menjalankan fungsi _for loop_ yang akan memanggil informasi elemen-elemen pada self.top_idx dari masukkan paling lama hingga yang terbaru, ditunjukkan dengan fungsi print(f""), dan dilapisi dengan _print_ "=====" dari atas dan bawah yang akan berfungsi sebagai "kotak" pemuat informasi. 

Pada baris 47-78 termuat fungsi main() yang akan menjadi kerangka utama program, di mana bagian inilah yang akan termuat ketika pengguna menjalankan program. Fungsi ini akan memanggil fitur-fitur program melalui history_manager yang akan memuat _class_ SearchHistory. Setelah itu, terdapat pilih = 0 yang akan menginisialisasi opsi masukan pengguna, diikuti oleh _while_ loop pilih != 5: yang akan meminta pengguna untuk memilih antara lima opsi, yaitu tambah pencarian baru, batalkan pencarian terakhir, lihat pencarian baru, tampilkan semua riwayat, dan keluar. Setelah itu, program akan mencoba (_try_) untuk meminta input dari pengguna mengenai pilihan yang ingin dijalankan. Apabila yang dimasukkan tidak sesuai dengan tipe data _int_, maka program akan menjalankan _ValueError_ yang memberitahu pengguna bahwa input tidak valid, lalu _continue_. Program akan melakukan hal yang berbeda berdasarkan pilihan mana yang dimasukkan oleh pengguna; memilih nomor 1 akan membuat program meminta pengguna untuk memasukkan informasi pencarian, diikuti kondisi _if_ yang akan menyimpan informasi pada history_manager bila dipenuhi dan mengembalikan pemberitahuan gagal bila tidak. Memilih nomor 2 akan memanggil fungsi pembatalan pencarian. Nomor 3 akan memanggil fungsi lihat pencarian terbaru. Nomor 4 akan memanggil fungsi penampilan riwayat pencarian. Terakhir, nomor 5 akan menghentikan program dan mengembalikan _print_ bahwa program selesai digunakan. Ketika masukan yang diterima tidak termasuk antara nomor 1-5, maka program akan mengembalikan _print_ bahwa pilihan tidak valid.

Pada belahan terakhir program (baris 81-82, terdapat kondisi _if_ di mana program akan memanggil fungsi main() apabila terpenuhi. Bagian ini akan menjadi fungsi yang memungkinkan program untuk dapat berjalan.

Gambar Output Program:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-16%20210448.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-16%20210525.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-16%20210540.png)

Seperti yang terlihat pada gambar output, pengguna menggunakan opsi 1 sebanyak tiga kali untuk memasukkan informasi pencarian yang telah dilakukan, yaitu "Orphie Rerun", "WD40", dan "Ketoconazole". Setelah itu, pengguna memasukkan nomor 3 untuk melihat pencarian terakhir yang dilakukan, di mana program menunjukkan bahwa pencarian terakhir yang dilakukan adalah "Ketoconazole". Kemudian, pengguna menjalankan opsi 4 yang menunjukkan semua riwayat pencarian pengguna. Setelah dijalankan, terlihat ketiga pencarian yang telah dimasukkan dari yang terbaru hingga yang terlama. Lalu, pengguna memasukkan opsi 2 untuk menghapus pencarian terakhir yang dilakukan, menyebabkan program untuk menghapus "Ketoconazole" dari daftar riwayat pencarian. Pengguna lalu memasukkan nomor 3 lagi untuk melihat pencarian terbaru setelah penghapusan, di mana program sekarang menyatakan bahwa "WD40" merupakan pencarian terbaru pengguna. Setelah itu, pengguna memasukkan nomor 4 lagi untuk memuat daftar riwayat pencarian. Sesuai dengan gambar output, terlihat bahwa hanya tersisa dua elemen pada daftar tersebut, yaitu "WD40" dan "Orphie Rerun", di mana "WD40" merupakan pencarian terbaru dan "Orphie Rerun" merupakan pencarian terlama. Terakhir, setelah semua ini pengguna memutuskan untuk berhenti menggunakan program, sehingga pengguna memilih opsi 5 yang menghentikan program dan mengakhiri sesi penggunaan.

Link Video (YouTube)  : f
