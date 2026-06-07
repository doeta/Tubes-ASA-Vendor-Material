# Perbandingan Algoritma DP, B&B, dan SA dalam Optimasi Pemilihan Vendor Material Bangunan Berdasarkan RAB

Proyek ini merupakan implementasi Tugas Besar Mata Kuliah **Analisis dan Strategi Algoritma (ASA)**. Proyek ini memodelkan permasalahan pemilihan vendor material bangunan sebagai *Multiple-Choice Knapsack Problem* (MCKP) dan menyelesaikannya menggunakan tiga algoritma berbeda untuk membandingkan kinerja waktu komputasi, penggunaan memori, dan kualitas solusi.

**Penulis:** Duta Adi Pamungkas (24060123140174)  
**Institusi:** Departemen Informatika, Universitas Diponegoro  

---

## Apa yang Dilakukan oleh Program Ini?

Program ini bertindak sebagai **Sistem Penunjang Keputusan** yang membantu manajer proyek membelanjakan Rencana Anggaran Biaya (RAB) secara optimal pada simulasi proyek pembangunan gedung bertingkat (3-5 lantai, ~2000 m2).

### 1. Memuat Data Material & Vendor (Input)
Program memiliki katalog berisi **25 kategori material bangunan nyata** (Semen, Besi Beton, Cat, Kabel Listrik, Pompa Air, dsb.) dengan kuantitas realistis skala gedung bertingkat. Untuk setiap material, terdapat 4 pilihan **Merk/Vendor** yang menawarkan **Harga Riil** dan **Skor Kualitas** yang berbeda-beda.

### 2. Menerapkan Priority Weighting (Pembobotan Prioritas)
Program mengalikan skor kualitas material dengan **Bobot Prioritas** sesuai tingkat kepentingan struktural:
* **Material Struktural** (Semen, Besi Beton) mendapat bobot tinggi (P = 1.4 - 1.5) agar program memprioritaskan kualitas demi keamanan dan integritas struktur.
* **Material Arsitektural & Finishing** (Cat, Keramik) mendapat bobot rendah (P = 0.8) sehingga program bisa berhemat di sektor ini saat uang mulai mepet.

### 3. Penskalaan Memori (Pre-processing)
Algoritma Dynamic Programming mengalokasikan memori berdasarkan jumlah uang, sehingga program membagi harga riil dengan skala **50.000** (Scale Factor) untuk menyeimbangkan kecepatan dan mencegah *Out of Memory* pada komputasi ruang matriks 25 kategori.

### 4. Eksekusi Pencarian Kombinasi (Inti Optimasi)
Program menjalankan 3 algoritma secara berurutan:
* **Syarat:** Memilih tepat 1 vendor untuk setiap jenis material. Total harga tidak boleh melampaui Batas RAB (Rp 1.800.000.000).
* **Tujuan:** Mencari kombinasi 25 vendor yang menghasilkan Total Skor Bobot paling maksimal.

### 5. Laporan Evaluasi (Output)
Program mencetak:
* Rincian vendor yang dipilih oleh masing-masing algoritma.
* **Tabel perbandingan kinerja:** skor bobot, total biaya riil, waktu eksekusi, penggunaan memori puncak, dan status optimalitas solusi.

---

## Analisis Algoritma

1. **Dynamic Programming (DP):** Pendekatan eksak bottom-up menggunakan tabulasi. Menjamin solusi 100% optimal namun dibatasi oleh kompleksitas memori pseudo-polinomial O(N x W). Dengan 25 kategori, DP ini berhasil menemukan solusi optimal dalam hitungan detik meski mengonsumsi memori paling besar (sekitar 8 MB).
2. **Branch and Bound (B&B):** Pendekatan eksak berbasis pohon keputusan yang menggunakan *pruning* (pemangkasan cabang). Untuk skala 25 kategori (ruang pencarian $4^{25}$), telah ditambahkan *LP-Relaxation Bound* berbasis Fractional Knapsack dan *Greedy Initial Solution*. Tersedia mekanisme *Time Limit* (timeout 30 detik) yang akan menghentikan komputasi panjang B&B dan mengembalikan solusi terbaik sejauh itu.
3. **Simulated Annealing (SA):** Pendekatan metaheuristik probabilistik yang menerima transisi acak dan memanfaatkan *cooling rate* (`T0 = 15.000`, max 8000 iterasi). Algoritma ini berjalan **sangat cepat** (hanya puluhan milidetik) dan hemat memori, namun hanya dapat mencapai ~97-98% solusi optimal dari DP.

## Struktur Direktori

```text
tubes_asa/
├── Algorithms/
│   ├── BranchAndBound.py     # Logika algoritma B&B (dengan time limit & LP bound)
│   ├── DynamicProgramming.py # Logika algoritma tabulasi matriks DP
│   └── SimulatedAnnealing.py # Logika algoritma heuristik SA
├── Dataset/
│   └── MaterialData.py       # Katalog 25 kategori material beserta data vendor faktual
├── Utils/
│   └── Formatter.py          # Fungsi utilitas (format Rupiah)
├── Settings.py               # Konfigurasi global (Batas RAB, Penskalaan, Parameter SA)
├── Main.py                   # Entry point program dan pencetak tabel
└── README.md                 # Dokumentasi proyek
```

## Cara Menjalankan

Buka terminal/command prompt, arahkan direktori ke `Tubes ASA`, dan jalankan perintah berikut:
```bash
python Main.py
```
Program akan secara otomatis meload 25 data material, men-skala RAB, menghitung bobot prioritas, dan membandingkan DP, B&B, dan SA dalam satu antarmuka terminal.
