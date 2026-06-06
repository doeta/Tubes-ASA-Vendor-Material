# Algorithms/SimulatedAnnealing.py
import random
import math
import Settings

def Solve(Materials, Rab):
    N = len(Materials)
    
    def GetFitness(State):
        Cost = sum(v['Cost'] for v in State)
        Score = sum(v['WeightedScore'] for v in State)
        if Cost > Rab:
            return Score - (Cost - Rab) * 1000 # Penalti jika over-budget
        return Score

    CurrentState = [random.choice(Mat) for Mat in Materials]
    CurrentFitness = GetFitness(CurrentState)
    
    BestState = list(CurrentState)
    BestFitness = CurrentFitness
    
    Temp = Settings.SaInitialTemp
    
    for Iteration in range(Settings.SaMaxIter):
        if Temp < 1e-3:
            break
            
        MatIdx = random.randint(0, N - 1)
        NewVendor = random.choice(Materials[MatIdx])
        
        NeighborState = list(CurrentState)
        NeighborState[MatIdx] = NewVendor
        NeighborFitness = GetFitness(NeighborState)
        
        DeltaE = NeighborFitness - CurrentFitness
        if DeltaE > 0 or random.random() < math.exp(DeltaE / Temp):
            CurrentState = NeighborState
            CurrentFitness = NeighborFitness
            
            if CurrentFitness > BestFitness and sum(v['Cost'] for v in CurrentState) <= Rab:
                BestFitness = CurrentFitness
                BestState = list(CurrentState)
                
        Temp *= Settings.SaCoolingRate
        
    if sum(v['Cost'] for v in BestState) > Rab:
        return 0, [] 
    return BestFitness, BestState
