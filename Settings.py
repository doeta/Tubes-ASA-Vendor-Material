# Settings.py

# Penskalaan memori untuk menghindari Out of Memory pada matriks DP
ScaleFactor = 100_000

# Rencana Anggaran Biaya (RAB) Maksimal
# Realistis untuk proyek gedung bertingkat skala kecil-menengah (3-5 lantai)
DefaultRabReal = 750_000_000
ScaledRab = DefaultRabReal // ScaleFactor

# Parameter Algoritma Simulated Annealing
SaInitialTemp = 1000.0
SaCoolingRate = 0.99
SaMaxIter = 2500
