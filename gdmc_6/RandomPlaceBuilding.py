import time
import numpy as np
from MonumentBuilding import *
from EvolutionaryAlgorithm import *
from DormBuilding import *


def placeBuilding(building, bluePrint, gd, rewards, maxTry=20):
    maxReward = -9999999
    sx = 0
    sz = 0
    for j in range(maxTry):
        rx = random.randint(2, len(bluePrint) - building.size[0] - 3)
        rz = random.randint(2, len(bluePrint[0]) - building.size[2] - 3)
        reward = getReward(rx, rz, building.size[0], building.size[2], bluePrint, gd, rewards)

        if reward > maxReward:
            maxReward = reward
            sx = rx
            sz = rz
        if reward == building.area:
            return sx, sz, maxReward
    return sx, sz, maxReward


def heuristicPlace(base, buildings, padding, gd, rewards, times):
    bluePrint = np.array(base)
    sum = 0
    for building in buildings:
        next = True
        for i in range(len(bluePrint) - building.size[0]):
            if next:
                for j in range(len(bluePrint[0]) - building.size[2]):
                    if bluePrint[i][j] == 3 or bluePrint[i][j] == 5 or bluePrint[i][j] == 6:
                        continue
                    reward = getReward(i, j, building.size[0], building.size[2], bluePrint, gd, rewards)
                    if reward > 0:
                        sum += reward
                        designBuilding(bluePrint, i, j, building, padding)
                        next = False
                        break
            else:
                break

    return bluePrint, sum


def randomPlaceBuilding(base, bigBuildings, buildings, padding, gd, rewards):
    globalReward = -1
    globalBluePoint = None
    globalBuildings = []
    leftBackPoints = []

    for i in range(1000):
        bluePrint = np.array(base)
        tempReward = 0
        tPoints = []
        tBuildings = []
        cnt = 0
        step = 1

        while True:
            building = bigBuildings[min(cnt, len(bigBuildings) - 1)]

            # if step == 1:
            #     building = bigBuildings[min(cnt,len(bigBuildings)-1)]
            # else:
            #     building = buildings[cnt % len(buildings)]

            sx, sz, maxReward = placeBuilding(building, bluePrint, gd, rewards)
            if maxReward < 0:
                # if step == 1:
                #     step = 2
                #     continue
                # else:
                #     break
                break

            tempReward += maxReward
            designBuilding(bluePrint, sx, sz, building, padding)
            tPoints.append((sx, sz))
            tBuildings.append(building)
            cnt += 1

        building = buildings[cnt % len(buildings)]
        for x in range(3, len(base)-building.size[0]-4, 5):
            for z in range(3, len(base[0])-building.size[2]-4, 5):
                tx = x + random.randint(-1, 1)
                tz = z + random.randint(-1, 1)
                reward = getReward(tx, tz, building.size[0], building.size[2], bluePrint, gd, rewards)
                if reward>0:
                    tempReward += reward
                    designBuilding(bluePrint, tx, tz, building, padding)
                    tPoints.append((tx, tz))
                    tBuildings.append(building)
                    cnt += 1
                    building = buildings[cnt % len(buildings)]


        if tempReward > globalReward:
            globalReward = tempReward
            globalBluePoint = bluePrint
            leftBackPoints = tPoints
            globalBuildings = tBuildings

    return globalBluePoint, globalBuildings, leftBackPoints
