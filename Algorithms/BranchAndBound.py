# Algorithms/BranchAndBound.py
import sys
sys.setrecursionlimit(10000)

class BranchAndBound:
    def __init__(self, Materials, Rab):
        self.Materials = Materials
        self.Rab = Rab
        self.N = len(Materials)
        self.BestScore = 0
        self.BestPath = []

        self.MaxSRemaining = [max(v['WeightedScore'] for v in Mat) for Mat in Materials]
        self.MinCRemaining = [min(v['Cost'] for v in Mat) for Mat in Materials]

        # Pre-compute cumulative sums untuk pruning lebih cepat (tanpa slice+sum setiap panggilan)
        self.CumMaxScore = [0] * (self.N + 1)
        self.CumMinCost = [0] * (self.N + 1)
        for i in range(self.N - 1, -1, -1):
            self.CumMaxScore[i] = self.CumMaxScore[i + 1] + self.MaxSRemaining[i]
            self.CumMinCost[i] = self.CumMinCost[i + 1] + self.MinCRemaining[i]

        # Urutkan vendor di setiap kategori: skor tertinggi dahulu agar solusi baik ditemukan lebih awal
        for i in range(self.N):
            self.Materials[i] = sorted(self.Materials[i], key=lambda v: v['WeightedScore'], reverse=True)

    def Solve(self):
        self.Dfs(0, 0, 0, [])
        return self.BestScore, self.BestPath

    def Dfs(self, Index, CurrentCost, CurrentScore, CurrentPath):
        if Index == self.N:
            if CurrentScore > self.BestScore:
                self.BestScore = CurrentScore
                self.BestPath = list(CurrentPath)
            return

        # Pruning 1: Jika biaya minimum sisa pasti melampaui RAB
        if CurrentCost + self.CumMinCost[Index] > self.Rab:
            return

        # Pruning 2: Jika skor maksimum sisa tidak mungkin melebihi BestScore saat ini
        if CurrentScore + self.CumMaxScore[Index] <= self.BestScore:
            return

        for Vendor in self.Materials[Index]:
            if CurrentCost + Vendor['Cost'] <= self.Rab:
                CurrentPath.append(Vendor)
                self.Dfs(Index + 1, CurrentCost + Vendor['Cost'], CurrentScore + Vendor['WeightedScore'], CurrentPath)
                CurrentPath.pop()
