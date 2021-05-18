import math
import matplotlib.pyplot as plt

import numpy as np

def GenNSim(n):
    p = []
    sommeAll=0
    sommeLast=0
    for i in range(n):
        value = np.random.uniform(0, 1, 1)[0]
        sommeAll = sommeAll + value
        p.append(value)
    for i in range(n-1):
        p[i]=p[i]/sommeAll
        p[i]=round(p[i],3)
        sommeLast=sommeLast+p[i]
    p[n-1]=round((1-sommeLast),3)

    return p

def GenerateSimulationMatrix(ArraySize,SimulationNumber):
    l = []
    f = open("Similations.txt", "w+")
    for i in range(1, SimulationNumber):
        k = GenNSim(ArraySize)
        l.append(k)
    f.write(str(l))
    f.write(";")
    f.close()
    return l
def GenSimulationUniforme(ArraySize,SimulationNumber):
    p=[]
    f = open("Similations.txt", "w+")

    for i in range(SimulationNumber):
        l=[]
        for j in range(ArraySize):
           # value = np.random.normal(0, 1, 1)[0]
            value =np.random.uniform(0, 1, 1)[0]
            value = round(value,3)
            l.append(value)
        p.append(l)
    f.write(str(p))
    f.write(";")
    f.close()

GenerateSimulationMatrix(3,20000)



def simulationsTotal(bondsArray,variationLevel,simulationNumber):
    p = open("yValuesProbabilitySimulations.txt", "w+")
    f = open("bValuesSimulation.txt", "w+")
    bondsSimulation=[]
    for i in range(simulationNumber):
        bondsSimuledListGroup=[]
        for bond in bondsArray:
            simuledVariation=np.random.uniform(0, variationLevel, variationLevel)[0]
            bond=bond*simuledVariation
            bondsSimuledListGroup.append(bond)
        bondsSimulation.append(bondsSimuledListGroup)
    f.write(str(bondsSimulation))
    f.write(";")
    f.close()
    yVariation=GenNSim(simulationNumber)
    p.write(str(yVariation))
    p.write(";")
    p.close()
    return (bondsSimulation,yVariation)



def calculateurCVarAndVar(benchmark,simulationNumber,portfeuille,alpha):
    simulationMatrix = GenerateSimulationMatrix(len(portfeuille),simulationNumber)
    Scenario_ResultAndProbability = []
    P = 1 / simulationNumber
    for i in range(simulationNumber - 1):
        Y = 0
        for j in range(len(portfeuille)):
            Y = Y + ((benchmark[j] - simulationMatrix[i][j]) * portfeuille[j])

        Scenario_ResultAndProbability.append([Y, P])
    SortedMatrixVarValue = np.array(Scenario_ResultAndProbability)
    SortedMatrixVarValue.sort(axis=0)
    k = int(alpha /(P))
    Var = SortedMatrixVarValue[k][0]
    somme = ((alpha /(P))-k)*(1/simulationNumber)
    for i in range(k,simulationNumber):
        somme = somme+SortedMatrixVarValue[k][0]*SortedMatrixVarValue[k][1]
    CVAR= somme/(1-alpha)
    return Var,CVAR

alpha=0.95
benchmark=[0.2,0.6,0.3]
variationLevel = 1
simulationNumber = 1000
portfeuille=[0.75,	0,	0.25]
var,cvar = calculateurCVarAndVar(benchmark,simulationNumber,portfeuille,alpha)
print("var = ",var)
print("Cvar = ",cvar)

