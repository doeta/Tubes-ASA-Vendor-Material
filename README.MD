# Perbandingan Algoritma DP, B&B, dan SA dalam Optimasi Pemilihan Vendor Material Bangunan Berdasarkan RAB

Proyek ini merupakan implementasi Tugas Besar Mata Kuliah **Analisis dan Strategi Algoritma (ASA)**. Proyek ini memodelkan permasalahan pemilihan vendor material bangunan sebagai *Multiple-Choice Knapsack Problem* (MCKP) dan menyelesaikannya menggunakan tiga algoritma berbeda untuk membandingkan kinerja waktu komputasi, penggunaan memori, dan kualitas solusi.

**Penulis:** Duta Adi Pamungkas (24060123140174)  
**Institusi:** Departemen Informatika, Universitas Diponegoro  

---

## Apa yang Dilakukan oleh Program Ini?

Program ini bertindak sebagai **Sistem Penunjang Keputusan** yang membantu manajer proyek membelanjakan Rencana Anggaran Biaya (RAB) secara optimal pada simulasi proyek pembangunan gedung bertingkat (3-5 lantai, ~2000 m2).

### 1. Memuat Data Material & Vendor (Input)
Program memiliki katalog berisi 15 kategori material bangunan nyata (Semen, Besi Beton, Cat, Kabel Listrik, dll) dengan kuantitas realistis skala gedung bertingkat. Untuk setiap material, terdapat 4 pilihan **Merk/Vendor** yang menawarkan **Harga Riil** dan **Skor Kualitas** yang berbeda-beda.

### 2. Menerapkan Priority Weighting (Pembobotan Prioritas)
Program mengalikan skor kualitas material dengan **Bobot Prioritas** sesuai tingkat kepentingan struktural:
* **Material Struktural** (Semen, Besi Beton) mendapat bobot tinggi (P = 1.5) agar program memprioritaskan kualitas demi keamanan struktur.
* **Material Arsitektural** (Cat, Keramik) mendapat bobot rendah (P = 0.8) sehingga program bisa berhemat di sektor ini.

### 3. Penskalaan Memori (Pre-processing)
Algoritma Dynamic Programming mengalokasikan memori berdasarkan jumlah uang, sehingga program membagi harga riil dengan skala 100.000 untuk mencegah galat Out of Memory.

### 4. Eksekusi Pencarian Kombinasi (Inti Optimasi)
Program menjalankan 3 algoritma secara berurutan:
* **Syarat:** Memilih tepat 1 vendor untuk setiap jenis material. Total harga tidak boleh melampaui RAB.
* **Tujuan:** Mencari kombinasi vendor yang menghasilkan Total Skor Bobot Paling Tinggi.

### 5. Laporan Evaluasi (Output)
Program mencetak:
* Rincian vendor yang dipilih oleh masing-masing algoritma.
* **Tabel perbandingan** kinerja: waktu eksekusi, penggunaan memori puncak, dan kualitas solusi.

---

## Analisis Algoritma
1. **Dynamic Programming (DP):** Pendekatan eksak bottom-up menggunakan tabulasi. Menjamin solusi 100% optimal namun dibatasi oleh kompleksitas memori pseudo-polinomial O(N x B).
2. **Branch and Bound (B&B):** Pendekatan eksak berbasis pohon keputusan yang menggunakan pruning (pemangkasan cabang) berdasarkan evaluasi batas biaya dan batas skor maksimal.
3. **Simulated Annealing (SA):** Pendekatan metaheuristik probabilistik yang mampu memberikan solusi near-optimal dengan komputasi waktu dan ruang yang sangat minimalis.

## Struktur Direktori

```text
tubes_asa/
├── Algorithms/
│   ├── BranchAndBound.py     # Logika algoritma pencarian pohon eksak
│   ├── DynamicProgramming.py # Logika algoritma tabulasi matriks
│   └── SimulatedAnnealing.py # Logika algoritma heuristik berbasis suhu
├── Dataset/
│   └── MaterialData.py       # Katalog 15 kategori material gedung bertingkat
├── Utils/
│   └── Formatter.py          # Fungsi utilitas (format Rupiah)
├── Settings.py               # Konfigurasi global (Batas RAB, Penskalaan, Parameter SA)
├── Main.py                   # Entry point program
└── README.MD                 # Dokumentasi proyek
```

## Cara Menjalankan

```bash
python Main.py
```
