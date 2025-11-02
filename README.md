🛡️ Proyek Enkripsi AES-256 (UTS Kriptografi)

🔑 Ikhtisar Proyek
Proyek ini adalah implementasi Advanced Encryption Standard (AES) 256-bit dengan mode GCM (Galois/Counter Mode), yang berfungsi sebagai tugas individu mata kuliah Kriptografi. Aplikasi ini dibangun menggunakan Python dan framework Streamlit, yang menyediakan interface web interaktif dan modern.

Tujuan utama proyek ini adalah mendemonstrasikan fungsi enkripsi dan dekripsi menggunakan algoritma modern yang aman dan kompleks, sekaligus memenuhi syarat implementasi fungsi backend pada arsitektur aplikasi.

✨ Fitur Utama dan Bukti Kompleksitas (Backend Logic)
Proyek ini menonjol karena menggunakan algoritma standar industri dan fitur keamanan tinggi, yang semuanya berjalan di sisi backend (server Python Streamlit):

Algoritma Modern AES-256: Menggunakan panjang kunci 256-bit, yang merupakan standar keamanan tertinggi dan paling kompleks di antara AES, jauh melampaui algoritma klasik (seperti Caesar atau Vigenère).

Key Derivation (Hashing SHA256): Kata kunci (password) pengguna tidak digunakan secara langsung. Backend terlebih dahulu memprosesnya melalui Hashing SHA256 untuk menghasilkan kunci 32-byte (256-bit) yang aman.

Mode GCM (Integrity Check): Implementasi menggunakan mode GCM yang menghasilkan Nonce dan Tag Otentikasi bersamaan dengan ciphertext.

Ini memastikan bahwa ciphertext tidak dapat dimodifikasi oleh pihak ketiga tanpa terdeteksi (Integritas Data).

Jika kunci salah atau ciphertext dirusak, proses verifikasi Tag akan gagal, dan backend akan mengembalikan pesan error.

Arsitektur Backend: Semua logika krusial (Hashing, Nonce Generation, Enkripsi, Dekripsi, dan Verifikasi Tag) dieksekusi oleh fungsi Python di server Streamlit.

🛠️ Cara Menjalankan Aplikasi
Aplikasi ini memerlukan Python 3.7+ dan beberapa library kriptografi.

1. Prasyarat
Pastikan Anda telah menginstal pip dan library yang diperlukan:

Bash

pip install streamlit pycryptodome
2. Eksekusi Program
Simpan kode di file app_aes.py. Jalankan melalui Terminal di folder proyek:

Bash

streamlit run app_aes.py
3. Demo Singkat
ENKRIPSI: Masukkan Plaintext dan Kata Kunci. Klik tombol. Output adalah gabungan Nonce + Ciphertext + Tag (Base64).

DEKRIPSI: Gunakan hasil ciphertext dan Kata Kunci yang sama untuk mendapatkan Plaintext kembali.

TES KEAMANAN: Coba Dekripsi dengan Kata Kunci yang salah untuk melihat fitur verifikasi backend yang menampilkan pesan error.

🔗 Kontak
Nama: Karina Ikhwani

NIM: 312310436

Mata Kuliah: Kriptografi (UTS Project)