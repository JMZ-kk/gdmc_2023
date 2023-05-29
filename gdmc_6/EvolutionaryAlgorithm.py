import numpy as np
import random


def getReward(sx, sz, lx, lz, bluePrint, gd, rewards, isMunition=False):
    reward = 0
    for i in range(sx, sx + lx):
        for j in range(sz, sz + lz):
            if bluePrint[i][j] == 3:
                return -999999
            elif bluePrint[i][j] == 4:
                reward -= abs(gd[0][i][j])
                reward -= abs(gd[1][i][j])
            else:
                reward += rewards[bluePrint[i][j]]
    if isMunition:
        reward += len(bluePrint) - sx + len(bluePrint[0]) - sz
    return reward


def designBuilding(base, sx, sz, building, padding):
    x1 = max(0, sx - padding)
    x2 = min(sx + building.size[0] + padding, len(base) - 1)
    z1 = max(0, sz - padding)
    z2 = min(sz + building.size[2] + padding, len(base[0]) - 1)
    for x in range(x1, x2):
        for z in range(z1, z2):
            if base[x][z] != 6:
                base[x][z] = 5
    if building.name != 'light':
        base[max(0, sx - 2):min(sx + building.size[0] + 2, len(base) - 1),
        max(0, sz - 2):min(sz + building.size[2] + 2, len(base[0]) - 1)] = 6
    base[sx:sx + building.size[0], sz:sz + building.size[2]] = 3


def calculateFitness(sol, buildings, map, padding, gd, rewards):
    sum = 0

    for i in range(len(buildings)):
        building = buildings[i]
        x = int(sol[i] // len(map))
        z = int(sol[i] % len(map[0]))
        reward = getReward(x, z, building.size[0], building.size[2], map, gd, rewards)
        if reward > 0:
            sum += reward
            designBuilding(map, x, z, building, padding)

    return sum


def initializationPop(popSize, buildings, bluePrint):
    pop = np.zeros((popSize, len(buildings)))
    for i in range(popSize):
        for j in range(len(buildings)):
            pop[i][j] = getNewGene(buildings[j], bluePrint)
    return pop


def getNewGene(building, bluePrint):
    while True:
        x = random.randint(0, len(bluePrint) - 1 - building.size[0])
        z = random.randint(0, len(bluePrint[0]) - 1 - building.size[2])
        if bluePrint[x][z] != 3 and bluePrint[x][z] != 5 and bluePrint[x][z] != 6:
            break
    gene = x * len(bluePrint[0]) + z
    return gene

def evo(bluePrint, buildings, padding, gd, rewards, popSize, NGeneration, pumt):
    def selectParents(pop, fitness, popSize):
        chosenId = np.random.choice(np.arange(popSize), size=popSize, p=fitness / fitness.sum())
        return pop[chosenId]

    def reproduce(x, y):
        n = len(x)
        c = random.randint(1, n - 1)
        res = np.zeros(len(x))
        for i in range(len(x)):
            if i < c:
                res[i] = x[i]
            else:
                res[i] = y[i]
        return res

    def mutate(x):
        res = np.zeros(len(x))
        c = random.randint(0, len(x) - 1)
        g = getNewGene(buildings[c], bluePrint)
        for i in range(len(x)):
            if i < c:
                res[i] = x[i]
            elif i == c:
                res[i] = g
            else:
                res[i] = y[i]
        return res

    bestValue = -1
    bestSol=np.zeros(len(buildings))
    pop = initializationPop(popSize, buildings, bluePrint)
    fitnessList = np.zeros(popSize)
    newPop = np.zeros((popSize, len(buildings)))

    for ng in range(NGeneration):
        for i in range(popSize):
            bluePrintCopy = np.array(bluePrint)
            fitnessList[i]= calculateFitness(pop[i],buildings, bluePrintCopy, padding, gd, rewards)
            if fitnessList[i]>bestValue:
                bestValue=fitnessList[i]
                bestSol=np.array(pop[i])
        parents = selectParents(pop, fitnessList, popSize)
        for i in range(popSize):
            x = random.choice(parents)
            y = random.choice(parents)
            child = reproduce(x, y)

            if random.uniform(0, 1) < pumt:
                child = mutate(child)
            for k in range(len(child)):
                newPop[i][k] = child[k]
        pop = newPop
    globalBluePrint = np.array(bluePrint)
    calculateFitness(bestSol, buildings, globalBluePrint, padding, gd, rewards)
    leftBackPoints=[]
    for i in range(len(bestSol)):
        x = int(bestSol[i] // len(globalBluePrint))
        z = int(bestSol[i] % len(globalBluePrint[0]))
        leftBackPoints.append((x,z))
    return globalBluePrint, buildings, leftBackPoints
