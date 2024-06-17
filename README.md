# Tugas Besar Teori Bahasa dan Automata

Proyek ini adalah implementasi sederhana dari sebuah parser untuk memeriksa kevalidan struktur kalimat berbahasa Indonesia menggunakan Finite Automata (FA) dan Pushdown Automata (PDA). Program ini mengenali kalimat berita aktif dengan struktur:
- S – P – O – K
- S – P – K
- S – P – O
- S – P

## Kelompok Kata
- **Subjek**: `{"aku", "ali", "ani", "dia", "dini"}`
- **Predikat**: `{"makan", "minum", "mandi", "main", "masak"}`
- **Objek**: `{"apel", "ayam", "air", "api", "alat"}`
- **Keterangan**: `{"di_rumah", "di_kantor", "di_sekolah", "di_taman", "di_mall"}`

## Struktur Direktori
- `finite_automata.py`: Berisi fungsi untuk mengenali kata-kata berdasarkan kategori.
- `lexical_analyzer.py`: Berisi fungsi untuk memproses kalimat menjadi token menggunakan fungsi dari `finite_automata`.
- `parser.py`: Berisi fungsi untuk memeriksa kevalidan struktur kalimat menggunakan token dari `lexical_analyzer`.
- `main.py`: Berisi fungsi utama untuk menjalankan program dan interaksi dengan pengguna.
- `README.md`: Berisi informasi tentang proyek dan cara menjalankannya.

## Instalasi
1. Pastikan Python telah terinstal di sistem Anda. Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).
2. Clone repositori atau salin semua file ke dalam direktori proyek.

## Cara Menjalankan Program
1. Buka terminal atau command prompt.
2. Navigasi ke direktori proyek.
3. Jalankan perintah berikut:
    ```sh
    python main.py
    ```

## Penggunaan
1. Setelah menjalankan `main.py`, masukkan kalimat yang ingin diuji ketika diminta.
2. Program akan menampilkan token yang dikenali dan status kevalidan kalimat.

### Contoh Kalimat
- **Kalimat Valid**:
    - `aku makan apel di_rumah`
    - `ali minum air di_kantor`
    - `ani mandi di_taman`
    - `dia main alat di_sekolah`
    - `dini masak ayam di_mall`

- **Kalimat  Invalid**:
    - `aku di_rumah makan apel` (Keterangan sebelum Predikat)
    - `apel aku makan` (Objek sebelum Subjek)
    - `makan ali air` (Predikat sebelum Subjek)
    - `dini di_kantor mandi` (Keterangan sebelum Predikat)
    - `mandi ali di_sekolah alat` (Predikat sebelum Subjek)

Untuk keluar dari program, ketik `exit` saat diminta memasukkan kalimat.

## Anggota Kelompok
- Baihaqi Bintang Bahana (1301223175)
- Binta Adimastama (1301223005)
- Putu Arjuna Nurgraha Eka Wana (1301223039)

## Implementasi

### Context-Free Grammar (CFG)
Grammar ini digunakan untuk menentukan struktur kalimat yang valid:

