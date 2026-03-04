Dokumentasi Program Diffie-Hellman Key Exchange

Repositori ini memuat implementasi sederhana dari protokol Diffie-Hellman key exchange menggunakan bahasa pemrograman Python tanpa memanfaatkan library kriptografi tambahan. Program ini bertujuan untuk memperlihatkan bagaimana dua pihak dapat membentuk kunci rahasia yang identik melalui jaringan publik tanpa pernah mengirimkan kunci privat mereka.

Implementasi ini dibuat untuk keperluan pembelajaran dan simulasi konsep dasar pertukaran kunci dalam kriptografi asimetris.
Alur Eksekusi Program

Program berjalan mengikuti tahapan logika berikut:

1️.Definisi Fungsi Perpangkatan Modular
Program terlebih dahulu mendeklarasikan fungsi power_mod.
Fungsi ini mengimplementasikan metode Square and Multiply untuk menghitung nilai:
(base^exponent) mod modulus

Metode ini digunakan agar perhitungan bilangan berpangkat besar tetap efisien dan tidak membebani proses komputasi.

2️.Penentuan Parameter Publik
Program menetapkan dua parameter yang dapat diketahui oleh semua pihak:

p = 23 (bilangan prima)
g = 5 (generator)
Kedua nilai ini bertindak sebagai parameter dasar dalam proses pertukaran kunci.

3️.Input Kunci Privat
Pengguna diminta untuk memasukkan secara manual:

Nilai kunci privat Alice (x)
Nilai kunci privat Bob (y)
Nilai tersebut bersifat rahasia dan tidak pernah dikirimkan melalui jaringan.

4️.Perhitungan Kunci Publik
Setelah menerima input, program menghitung:
Kunci publik Alice
A = g^x mod p

Kunci publik Bob
B = g^y mod p
Nilai A dan B inilah yang diasumsikan dikirim melalui saluran komunikasi publik.

5.Simulasi Pertukaran Kunci
Program menampilkan nilai A dan B sebagai representasi proses pengiriman kunci publik melalui jaringan terbuka.

6.Perhitungan Shared Secret
Tahap berikutnya adalah pembentukan kunci rahasia bersama:

Alice menerima B dan menghitung:
S = B^x mod p
Bob menerima A dan menghitung:
S = A^y mod p

Karena sifat matematika perpangkatan modular:
(g^x)^y = (g^y)^x
Maka kedua pihak akan memperoleh nilai S yang sama.

7.Verifikasi Akhir
Program membandingkan hasil perhitungan shared secret di sisi Alice dan Bob.
Jika nilainya identik → pertukaran kunci berhasil.
Jika berbeda → terjadi kesalahan pada proses input atau perhitungan.
