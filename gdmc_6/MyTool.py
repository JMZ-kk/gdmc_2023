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

editor = Editor()


def getCode(p1, p2):
    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()
    worldSlice = editor.loadWorldSlice(buildRect)
    idSet = {}
    for x in range(p1[0], p2[0]):
        for y in range(p1[1], p2[1]):
            for z in range(p1[2], p2[2]):
                id = worldSlice.getBlockGlobal((x, y, z)).id
                if id not in ['minecraft:air', 'minecraft:void_air', 'minecraft:cave_air']:
                    tp = (x - p1[0], y - p1[1], z - p1[2])
                    if id in idSet.keys():
                        idSet[id].append(tp)
                    else:
                        idSet[id] = [tp]
    return idSet


ids = getCode((1053, -60, 1425), (1067, -37, 1438))
for key in ids.keys():
    li = ids[key]
    print('self.',key[10:], end='List=[')
    for tp in li:
        print('(', tp[0], ',', tp[1], ',', tp[2], end='),')
    print(']')

for key in ids.keys():
    li = ids[key]
    print('editor.placeBlockGlobal(self.transform(self.',key[10:],'List, lbb), Block("',key,'"))')
