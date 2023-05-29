from typing import Optional, Iterable, Set, Tuple, Union
import random
from gdpc import __url__, Editor, Block, Box, lookup
import numpy as np
from glm import ivec2, ivec3
from gdpc.vector_tools import Vec3iLike, Rect, Box, addY, dropY

from DormBuilding import *
from TrampolineStructure import *
from EnchantingBuilding import *
from Farm import *
from MyPoint import *
from PlaceWall import *
from PlaceRoad import *

from static_block_lists import *
import time
from sklearn import cluster
from MonumentBuilding import *
from MunitionsFactory import *
from MeetingBuilding import *
from StreetLight import *
from SteveStatue import *
from EndermanStatue import *
from Shop import *
from EvolutionaryAlgorithm import *
from RandomPlaceBuilding import *

import matplotlib.pyplot as plt



realPlace4Wall = 9
wallPadding = 4
reserveForWall = realPlace4Wall + wallPadding
minBuildingEdge = 10
rewards = [-9999, -10, 1, -9999, 0, -50, -50, 0, -999, -999, -999]
light_rewards = [-9999, -10, 1, -9999, 0, 0, 0, 0, 0, 0, 0]
buildings = [TrampolineStructure(), SteveStatue(), EndermanStatue()]
bigBuildings = [MeetingBuilding(), MunitionsFactory(), DormBuilding(), Shop(), EnchantingBuilding(), DormBuilding()]

groundBlockName = 'minecraft:dirt'
padding = 6
needMonument = True

editor = Editor(buffering=True)

def clearTreeAndLava(buildRect, worldSlice):
    heightMap = worldSlice.heightmaps["MOTION_BLOCKING"]
    sx = buildRect.begin[0]
    sz = buildRect.begin[1]
    kindCount={}
    for x in range(len(heightMap)):
        xx = x + sx
        for z in range(len(heightMap[0])):
            zz = z + sz
            c = 1
            while True:
                kind = worldSlice.getBlockGlobal((xx, heightMap[x][z] - c, zz)).id
                if kind in TREE_BLOCKS:
                    editor.placeBlockGlobal((xx, heightMap[x][z] - c, zz), Block('minecraft:air'))
                elif kind in ['minecraft:lava', 'minecraft:netherrack', 'minecraft:obsidian',
                              'minecraft:end_stone_brick_slab',
                              'minecraft:end_stone_brick_stairs', 'minecraft:crying_obsidian', 'minecraft:magma_block']:
                    editor.placeBlockGlobal((xx, heightMap[x][z] - c, zz), Block('minecraft:air'))
                elif kind not in ['minecraft:air', 'minecraft:void_air', 'minecraft:cave_air']:
                    if kind in kindCount.keys():
                        kindCount[kind] = kindCount[kind] + 1
                    else:
                        kindCount[kind] = 1
                    break
                c += 1

    most=0
    print(kindCount)
    for key in kindCount.keys():
        if kindCount[key]>most:
            most=kindCount[key]
            groundBlockName=key
    print('tree_cleared')
    return groundBlockName


def countHeightScore(x, z, subHeightMap):
    def compare(a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    score = 0
    if x > 0:
        score += compare(subHeightMap[x][z], subHeightMap[x - 1][z])
    if x < len(subHeightMap) - 1:
        score += compare(subHeightMap[x][z], subHeightMap[x + 1][z])
    if z > 0:
        score += compare(subHeightMap[x][z], subHeightMap[x][z - 1])
    if z < len(subHeightMap[0]) - 1:
        score += compare(subHeightMap[x][z], subHeightMap[x][z + 1])
    return score


def flattenMap(buildRect, times=3):
    worldSlice = editor.loadWorldSlice(buildRect)
    heightMap = worldSlice.heightmaps["MOTION_BLOCKING"]
    subHeightMap = heightMap[reserveForWall:len(heightMap) - reserveForWall,
                   reserveForWall:len(heightMap[0]) - reserveForWall]
    sx = buildRect.begin[0] + reserveForWall
    sz = buildRect.begin[1] + reserveForWall
    for _ in range(times):
        for x in range(len(subHeightMap)):
            xx = x + sx
            for z in range(len(subHeightMap[0])):
                zz = z + sz
                score = countHeightScore(x, z, subHeightMap)
                if score >= 3:
                    editor.placeBlockGlobal((xx, subHeightMap[x][z] - 1, zz), Block('minecraft:air'))
                    editor.placeBlockGlobal((xx, subHeightMap[x][z] - 2, zz), Block(groundBlockName))
                elif score <= -3:
                    editor.placeBlockGlobal((xx, subHeightMap[x][z], zz), Block(groundBlockName))





def getTerrain(subHeightMap, rectx, rectz, worldSlice, gd):
    base = np.zeros((len(subHeightMap), len(subHeightMap[0])), dtype=int)
    for x in range(len(subHeightMap)):
        xx = rectx + x
        for z in range(len(subHeightMap[0])):
            zz = rectz + z
            kind = worldSlice.getBlockGlobal((xx, subHeightMap[x][z] - 1, zz)).id
            if kind in WATER_BLOCKS:  # 水方块
                base[x][z] = 1
            elif gd[0][x][z] == 0 and gd[1][x][z] == 0:  # 平地，最佳选择
                base[x][z] = 2
            elif kind in MANMADE_BLOCKS:  # 村庄等人造建筑
                base[x][z] = 3
            else:
                base[x][z] = 4  # 非平地
    return base


def placeMonument(base, gd):
    monu = MonumentBuilding()
    maxReward = -9999999
    sx = 0
    sz = 0
    idealx = (len(base) - monu.size[0] - 1) // 2
    idealz = (len(base[0]) - monu.size[0] - 1) // 2

    for x in range(20, len(base) - monu.size[0] - 21, 5):
        for z in range(20, len(base[0]) - monu.size[2] - 21, 5):
            reward = getReward(x, z, monu.size[0], monu.size[2], base, gd, rewards) - abs(idealx - x) - abs(idealz - z)
            if reward > maxReward:
                maxReward = reward
                sx = x
                sz = z
    designBuilding(base, sx, sz, monu, padding)
    return sx, sz


def chooseLight(middlePointLists, globalBuildings, leftBackBottomPoints, bluePrint, gd, subHeightMap, rx, rz):
    light = StreetLight()

    def BFS(node):
        waitingList = [node]
        finishedList = []
        while len(waitingList) > 0:
            tp = waitingList[0]
            waitingList.remove(tp)
            x = tp[0]
            z = tp[1]
            if (x, z) not in finishedList:
                isFeasible=True
                for i in range(x, x + light.size[0]):
                    for j in range(z, z + light.size[2]):
                        if bluePrint[i][j] == 3 or bluePrint[i][j] == 6 or bluePrint[i][j] == 5:
                            isFeasible = False
                            break
                        if not isFeasible:
                            break
                if isFeasible:
                    return tp
                finishedList.append(tp)
                if x > 1 and (x - 1, z) not in finishedList:
                    waitingList.append((x - 1, z))
                if x < len(bluePrint) - light.size[0] - 2 and (x + 1, z) not in finishedList:
                    waitingList.append((x + 1, z))
                if z > 1 and (x, z - 1) not in finishedList:
                    waitingList.append((x, z - 1))
                if z < len(bluePrint[0]) - light.size[2] - 2 and (x, z + 1) not in finishedList:
                    waitingList.append((x, z + 1))

    middlePointLists2D = np.zeros((len(middlePointLists), 2))
    for i in range(0, len(middlePointLists)):
        tp = middlePointLists[i]
        middlePointLists2D[i][0] = tp[0] - rx
        middlePointLists2D[i][1] = tp[2] - rz
    nc = int(len(middlePointLists2D) / 4)
    if nc > 0:
        kmeans = cluster.KMeans(n_clusters=nc, n_init=10).fit(middlePointLists2D)
        centers = kmeans.cluster_centers_
        for i in range(len(centers)):
            center = centers[i]
            ct = (round(center[0]) - 2, round(center[1]) - 2)
            ntp = BFS(ct)
            globalBuildings.append(light)
            leftBackBottomPoints.append(ivec3(ntp[0] + rx, subHeightMap[ntp[0] + 2][ntp[1] + 2], ntp[1] + rz))


def main():
    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()

    worldSlice = editor.loadWorldSlice(buildRect)
    start = time.time()
    groundBlockName = clearTreeAndLava(buildRect, worldSlice)
    t1 = time.time()
    print('clearTree: ', t1 - start)

    flattenMap(buildRect)

    t2 = time.time()
    print('flattenMap: ', t2 - t1)
    worldSlice = editor.loadWorldSlice(buildRect)
    heightMap = worldSlice.heightmaps["MOTION_BLOCKING"]
    subHeightMap = heightMap[reserveForWall:len(heightMap) - reserveForWall,
                   reserveForWall:len(heightMap[0]) - reserveForWall]

    unitSubHeightMap = subHeightMap - np.min(subHeightMap)
    gd = np.gradient(unitSubHeightMap)
    rectx = buildRect.begin[0]
    rectz = buildRect.begin[1]
    print('sx：', rectx + reserveForWall)
    print('sz：', rectz + reserveForWall)

    base = getTerrain(subHeightMap, rectx + reserveForWall, rectz + reserveForWall, worldSlice, gd)

    totalArea = len(unitSubHeightMap) * len(unitSubHeightMap[0]) - round(0.5 * len(np.where(base == 1)[0])) - len(
        np.where(base == 3)[0])
    ksds=0
    for ii in range(len(base)):
        for jj in range(len(base[0])):
            if base[ii][jj]==2:
                ksds+=1
    print('flat ratio: ',ksds/(len(base)*len(base[0])))
    monu = MonumentBuilding()
    totalArea -= monu.area
    mx, mz = placeMonument(base, gd)
    node1a = (mx + monu.size[0] // 2, mz - 3)
    node2a = (mx - 3, mz + monu.size[2] // 2)
    node3a = (mx + monu.size[0] // 2, mz + monu.size[2] + 2)
    node4a = (mx + monu.size[0] + 2, mz + monu.size[2] // 2)

    t3 = time.time()
    globalBluePrint, globalBuildings, leftBackPoints = \
        randomPlaceBuilding(base, bigBuildings, buildings, padding, gd, rewards)
    # globalBluePrint, globalBuildings, leftBackPoints = \
    #     evo(base, bigBuildings, padding, gd, rewards, 100, 500, 0.1)
    globalBuildings.append(monu)
    leftBackPoints.append((mx, mz))


    t4 = time.time()
    print('build blueprint', t4 - t3)

    node1 = findBetterNode(globalBluePrint, round(len(globalBluePrint) / 2), 0)
    node2 = findBetterNode(globalBluePrint, 0, round(len(globalBluePrint[0]) / 2), horizontal=False)
    node3 = findBetterNode(globalBluePrint, round(len(globalBluePrint) / 2), len(globalBluePrint[0]) - 1)
    node4 = findBetterNode(globalBluePrint, len(globalBluePrint) - 1, round(len(globalBluePrint[0]) / 2),
                           horizontal=False)

    node5a = (leftBackPoints[2][0] + 9, leftBackPoints[2][1] + 4)

    globalBluePrint = AStar(node1, node1a, globalBluePrint, subHeightMap, editor)
    globalBluePrint = AStar(node2, node2a, globalBluePrint, subHeightMap, editor)
    globalBluePrint = AStar(node3, node3a, globalBluePrint, subHeightMap, editor)
    globalBluePrint = AStar(node4, node4a, globalBluePrint, subHeightMap, editor)
    globalBluePrint = AStar((3, 0), node5a, globalBluePrint, subHeightMap, editor)

    t5 = time.time()
    print('plan road ', t5 - t4)

    buildWall(editor, realPlace4Wall, wallPadding, rectx, rectz, heightMap, worldSlice)

    t6 = time.time()
    print('build wall ', t6 - t5)

    lp1 = []
    lp2 = []
    middlePointLists = []
    leftBackBottomPoints = []
    for i in range(len(leftBackPoints)):
        bsize = globalBuildings[i].size
        sx = leftBackPoints[i][0]
        sz = leftBackPoints[i][1]
        bar = np.mean(subHeightMap[sx - 2: sx + bsize[0] + 2, sz - 2: sz + bsize[2] + 2])
        leftBackBottomPoint = addY(leftBackPoints[i], bar) + ivec3(rectx + reserveForWall, 0, rectz + reserveForWall)
        middlePointLists.append(leftBackBottomPoint + ivec3(bsize[0] / 2, 0, bsize[2] / 2))
        leftBackBottomPoints.append(leftBackBottomPoint)
    chooseLight(middlePointLists, globalBuildings, leftBackBottomPoints, globalBluePrint, gd, subHeightMap
                , rectx + reserveForWall, rectz + reserveForWall)
    for i in range(len(leftBackBottomPoints)):
        bsize = globalBuildings[i].size
        sx = leftBackBottomPoints[i][0]-rectx-reserveForWall
        bar = leftBackBottomPoints[i][1]
        sz = leftBackBottomPoints[i][2]-rectz-reserveForWall
        if globalBuildings[i].name == 'light':
            continue

        for x in range(sx - 2, sx + bsize[0] + 2):
            for z in range(sz - 2, sz + bsize[2] + 2):
                try:
                    while subHeightMap[x][z] < bar:
                        lp1.append((rectx + reserveForWall + x, subHeightMap[x][z], rectz + reserveForWall + z))
                        subHeightMap[x][z] += 1
                    while subHeightMap[x][z] > bar:
                        lp2.append((rectx + reserveForWall + x, subHeightMap[x][z] - 1, rectz + reserveForWall + z))
                        subHeightMap[x][z] -= 1
                except:
                    pass
    editor.placeBlockGlobal(lp1, Block(groundBlockName))
    editor.placeBlockGlobal(lp2, Block('minecraft:air'))

    for i in range(len(leftBackBottomPoints)):
        globalBuildings[i].build(editor, leftBackBottomPoints[i])
    placeRoad(editor, rectx + reserveForWall, rectz + reserveForWall, globalBluePrint, subHeightMap, worldSlice)
    print('building: ', time.time() - t6)
    print('total time: ', t1 + t2 + t3 + t4 + t5 + t6)


if __name__ == '__main__':
    main()
