# Algorithms/BranchAndBound.py
import sys
import time
sys.setrecursionlimit(100000)

class BranchAndBound:
    def __init__(self, Materials, Rab, TimeLimit=30):
        self.Materials = Materials
        self.Rab = Rab
        self.N = len(Materials)
        self.BestScore = 0
        self.BestPath = []
        self.NodeCount = 0
        self.TimedOut = False
        self.TimeLimit = TimeLimit  # Batas waktu eksplorasi (detik)
        self.StartTime = 0

        # cari min cost & skor termurah
        self.MinCost = [min(v['Cost'] for v in Mat) for Mat in Materials]
        self.CheapestScore = []
        for i in range(self.N):
            cheapest = min(Materials[i], key=lambda v: (v['Cost'], -v['WeightedScore']))
            self.CheapestScore.append(cheapest['WeightedScore'])

        # precompute suffix max
        self.CumMaxScore = [0] * (self.N + 1)
        self.CumMinCost = [0] * (self.N + 1)
        self.CumCheapestScore = [0] * (self.N + 1)
        for i in range(self.N - 1, -1, -1):
            self.CumMaxScore[i] = self.CumMaxScore[i + 1] + max(v['WeightedScore'] for v in Materials[i])
            self.CumMinCost[i] = self.CumMinCost[i + 1] + self.MinCost[i]
            self.CumCheapestScore[i] = self.CumCheapestScore[i + 1] + self.CheapestScore[i]

        # bikin list upgrade buat LP bound
        AllUpgrades = []
        for i in range(self.N):
            for v in Materials[i]:
                GainCost = v['Cost'] - self.MinCost[i]
                GainScore = v['WeightedScore'] - self.CheapestScore[i]
                if GainCost > 0 and GainScore > 0:
                    AllUpgrades.append((GainScore / GainCost, GainScore, GainCost, i))

        AllUpgrades.sort(reverse=True, key=lambda x: x[0])

        # cache suffix upgrade
        self.SuffixUpgrades = [[] for _ in range(self.N + 1)]
        for Idx in range(self.N):
            self.SuffixUpgrades[Idx] = [
                (r, gs, gc) for (r, gs, gc, cat) in AllUpgrades if cat >= Idx
            ]

        # sort berdasarkan skor
        for i in range(self.N):
            self.Materials[i] = sorted(
                self.Materials[i], key=lambda v: v['WeightedScore'], reverse=True
            )

        # init pakai greedy
        self._InitGreedy()

    def _InitGreedy(self):
        # solusi awal
        Path = [None] * self.N
        TotalCost = 0

        # ambil yang paling murah
        for i in range(self.N):
            Cheapest = min(self.Materials[i], key=lambda v: v['Cost'])
            Path[i] = Cheapest
            TotalCost += Cheapest['Cost']

        if TotalCost > self.Rab:
            return  # udah over budget duluan

        # coba upgrade
        Upgrades = []
        for i in range(self.N):
            for v in self.Materials[i]:
                if v['WeightedScore'] > Path[i]['WeightedScore']:
                    DeltaCost = v['Cost'] - Path[i]['Cost']
                    DeltaScore = v['WeightedScore'] - Path[i]['WeightedScore']
                    Ratio = DeltaScore / max(DeltaCost, 1)
                    Upgrades.append((Ratio, i, v))

        Upgrades.sort(reverse=True)

        for _, i, v in Upgrades:
            NewCost = TotalCost - Path[i]['Cost'] + v['Cost']
            if NewCost <= self.Rab and v['WeightedScore'] > Path[i]['WeightedScore']:
                TotalCost = NewCost
                Path[i] = v

        Score = sum(v['WeightedScore'] for v in Path)
        if Score > self.BestScore:
            self.BestScore = Score
            self.BestPath = list(Path)

    def _LPBound(self, Index, CurrentCost, CurrentScore):
        # bound pakai fractional knapsack
        Remaining = self.Rab - CurrentCost
        Mandatory = self.CumMinCost[Index]

        if Remaining < Mandatory:
            return -1  # ga cukup budget

        # base score
        Bound = CurrentScore + self.CumCheapestScore[Index]

        # sisa budget
        UpgradeBudget = Remaining - Mandatory

        # greedy fill
        for Ratio, GainScore, GainCost in self.SuffixUpgrades[Index]:
            if UpgradeBudget <= 0:
                break
            if GainCost <= UpgradeBudget:
                Bound += GainScore
                UpgradeBudget -= GainCost
            else:
                # ambil sisanya
                Bound += GainScore * (UpgradeBudget / GainCost)
                break

        return Bound

    def Solve(self):
        self.StartTime = time.time()
        self.Dfs(0, 0, 0, [])
        return self.BestScore, self.BestPath

    def Dfs(self, Index, CurrentCost, CurrentScore, CurrentPath):
        # cek timeout
        self.NodeCount += 1
        if self.NodeCount % 5000 == 0:
            if time.time() - self.StartTime > self.TimeLimit:
                self.TimedOut = True
                return

        if self.TimedOut:
            return

        if Index == self.N:
            if CurrentScore > self.BestScore:
                self.BestScore = CurrentScore
                self.BestPath = list(CurrentPath)
            return

        # prune kalau over budget
        if CurrentCost + self.CumMinCost[Index] > self.Rab:
            return

        # prune max score
        if CurrentScore + self.CumMaxScore[Index] <= self.BestScore:
            return

        # prune lp bound
        if self._LPBound(Index, CurrentCost, CurrentScore) <= self.BestScore:
            return

        for Vendor in self.Materials[Index]:
            if CurrentCost + Vendor['Cost'] <= self.Rab:
                CurrentPath.append(Vendor)
                self.Dfs(
                    Index + 1,
                    CurrentCost + Vendor['Cost'],
                    CurrentScore + Vendor['WeightedScore'],
                    CurrentPath
                )
                CurrentPath.pop()
                if self.TimedOut:
                    return
