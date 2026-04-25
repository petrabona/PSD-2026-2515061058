Judul Program  : Aplikasi Manajer Tugas

Program ini merupakan salah satu contoh implementasi dari struktur data _List 1D_ pada _Python_. Program ini berfungsi sebagai
suatu "to-do list' atau pengingat mengenai tugas-tugas yang harus dikerjakan. Alasan pemilihan tema ini adalah karena hal ini
merefleksikan diri saya sebagai seorang mahasiswa, yang di mana program seperti ini dapat membantu sebagai tambahan informasi
dalam mempertimbangkan bagaimana saya akan mengatur penggunaan waktu.

Program ini menggunakan struktur data _1D List_ yang melibatkan penggunaan _append_ untuk penomoran data yang dimasukkan,
_indexing_ untuk memberikan referensi penunjuk pada tiap data yang dimasukkan, dan _push/pop_ yang berfungsi sebagai metode untuk
memanipulasi isi data dalam _list_ yang dibuat.

Gambar Source Code:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-04-25%20185602.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/ddabfe1173da8c6c952e53c4429540a85ab3a9df/assets/Screenshot%202026-04-25%20185623.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/72b7ba6de40b5fb19c6c3969f44f539dadbb2e2c/assets/Screenshot%202026-04-25%20185647.png)

Baris 1-7 merupakan bagian yang mendefinisikan fungsi _menu()_, yang akan menjadi display laman utama program ini. Terdapat fungsi
print untuk title nya dan lima fungsi seterusnya yang memuat informasi mengenai 5 perintah yang dapat dieksekusi dalam program.
Pada baris 9 terdapat definisi fungsi _main()_ yang akan berisi sebagian besar dari program ini. Pada fungsi inilah semua fitur-
fitur program berada. Seterusnya, terdapat _tugas_ yang berfungsi sebagai medium dari data yang akan dimasukkan. Bagian [] berfungsi
sebagai tempat yang akan menunjukkan ada atau tidak tanda centang pada data yang dimasukkan. Bagian _running = True_ memastikan program
berjalan kecuali diperintahkan menjadi _False_. Ini dipastikan oleh perintah _while running:_. Setelah itu, terdapat fungsi try yang akan
mencoba untuk mengambil input dari pengguna mengenai pilihan apa yang ingin diambil. baris _except ValueError_ digunakan apabila pengguna
memasukkan input yang tidak valid sebagai sebuah pengaman yang diikuti oleh _continue_ sehingga program akan terus berjalan.

Dari baris 20-66 akan berisi fungsi _if_ dan _elif_ yang masing-masing diberikan fungsi yang berbeda berdasarkan menu yang ada pada laman
utama. Pemanggilan _if choice == 1_ akan menyebabkan program untuk meminta nama tugas yang akan disimpan oleh baris _append_ dan mengembalikan
_print_ yang memberikan notifikasi bahwa pemasukkan nama berhasil. _elif choice == 2_ berfungsi untuk menunjukkan tugas-tugas yang telah 
dimasukkan. Apabila dipanggil saat _list_ kosong, maka program akan mengembalikan notifikasi bahwa daftarnya kosong, lalu _continue_. 
Selain itu, program akan menunjukkan informasi tugas yang dimasukkan. Fungsi _for_ digunakan untuk menomorkan tugas, yang kemudian
diikuti oleh _status_ yang akan memberikan centang pada [] apabila telah ditanda selesai menggunakan perintah _choice_ ke-3. Semua ini
kemudian akan di-_print_ sebagai output. _elif choice == 3_ berfungsi untuk menandakan tugas yang telah selesai. Apabila daftar tugas
kosong, maka program akan mengembalikan output bahwa daftar kosong, sama seperti pada _choice_ 2, dan _continue_. Selain itu, program
akan mencoba untuk meminta informasi mengenai data mana yang akan ditanda melalui _int(input()_ yang akan disimpan pada _indeks_.
Fungsi _if_ berfungsi untuk memastikan bahwa data yang dipilih benar ada, yang kemudian akan mengembalikan _ValueError_ melalui fungsi
_else_ apabila tidak valid. _elif choice == 4_ berfungsi untuk menghapus nama tugas. Apabila dipanggil saat tidak ada tugas, maka akan
mengoutputkan bahwa daftar kosong, lalu di-_continue_. Selain itu, program akan mencoba untuk meminta data mengenai data mana yang akan
dihapus, yang melibatkan fungsi _if_ dilanjutkan oleh _hapus_tugas_ yang berisi _tugas.pop(indeks)_ untuk menghapuss data. Fungsi
_else_ dan _expect ValueError_ digunakan apabila pengguna memasukkan data yang tidak valid. _elif == 5_ berfungsi untuk menghentikan
program. Apabila dipanggil, bagian ini akan mengubah _running_ menjadi _False_ yang akan menghentikan program. _else_ yang melingkup
semua program ini akan mengembalikan _print_ untuk memberitahu pengguna untuk memasukkan pilihan yang tersedia.

Fungsi _if __ name __ == "__ main __" adalah untuk memanggil _main()_ sehingga program dapat berjalan.

Gambar Output:
![Gambar Output](https://github.com/petrabona/PSD-2026-2515061058/blob/724cc6e5acb8df45ed0930a57fafbaedcabaabfb/assets/Screenshot%202026-04-25%20185821.png)
![Gambar Output](https://github.com/petrabona/PSD-2026-2515061058/blob/3a88b3b34b8d7da7ab56ad47145e4397b64ed0eb/assets/Screenshot%202026-04-25%20185838.png)
![Gambar Output](https://github.com/petrabona/PSD-2026-2515061058/blob/96a9141a8d7c25a81ef1ce705ab41d300d3fb3b0/assets/Screenshot%202026-04-25%20185854.png)

Pada gambar pertama, terlihat saya menginputkan angka 1 sebanyak tiga kali untuk memasukkan tiga jenis nama tugas yang berbeda, yakni
"Aljabar Matriks", "Matematika Diskrit", dan "Bahasa Indonesia" yang kemudian akan disimpan ke dalam _list_ program. Kemudian, saya 
masukkan angka 2 untuk melihat semua tugas, yang di mana dapat terlihat ketiga nama-nama tugas sebelumnya dengan [] yang belum terisi.
Dalam gambar kedua, Saya memasukkan angka 3 dua kali untuk mencentangkan dua tugas, yakni tugas pertama dan ketiga. Setelah itu, saya
memasukkan kembali angka 2 yang di mana terlihat bahwa "Aljabar Matriks" dan "Bahasa Indonesia" tercentang kotak bracketnya. Setelah
itu, saya memasukkan angka 4 untuk menghapus tugas kedua, yang di mana perintah ini menyebabkan program menghapus tugas
"Matematika Diskrit". 
Dalam gambar ketiga, saya masukkan angka 2 untuk melihat kembali daftar tugas, yang di mana terlihat "Aljabar Matriks" dan "Bahasa
Indonesia" dengan bracket tercentang [X] dan hilangnya "Matematika Diskrit" dalam daftar karena perintah 4 sebelumnya.
Setelah semua ini, saya memutuskan untuk mengakhiri sesi penggunaan dengan memasukkan angka 5, yang menyebabkan program berhenti.

Link Video (YouTube)  : https://youtu.be/uUZZQNHEolQ
