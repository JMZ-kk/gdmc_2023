from typing import Optional, Iterable, Set, Tuple, Union
import random
from gdpc import __url__, Editor, Block, Box, lookup
import numpy as np
from glm import ivec2, ivec3
from gdpc.vector_tools import Vec3iLike, Rect, Box, addY, dropY
from Farm import *
from MyPoint import *

from static_block_lists import *
import time
from sklearn import cluster


def addToList(p, clist):
    for i in range(len(clist)):
        if p.fn > clist[i].fn:
            clist.insert(i, p)
            return
        elif p.fn == clist[i].fn and p.gn > clist[i].gn:
            clist.insert(i, p)
            return
    clist.append(p)


def AStar(node1, node2, map, subHeightMap, editor):
    def calDisToTar(x, z):
        return abs(x - node2[0]) + abs(z - node2[1])

    def islegalPoint(x, z):
        return (map[x][z] != 3 and map[x][z] != 6) or (x == node2[0] and z == node2[1])

    def getHeightPenalty(x1, z1, x2, z2):
        if map[x2][z2] == 1:
            return 2
        dis = abs(subHeightMap[x1][z1] - subHeightMap[x2][z2])
        if dis < 2:
            return 1
        return 5 ^ dis + 1

    def setValue(x, z, father=None):
        if map[x][z] == 1 or map[x][z] == 8:
            map[x][z] = 8  # 浮桥
        else:
            map[x][z] = 7  # 正常路
        if father != None:
            if subHeightMap[x][z] - subHeightMap[father.x][father.z] > 1:
                subHeightMap[father.x][father.z] = subHeightMap[x][z]
                editor.placeBlockGlobal((father.x, subHeightMap[x][z] - 1, father.z), Block('minecraft:dirt'))
            if subHeightMap[x][z] - subHeightMap[father.x][father.z] < -1:
                subHeightMap[father.x][father.z] = subHeightMap[father.x][father.z] - 1
                editor.placeBlockGlobal((father.x, subHeightMap[father.x][father.z] - 1, father.z),
                                        Block('minecraft:air'))
                editor.placeBlockGlobal((father.x, subHeightMap[father.x][father.z] - 2, father.z),
                                        Block('minecraft:dirt'))

    if (node1[0] == -1 and node1[1] == -1) or (node2[0] == -1 and node2[1] == -1):
        return map

    start = MyPoint(node1[0], node1[1], 0, calDisToTar(node1[0], node1[1]))

    checkedArray = np.zeros((len(map), len(map[0])))
    checking = [start]  # 靠后的fn最小

    while len(checking) > 0:
        tp = checking.pop()
        x = tp.x
        z = tp.z
        if x == node2[0] and z == node2[1]:
            temp = tp
            setValue(temp.x, temp.z, temp.father)
            while temp.father is not None:
                temp.father.son = temp
                temp = temp.father
                setValue(temp.x, temp.z, temp.father)
                if temp.x > 0 and map[temp.x - 1][temp.z] != 3 and abs(
                        subHeightMap[temp.x][temp.z] - subHeightMap[temp.x - 1][temp.z]) < 2:
                    setValue(temp.x - 1, temp.z)
                if temp.x < len(map) - 1 and map[temp.x + 1][temp.z] != 3 and abs(
                        subHeightMap[temp.x][temp.z] - subHeightMap[temp.x + 1][temp.z]) < 2:
                    setValue(temp.x + 1, temp.z)
                if temp.z > 0 and map[temp.x][temp.z - 1] != 3 and abs(
                        subHeightMap[temp.x][temp.z] - subHeightMap[temp.x][temp.z - 1]) < 2:
                    setValue(temp.x, temp.z - 1)
                if temp.z < len(map[0]) - 1 and map[temp.x][temp.z + 1] != 3 and abs(
                        subHeightMap[temp.x][temp.z] - subHeightMap[temp.x][temp.z + 1]) < 2:
                    setValue(temp.x, temp.z + 1)
            break
        children = []
        if x > 0 and islegalPoint(x - 1, z):
            children.append(MyPoint(x - 1, z, tp.gn + getHeightPenalty(x - 1, z, x, z), calDisToTar(x - 1, z), tp))
        if x < len(map) - 1 and islegalPoint(x + 1, z):
            children.append(MyPoint(x + 1, z, tp.gn + getHeightPenalty(x + 1, z, x, z), calDisToTar(x + 1, z), tp))
        if z > 0 and islegalPoint(x, z - 1):
            children.append(MyPoint(x, z - 1, tp.gn + getHeightPenalty(x, z - 1, x, z), calDisToTar(x, z - 1), tp))
        if z < len(map[0]) - 1 and islegalPoint(x, z + 1):
            children.append(MyPoint(x, z + 1, tp.gn + getHeightPenalty(x, z + 1, x, z), calDisToTar(x, z + 1), tp))

        for subPoint in children:
            p = subPoint.getInList(checking)
            if p is not None:
                if subPoint.fn < p.fn:
                    checking.remove(p)
                    p.fn = subPoint.fn
                    p.gn = subPoint.gn
                    p.hn = subPoint.hn
                    addToList(p, checking)
                    p.father = tp

            elif checkedArray[subPoint.x][subPoint.z] == 0:
                subPoint.father = tp
                addToList(subPoint, checking)
        checkedArray[tp.x][tp.z] = 1
    return map


def findBetterNode(map, x, z, horizontal=True):
    try:
        if horizontal:
            for i in range(0, len(map)):
                move = i // 2
                if i % 2 == 0:
                    if map[x + move][z] != 3 and map[x + move][z] != 1 and map[x + move][z] != 6:
                        return (x + move, z)
                else:
                    if map[x - move][z] != 3 and map[x - move][z] != 1 and map[x - move][z] != 6:
                        return (x - move, z)
        else:
            for i in range(0, len(map[0]) - 1):
                move = i // 2
                if i % 2 == 0:
                    if map[x][z + move] != 3 and map[x][z + move] != 1 and map[x][z + move] != 6:
                        return (x, z + move)
                else:
                    if map[x][z - move] != 3 and map[x][z - move] != 1 and map[x][z - move] != 6:
                        return (x, z - move)
    except:
        return (-1, -1)
    return (-1, -1)

def placeRoad(editor, sx, sz, roadBluePrint, subHeightMap, worldSlice):
    for i in range(len(roadBluePrint)):
        for j in range(len(roadBluePrint[0])):
            if roadBluePrint[i][j] == 7:
                editor.placeBlockGlobal((sx + i, subHeightMap[i][j] - 1, sz + j), Block("minecraft:mossy_cobblestone"))
                roadBluePrint[i][j] = 9
                if worldSlice.getBlockGlobal((sx + i, subHeightMap[i][j], sz + j)).id not in ['minecraft:air',
                                                                                              'minecraft:void_air',
                                                                                              'minecraft:cave_air']:
                    editor.placeBlockGlobal((sx + i, subHeightMap[i][j], sz + j), Block("minecraft:air"))
            elif roadBluePrint[i][j] == 6:
                editor.placeBlockGlobal((sx + i, subHeightMap[i][j] - 1, sz + j), Block("minecraft:cobblestone"))
                roadBluePrint[i][j] = 9
                if worldSlice.getBlockGlobal((sx + i, subHeightMap[i][j], sz + j)).id not in ['minecraft:air',
                                                                                              'minecraft:void_air',
                                                                                              'minecraft:cave_air']:
                    editor.placeBlockGlobal((sx + i, subHeightMap[i][j], sz + j), Block("minecraft:air"))
            elif roadBluePrint[i][j] == 8:
                editor.placeBlockGlobal((sx + i, subHeightMap[i][j], sz + j), Block("minecraft:oak_wood"))
                try:
                    if roadBluePrint[i + 1][j] == 1 or roadBluePrint[i - 1][j] == 1 or roadBluePrint[i][j + 1] == 1 or \
                            roadBluePrint[i][j - 1] == 1:
                        editor.placeBlockGlobal((sx + i, subHeightMap[i][j] + 1, sz + j), Block("minecraft:oak_fence"))
                except:
                    pass
                roadBluePrint[i][j] = 9
