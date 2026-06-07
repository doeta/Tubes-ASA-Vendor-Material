# Main.py
import sys
sys.dont_write_bytecode = True

import time
import tracemalloc
import Settings
from Dataset.MaterialData import LoadProcessedData, GenerateMassiveData
from Algorithms.DynamicProgramming import Solve as DpSolve
from Algorithms.BranchAndBound import BranchAndBound
from Algorithms.SimulatedAnnealing import Solve as SaSolve
from Utils.Formatter import FormatRupiah

def PrintResult(AlgoName, Score, Path, ExecTime, PeakMemKb):
    print(f"\n[{AlgoName}]")
    print(f"  Waktu Eksekusi    : {ExecTime:.5f} detik")
    print(f"  Puncak Memori     : {PeakMemKb:.2f} KB")
    print(f"  Total Skor Bobot  : {Score:.2f}")

    if not Path:
        print("  Status: GAGAL MENEMUKAN SOLUSI (Over Budget)")
        return

    TotalRealCost = sum(v['RealCost'] for v in Path)
    print(f"  Total Biaya Riil  : {FormatRupiah(TotalRealCost)}")
    print("  Rincian Pilihan Vendor:")
    for v in Path:
        print(f"    - {v['Id']} | {FormatRupiah(v['RealCost'])} (Kualitas: {v['Quality']})")

def PrintComparisonTable(Results, Rab):
    print("\n" + "=" * 80)
    print(" TABEL PERBANDINGAN KINERJA ALGORITMA")
    print("=" * 80)
    print(f"  {'Kriteria':<25} | {'DP':>15} | {'B&B':>15} | {'SA':>15}")
    print("  " + "-" * 73)

    # Total Skor
    print(f"  {'Total Skor Bobot':<25} | ", end="")
    for R in Results:
        print(f"{R['Score']:>15.2f} | ", end="")
    print()

    # Total Biaya
    print(f"  {'Total Biaya Riil':<25} | ", end="")
    for R in Results:
        if R['Path']:
            Cost = sum(v['RealCost'] for v in R['Path'])
            CostStr = FormatRupiah(Cost)
        else:
            CostStr = "N/A"
        print(f"{CostStr:>15} | ", end="")
    print()

    # Waktu
    print(f"  {'Waktu Eksekusi (dtk)':<25} | ", end="")
    for R in Results:
        print(f"{R['Time']:>15.5f} | ", end="")
    print()

    # Memori
    print(f"  {'Puncak Memori (KB)':<25} | ", end="")
    for R in Results:
        print(f"{R['Memory']:>15.2f} | ", end="")
    print()

    # Optimalitas
    MaxScore = max(R['Score'] for R in Results)
    print(f"  {'Status Solusi':<25} | ", end="")
    for R in Results:
        if R['Score'] == 0:
            Status = "Gagal"
        elif R['Score'] >= MaxScore:
            Status = "Optimal"
        else:
            Pct = (R['Score'] / MaxScore) * 100
            Status = f"~{Pct:.1f}%"
        print(f"{Status:>15} | ", end="")
    print()

    print("  " + "-" * 73)
    print(f"  Batas RAB: {FormatRupiah(Rab)}")
    print("=" * 80)

if __name__ == "__main__":
    print("=" * 80)
    print(" PERBANDINGAN ALGORITMA DP, B&B, DAN SA")
    print(" Optimasi Pemilihan Vendor Material Bangunan Berdasarkan RAB")
    print(" Simulasi Proyek Pembangunan Gedung Bertingkat")
    print("=" * 80)

    # Load data
    # 1. LoadProcessedData()      -> 25 Kategori
    # 2. GenerateMassiveData(50)  -> Uji beban 50 Kategori

    Materials = LoadProcessedData()
    RabScaled = Settings.ScaledRab

    print(f"  Jumlah Kategori Material : {len(Materials)}")
    print(f"  Batas RAB                : {FormatRupiah(Settings.DefaultRabReal)}")
    print(f"  Skala Faktor             : {Settings.ScaleFactor:,}")
    print(f"  RAB Setelah Diskala      : {RabScaled}")

    Results = []

    # Run DP
    tracemalloc.start()
    Start = time.time()
    DpScore, DpPath = DpSolve(Materials, RabScaled)
    DpTime = time.time() - Start
    DpMem = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()
    PrintResult("DYNAMIC PROGRAMMING", DpScore, DpPath, DpTime, DpMem)
    Results.append({"Name": "DP", "Score": DpScore, "Path": DpPath, "Time": DpTime, "Memory": DpMem})

    # Run BnB
    tracemalloc.start()
    Start = time.time()
    Bb = BranchAndBound(Materials, RabScaled)
    BbScore, BbPath = Bb.Solve()
    BbTime = time.time() - Start
    BbMem = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()
    BbLabel = "BRANCH AND BOUND"
    if Bb.TimedOut:
        BbLabel += f" (Timeout {Bb.TimeLimit}s, {Bb.NodeCount:,} nodes)"
    PrintResult(BbLabel, BbScore, BbPath, BbTime, BbMem)
    Results.append({"Name": "B&B", "Score": BbScore, "Path": BbPath, "Time": BbTime, "Memory": BbMem})

    # Run SA
    tracemalloc.start()
    Start = time.time()
    SaScore, SaPath = SaSolve(Materials, RabScaled)
    SaTime = time.time() - Start
    SaMem = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()
    PrintResult("SIMULATED ANNEALING", SaScore, SaPath, SaTime, SaMem)
    Results.append({"Name": "SA", "Score": SaScore, "Path": SaPath, "Time": SaTime, "Memory": SaMem})

    # Print perbandingan
    PrintComparisonTable(Results, Settings.DefaultRabReal)
