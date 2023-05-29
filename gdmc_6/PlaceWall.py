import numpy as np
from Farm import *
from static_block_lists import *
from CannonStructure import *
from ZCannonStructure import *
from StreetLight import *


def buildWall(editor, realPlace4Wall, wallPadding, rectx, rectz, heightMap, worldSlice):
    highest = np.max(heightMap) - np.mean(heightMap)+1
    # highest = min(highest, len(heightMap) - 2 * realPlace4Wall)
    # highest = min(highest, len(heightMap[0]) - 2 * realPlace4Wall)

    if highest < 5:
        tallest = np.max(heightMap) + 2
    elif highest > 9:
        tallest = np.max(heightMap) - 2
    else:
        tallest = np.max(heightMap)

    def buildPlane(x1, z1, x2, z2, front=True, top=tallest):
        if abs(x1 - x2) < abs(z1 - z2):
            geometry.placeCuboid(editor, (rectx + x1, top + 1, rectz + z1 + realPlace4Wall),
                                 (rectx + x2, top + 2, rectz + z2 - realPlace4Wall),
                                 Block("minecraft:stone"))
            if front:
                geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z1),
                                     (rectx + x1, top + 3, rectz + z2),
                                     Block("minecraft:stone_brick_wall"))
                geometry.placeCuboid(editor, (rectx + x2, top + 3, rectz + z1 + realPlace4Wall),
                                     (rectx + x2, top + 3, rectz + z2 - realPlace4Wall),
                                     Block("minecraft:stone_brick_wall"))
            else:
                geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z1 + realPlace4Wall),
                                     (rectx + x1, top + 3, rectz + z2 - realPlace4Wall),
                                     Block("minecraft:stone_brick_wall"))
                geometry.placeCuboid(editor, (rectx + x2, top + 3, rectz + z1),
                                     (rectx + x2, top + 3, rectz + z2),
                                     Block("minecraft:stone_brick_wall"))
        else:
            geometry.placeCuboid(editor, (rectx + x1 + realPlace4Wall, top + 1, rectz + z1),
                                 (rectx + x2 - realPlace4Wall, top + 2, rectz + z2),
                                 Block("minecraft:stone"))
            if front:
                geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z1),
                                     (rectx + x2, top + 3, rectz + z1),
                                     Block("minecraft:stone_brick_wall"))
                geometry.placeCuboid(editor, (rectx + x1 + realPlace4Wall, top + 3, rectz + z2),
                                     (rectx + x2 - realPlace4Wall, top + 3, rectz + z2),
                                     Block("minecraft:stone_brick_wall"))
            else:
                geometry.placeCuboid(editor, (rectx + x1 + realPlace4Wall, top + 3, rectz + z1),
                                     (rectx + x2 - realPlace4Wall, top + 3, rectz + z1),
                                     Block("minecraft:stone_brick_wall"))
                geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z2),
                                     (rectx + x2, top + 3, rectz + z2),
                                     Block("minecraft:stone_brick_wall"))

    def buildTower(x1, z1, x2, z2, top=tallest):
        editor.flushBuffer()
        subHeightMap = heightMap[x1:x2 + 1, z1:z2 + 1]
        shortest = np.min(subHeightMap)
        geometry.placeCuboid(editor, (rectx + x1, shortest - 10, rectz + z1),
                             (rectx + x2, top + 2, rectz + z2),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x1, top + 6, rectz + z1),
                             (rectx + x2, top + 7, rectz + z2),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x1, top + 8, rectz + z1),
                             (rectx + x2, top + 8, rectz + z2),
                             Block("minecraft:stone_brick_wall"))
        geometry.placeCuboid(editor, (rectx + x1 + 1, top + 8, rectz + z1 + 1),
                             (rectx + x2 - 1, top + 8, rectz + z2 - 1),
                             Block("minecraft:air"))
        geometry.placeCuboid(editor, (rectx + x1, top + 11, rectz + z1),
                             (rectx + x2, top + 12, rectz + z2),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x1, top + 13, rectz + z1),
                             (rectx + x2, top + 13, rectz + z2),
                             Block("minecraft:stone_brick_wall"))
        geometry.placeCuboid(editor, (rectx + x1 + 1, top + 14, rectz + z1 + 1),
                             (rectx + x2 - 1, top + 14, rectz + z2 - 1),
                             Block("minecraft:stone_brick_wall"))
        geometry.placeCuboid(editor, (rectx + x1 + 2, top + 15, rectz + z1 + 2),
                             (rectx + x2 - 2, top + 15, rectz + z2 - 2),
                             Block("minecraft:campfire"))

        geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z1),
                             (rectx + x1, top + 10, rectz + z1),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x1, top + 3, rectz + z2),
                             (rectx + x1, top + 10, rectz + z2),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x2, top + 3, rectz + z1),
                             (rectx + x2, top + 10, rectz + z1),
                             Block("minecraft:stone"))
        geometry.placeCuboid(editor, (rectx + x2, top + 3, rectz + z2),
                             (rectx + x2, top + 10, rectz + z2),
                             Block("minecraft:stone"))

    def buildBase(l1, l2, horizontal=True):
        last = realPlace4Wall
        if horizontal:
            x = round(len(heightMap) / 2)
            z = l1
            height = heightMap[x][z]
            h2 = heightMap[x][z + realPlace4Wall - 1]
            openDoor = abs(height - h2) < 2
            height = max(height, h2)
            for i in range(realPlace4Wall, len(heightMap) - realPlace4Wall):
                kind = worldSlice.getBlockGlobal((rectx + i, heightMap[i][l1] - 1, rectz + l1)).id
                kind2 = worldSlice.getBlockGlobal((rectx + i, heightMap[i][l2] - 1, rectz + l2)).id
                if kind in WATER_BLOCKS and kind2 in WATER_BLOCKS:
                    if i > last:
                        openDoor = False
                        subHeightMap = heightMap[last:i, l1:l2 + 1]
                        shortest = np.min(subHeightMap)
                        geometry.placeCuboidHollow(editor, (rectx + last, shortest, rectz + l1),
                                                   (rectx + i - 1, tallest, rectz + l2),
                                                   Block("minecraft:stone"))
                        last = 99999
                elif last == 99999:
                    last = i
            if len(heightMap) > last:
                subHeightMap = heightMap[last:len(heightMap) - realPlace4Wall, l1:l2 + 1]
                shortest = np.min(subHeightMap)
                geometry.placeCuboidHollow(editor, (rectx + last, shortest, rectz + l1),
                                           (rectx + len(heightMap) - realPlace4Wall - 1, tallest, rectz + l2),
                                           Block("minecraft:stone"))
            if openDoor:
                dis = tallest - height
                hwidth = max(dis // 2, 1)
                geometry.placeCuboid(editor, (rectx + x - hwidth, height, rectz + z),
                                     (rectx + x + hwidth, tallest - 1, rectz + z + realPlace4Wall - 1),
                                     Block("minecraft:air"))
                geometry.placeCuboid(editor, (rectx + x - hwidth - 1, height - 5, rectz + z),
                                     (rectx + x - hwidth - 1, tallest, rectz + z + realPlace4Wall - 1),
                                     Block("minecraft:stone"))
                geometry.placeCuboid(editor, (rectx + x + hwidth + 1, height - 5, rectz + z),
                                     (rectx + x + hwidth + 1, tallest, rectz + z + realPlace4Wall - 1),
                                     Block("minecraft:stone"))
                geometry.placeCuboid(editor, (rectx + x - hwidth, height - 1, rectz + z),
                                     (rectx + x + hwidth, height - 1, rectz + z + realPlace4Wall - 1),
                                     Block("minecraft:stone"))
        else:
            x = l1
            z = round(len(heightMap[0]) / 2)
            height = heightMap[x][z]
            h2 = heightMap[x + realPlace4Wall - 1][z]
            openDoor = abs(height - h2) < 2
            height = max(height, h2)
            for i in range(realPlace4Wall, len(heightMap[0]) - realPlace4Wall):
                kind = worldSlice.getBlockGlobal((rectx + l1, heightMap[l1][i] - 1, rectz + i)).id
                kind2 = worldSlice.getBlockGlobal((rectx + l2, heightMap[l2][i] - 1, rectz + i)).id
                if kind in WATER_BLOCKS and kind2 in WATER_BLOCKS:
                    if i > last:
                        openDoor = False
                        subHeightMap = heightMap[l1:l2 + 1, last:i]
                        shortest = np.min(subHeightMap)
                        geometry.placeCuboidHollow(editor, (rectx + l1, shortest, rectz + last),
                                                   (rectx + l2, tallest, rectz + i - 1),
                                                   Block("minecraft:stone"))
                        last = 99999
                elif last == 99999:
                    last = i
            if len(heightMap[0]) > last:
                subHeightMap = heightMap[l1:l2 + 1, last:len(heightMap[0]) - realPlace4Wall]
                shortest = np.min(subHeightMap)
                geometry.placeCuboidHollow(editor, (rectx + l1, shortest, rectz + last),
                                           (rectx + l2, tallest, rectz + len(heightMap[0]) - realPlace4Wall - 1),
                                           Block("minecraft:stone"))
            if openDoor:
                dis = tallest - height
                hwidth = max(dis // 2, 1)
                geometry.placeCuboid(editor, (rectx + x, height, rectz + z - hwidth),
                                     (rectx + x + realPlace4Wall - 1, tallest - 1, rectz + z + hwidth),
                                     Block("minecraft:air"))
                geometry.placeCuboid(editor, (rectx + x + 1, height - 5, rectz + z + hwidth + 1),
                                     (rectx + x + realPlace4Wall - 1, tallest, rectz + z + hwidth + 1),
                                     Block("minecraft:stone"))
                geometry.placeCuboid(editor, (rectx + x + 1, height - 5, rectz + z - hwidth - 1),
                                     (rectx + x + realPlace4Wall - 1, tallest, rectz + z - hwidth - 1),
                                     Block("minecraft:stone"))
                geometry.placeCuboid(editor, (rectx + x, height - 1, rectz + z - hwidth),
                                     (rectx + x + realPlace4Wall - 1, height - 1, rectz + z + hwidth),
                                     Block("minecraft:stone"))

    l1 = 0
    l2 = realPlace4Wall - 1
    buildBase(l1, l2)

    l1 = len(heightMap[0]) - realPlace4Wall
    l2 = len(heightMap[0]) - 1
    buildBase(l1, l2)

    l1 = 0
    l2 = realPlace4Wall - 1
    buildBase(l1, l2, horizontal=False)

    l1 = len(heightMap) - realPlace4Wall
    l2 = len(heightMap) - 1
    buildBase(l1, l2, horizontal=False)

    buildPlane(0, 0, realPlace4Wall - 1, len(heightMap[0]) - 1)
    buildPlane(len(heightMap) - realPlace4Wall, 0, len(heightMap) - 1, len(heightMap[0]) - 1, front=False)
    buildPlane(0, 0, len(heightMap) - 1, realPlace4Wall - 1)
    buildPlane(0, len(heightMap[0]) - realPlace4Wall, len(heightMap) - 1, len(heightMap[0]) - 1, front=False)

    c1 = ZCannonStructure(inverse=True)
    c2 = ZCannonStructure()
    c3 = CannonStructure(inverse=True)
    c4 = CannonStructure()
    light = StreetLight(simple=True)
    cnt = 0
    for i in range(realPlace4Wall + 3, len(heightMap) - realPlace4Wall - 4, 6):
        if cnt % 2 == 0:
            c1.build(editor, ivec3(rectx + i, tallest + 3, rectz + 2))
            c2.build(editor, ivec3(rectx + i, tallest + 3, rectz + len(heightMap[0]) - 7))
        else:
            light.build(editor, ivec3(rectx + i - 2, tallest + 3, rectz + 2))
            light.build(editor, ivec3(rectx + i - 2, tallest + 3, rectz + len(heightMap[0]) - 7))
        cnt += 1
    cnt = 0
    for i in range(realPlace4Wall + 3, len(heightMap[0]) - realPlace4Wall - 4, 7):
        if cnt % 2 == 0:
            c3.build(editor, ivec3(rectx + 2, tallest + 3, rectz + i))
            c4.build(editor, ivec3(rectx + len(heightMap) - 7, tallest + 3, rectz + i))
        else:
            light.build(editor, ivec3(rectx + 2, tallest + 3, rectz + i - 2))
            light.build(editor, ivec3(rectx + len(heightMap) - 7, tallest + 3, rectz + i - 2))
        cnt += 1

    buildTower(len(heightMap) - realPlace4Wall, len(heightMap[0]) - realPlace4Wall, len(heightMap) - 1,
               len(heightMap[0]) - 1)
    buildTower(0, len(heightMap[0]) - realPlace4Wall, realPlace4Wall - 1, len(heightMap[0]) - 1)  # 右上
    buildTower(0, 0, realPlace4Wall - 1, realPlace4Wall - 1)  # 左上
    buildTower(len(heightMap) - realPlace4Wall, 0, len(heightMap) - 1, realPlace4Wall - 1)  # 左下

    airList = []
    s = realPlace4Wall
    # baseHeight = np.min(heightMap[s:s + wallPadding - 1, s:s + wallPadding - 1])
    baseHeight = heightMap[s + wallPadding][s + 1]
    for i in range(wallPadding - 1):
        for j in range(wallPadding - 1):
            dis = heightMap[s + i][s + j] - baseHeight
            if dis > 0:
                for k in range(dis):
                    airList.append((rectx + s + i, baseHeight + k, rectz + s + j))
    editor.placeBlockGlobal(airList, Block("minecraft:air"))
    geometry.placeCuboid(editor, (rectx + s, baseHeight - 1, rectz + s),
                         (rectx + s + wallPadding - 2, baseHeight - 1, rectz + s + wallPadding - 2),
                         Block("minecraft:stone"))

    for i in range(wallPadding - 1):
        if i == wallPadding - 2:
            geometry.placeLine(editor, (rectx + s + i, baseHeight, rectz + s + wallPadding - 1),
                               (rectx + s + i, tallest + 2, rectz + s + wallPadding + tallest - baseHeight + 1),
                               Block("minecraft:stone"))
        else:
            geometry.placeLine(editor, (rectx + s + i, baseHeight, rectz + s + wallPadding - 1),
                               (rectx + s + i, tallest + 2, rectz + s + wallPadding + tallest - baseHeight + 1),
                               Block("minecraft:stone_brick_stairs", {"facing": "south"}))
        geometry.placeLine(editor, (rectx + s + i, baseHeight, rectz + s + wallPadding),
                           (rectx + s + i, tallest + 2, rectz + s + wallPadding + tallest - baseHeight + 2),
                           Block("minecraft:stone"))
    geometry.placeLine(editor, (rectx + s + wallPadding - 2, baseHeight + 1, rectz + s + wallPadding - 1),
                       (rectx + s + wallPadding - 2, tallest + 3, rectz + s + wallPadding + tallest - baseHeight + 1),
                       Block("minecraft:stone_brick_wall"))
    geometry.placeLine(editor, (rectx + s + wallPadding - 2, baseHeight + 2, rectz + s + wallPadding - 1),
                       (rectx + s + wallPadding - 2, tallest + 3, rectz + s + wallPadding + tallest - baseHeight),
                       Block("minecraft:stone_brick_wall"))
    editor.placeBlockGlobal((rectx + s - 1, tallest + 3, rectz + s + wallPadding + tallest - baseHeight + 1),
                            Block("minecraft:air"))
    geometry.placeLine(editor,
                       (rectx + s + wallPadding - 2, tallest + 3, rectz + s + wallPadding + tallest - baseHeight + 2),
                       (rectx + s - 1, tallest + 3, rectz + s + wallPadding + tallest - baseHeight + 2),
                       Block("minecraft:stone_brick_wall"))
