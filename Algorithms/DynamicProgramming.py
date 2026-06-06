# Algorithms/DynamicProgramming.py

def Solve(Materials, Rab):
    N = len(Materials)
    Dp = {W: (0, []) for W in range(Rab + 1)}
    
    for i in range(N):
        NewDp = {W: (0, []) for W in range(Rab + 1)}
        for W in range(Rab + 1):
            for V in Materials[i]:
                if W >= V['Cost']:
                    PrevScore, PrevPath = Dp[W - V['Cost']]
                    if i == 0 or len(PrevPath) == i: 
                        if PrevScore + V['WeightedScore'] > NewDp[W][0]:
                            NewDp[W] = (PrevScore + V['WeightedScore'], PrevPath + [V])
        Dp = NewDp
        
    BestScore = 0
    BestPath = []
    for W in range(Rab + 1):
        if len(Dp[W][1]) == N and Dp[W][0] > BestScore:
            BestScore = Dp[W][0]
            BestPath = Dp[W][1]
            
    return BestScore, BestPath
