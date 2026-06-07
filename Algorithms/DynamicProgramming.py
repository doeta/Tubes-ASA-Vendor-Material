# Algorithms/DynamicProgramming.py

def Solve(Materials, Rab):
    # DP solver untuk knapsack
    # O(N * K * W) time, O(N * W) space
    N = len(Materials)
    NEG_INF = float('-inf')

    # inisialisasi dp
    Dp = [NEG_INF] * (Rab + 1)
    Dp[0] = 0

    # simpan pilihan buat backtrack
    Choice = []

    for i in range(N):
        NewDp = [NEG_INF] * (Rab + 1)
        GroupChoice = [-1] * (Rab + 1)

        for j, V in enumerate(Materials[i]):
            c = V['Cost']
            s = V['WeightedScore']
            for w in range(c, Rab + 1):
                prev = Dp[w - c]
                if prev != NEG_INF:
                    candidate = prev + s
                    if candidate > NewDp[w]:
                        NewDp[w] = candidate
                        GroupChoice[w] = j

        Dp = NewDp
        Choice.append(GroupChoice)

    # cari max score
    BestScore = 0
    BestW = -1
    for w in range(Rab + 1):
        if Dp[w] > BestScore:
            BestScore = Dp[w]
            BestW = w

    if BestW == -1:
        return 0, []

    # backtrack buat ambil list vendornya
    Path = [None] * N
    w = BestW
    for i in range(N - 1, -1, -1):
        j = Choice[i][w]
        if j == -1:
            return 0, []
        Path[i] = Materials[i][j]
        w -= Materials[i][j]['Cost']

    return BestScore, list(Path)
