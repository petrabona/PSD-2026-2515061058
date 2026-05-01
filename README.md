Judul Program  :  Program Sortir Kontributor Pembersihan Sampah

Program ini merupakan contoh implementasi dari _bubble sorting_ pada _Python_. Program ini berfungsi sebagai suatu sistem yang
memungkinkan pendataan pembersihan sampah berdasarkan jumlah yang telah dibersihkan dalam unit kg. Alasan pemilihan tema ini adalah
karena hal ini merefleksikan ketidaksadaran masyarakat mengenai dampak negatif yang dibawakan oleh sampah-sampah yang tidak ditangani
dengan baik, sehingga diharapkan program seperti ini dapat digunakan sebagai alat penyusunan data bagi sebuah tempat pembuangan umum
dan sebagai media penyampaian informasi kepada masyarakat mengenai aktivitas tiap individu yang melibatkan pembuangan limbah.

Program ini menggunakan fungsi _bubble sort_, yaitu sebuah algoritma yang menyusun sekumpulan data dengan cara menelusuri data secara
berulang dari elemen pertama hingga terakhir yang kemudian data-data tersebut akan dibandingkan berdasarkan pasangan yang bersebelahan.

Gambar Source Code:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-01%20225109.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-01%20225121.png)

Baris 1-4 merupakan bagian yang berfungsi untuk mendefinisikan fungsi tukar(arr, i, j), yang di mana indeks untuk dua variabel yang akan
dibandingkan didefinisikan sebagai arr[i] untuk indeks pertama dan arr[j] untuk indeks kedua. Pada bagian ini terdapat juga variabel temp
yang berfungsi sebagai tempat peletakan nilai indeks arr[i] dan arr [j] secara sementara ketika kedua indeks akan dibandingkan sehingga 
dapat digunakan apabila kondisi penyusunan telah terpenuhi.

Pada baris 6-11 terdapat barisan program yang mendefinisikan bubble_sort(peserta), yang di mana fungsi ini akan menjadi fitur utama program
ini. Pada bagian inilah data yang dimasukkan pengguna akan disusun berdasarkan jumlah yang terbesar hingga yang terkecil. Variabel n berfungsi
sebagai tempat yang akan menampung semua nama peserta/kontributor yang akan dimasukkan oleh pengguna ketika program berjalan. Setelah itu,
terdapat sebuah perulangan for loop yang berfungsi sebagai loop bagian luar yang akan menangani jumlah indeks yang akan disortir sehingga
program akan terus menyusun data yang belum disortir dan meninggalkan yang sudah berada pada posisi yang semestinya. Perulangan for j
in range(n - i - 1) di bawahnya memiliki fungsi sebagai baris kode yang akan menangani pembandingan variabel sehingga program akan 
membandingkan indeks yang bertetanggaan. Kemudian, terdapat kondisi if yang di mana program akan menjalankan fungsi tukar apabila
data pada indeks pertama ditemukan berjumlah lebih kecil dari data pada indeks selanjutnya.

Lalu, terdapat definisi main() yang akan menjadi bagian output dari program. Mula-mula, program akan mencoba (try) untuk meminta jumlah
kontributor yang akan disusun datanya. Apabila jumlah yang dimasukkan kurang atau sama dengan 0, maka program akan mengembalikan notifikasi
yang meminta bahwa jumlah kontributor harus lebih dari 0, lalu dikembalikan pada permintaan awal (return). Selain itu, apabila pengguna
memasukkan data yang tidak berupa integer, maka program akan mengembalikan _ValueError_ yang akan memprint bahwa input yang dimasukkan tidak
valid, lalu return pada input awal.

Baris peserta = [] merupakan bagian yang akan menyimpan data-data peserta yang akan dimasukkan oleh pengguna. Di bawahnya terdapat sebuah line
yang akan memprint sebuah permintaan terhadap pengguna untuk memasukkan nama dan jumlah kontribusi tiap indeks melalui fungsi print(f"...). Pada
baris ke-27 terdapat variabel nama yang akan meminta pengguna untuk memasukkan nama dari tiap kontributor yang dimasukkan pada fungsi
num_kontributor sebelumya. Ketika nama telah dimasukkan, maka program akan menjalankan sebuah perintah untuk mencoba (try) untuk meminta data
mengenai jumlah sampah yang telah dibersihkan melalui sampah_kg, yang di mana apabila data yang dimasukkan merupakan nomor negatif, maka program
akan mengembalikan notifikasi tidak valid, lalu di-continue. Setelah itu, program menjalankan baris peserta.append yang akan menggabungkan nama
peserta beserta jumlah kontribusi kebersihan sampah masing-masing, yang kemudian akan di-break. Apabila saat bagian try pengguna memasukkan data
non-angka, maka program akan mengembalikan ValueError yang memberitahu pengguna bahwa input tidak valid.

Pada baris 39, terdapat fungsi print("\n--- Data Kontributor Sebelum Diurutkan ---") yang berfungsi untuk memuat interface dari program ketika
dieksekusi oleh pengguna, yang diikuti oleh perulangan for loop yang akan memprint nama-nama peserta yang dimasukkan beserta kontribusi
pembersihan masing-masing sebelum disusun oleh bubble sort.
Setelah semua ini, pada baris 43 merupakan sebuah pemanggilan pada fungsi bubble_sort(peserta) yang akan melakukan sorting pada data-data
yang telah dimasukkan oleh pengguna ketika program dijalankan. Setelah itu, pada baris 45 terdapat sebuah baris print yang memiliki fungsi
yang sama dengan yang berada pada baris 39, dengan perbedaan bahwa print ini menunjukkan data setelah disusun oleh bubble sort. Perulangan
for loop yang ada selanjutnya akan memprint setiap nama kontributor dan jumlah pembersihannya yang telah dinomorkan melalui fungsi enumerate.

Terakhir, pada baris 50-51 terdapat kondisi if yang di mana ketika __name__ sesuai dengan "__main__", maka program akan memanggil fungsi
main(), yang akan memungkinkan program untuk berjalan.

Gambar Output Program:
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-01%20225136.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-01%20225159.png)
![Gambar Source Code](https://github.com/petrabona/PSD-2026-2515061058/blob/main/assets/Screenshot%202026-05-01%20225210.png)

Pada gambar output pertama dan kedua, terlihat informasi yang telah dimasukkan oleh pengguna yakni nama-nama tiap kontributor beserta kontribusi pembersihan
sampah yang dilakukan (diukur dalam kg). Terdapat 4 kontributor yang dimasukkan, yakni Jun, Jin, Jon, dan Jan, beserta kontribusinya masing-masing
yaitu 15, 20, 7, dan 5 kg.
Pada gambar ketiga terurai informasi mengenai susunan nama kontributor pembuangan sampah beserta jumlah yang dibersihkan sebelum dan setelah disusun.
Seperti yang ditunjukkan, susunan sebelum disortir terlihat tidak rapi dengan jumlah berat terletak tidak sesuai posisinya, di mana hal ini 
telah diselesaikan ketika fungsi bubble sort dijalankan sehingga termuat daftar kontributor yang telah disortir dari yang terbesar hingga yang terkecil.

Link Video (YouTube)  :  f
