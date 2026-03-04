Dokumentasi Program Diffie-Hellman Key Exchange

Repositori ini memuat implementasi sederhana dari protokol Diffie-Hellman key exchange menggunakan bahasa pemrograman Python tanpa memanfaatkan library kriptografi tambahan. Program ini bertujuan untuk memperlihatkan bagaimana dua pihak dapat membentuk kunci rahasia yang identik melalui jaringan publik tanpa pernah mengirimkan kunci privat mereka.

Implementasi ini dibuat untuk keperluan pembelajaran dan simulasi konsep dasar pertukaran kunci dalam kriptografi asimetris.

### Alur Eksekusi Program
## Program berjalan mengikuti tahapan logika berikut:

1️.  **Inisialisasi Fungsi Modular**: Program mendefinisikan fungsi power_mod yang menggunakan metode Square and Multiply untuk menghitung perpangkatan dalam sistem modulo secara efisien.

2️.  **Penentuan Parameter Publik**:Program menetapkan dua parameter yang dapat diketahui oleh semua pihak:

* p = 23 (bilangan prima)
* g = 5 (generator)
Kedua nilai ini bertindak sebagai parameter dasar dalam proses pertukaran kunci.

3️.  **Input Kunci Privat**:Pengguna diminta untuk memasukkan secara manual:
* Nilai kunci privat Alice (x)
* Nilai kunci privat Bob (y)

4️.  **Perhitungan Kunci Publik**: Program menghitung:

* A = g^x mod p
* B = g^y mod p

5.  **Pembentukan Shared Secret**: Kedua pihak menghitung kunci rahasia bersama:

* Alice: S = B^x mod p
* Bob: S = A^y mod p

6.  **Verifikasi Akhir**: Program membandingkan hasil shared secret dari kedua sisi. Jika nilainya sama, maka pertukaran kunci berhasil.

## CARA MENJALANKAN PROGRAM

### Prasyarat 
Pastikan anda telah menginstyal python diperangkat anda

Instruksi Menjalankan
  1. Buka terminal atau command prompt.
  2. Navigasikan ke direktori tempat file `bashdifflehellmancode.py` disimpan.
  3. Jalankan perintah berikut:
     ```bash
     python difflehellmancode.py
     ```
  4. Masukkan nilai angka bulat saat diminta untuk kunci privat Alice dan Bob.
  5. Lihat hasil perhitungan kunci publik dan verifikasi shared secret di layar terminal.
