from Building import *
from glm import ivec3
from gdpc import geometry, Block
from ZCannonStructure import *
import random


class MunitionsFactory(Building):
    def __init__(self):
        super().__init__((7, 10, 17))
        self.zCannon=ZCannonStructure(isFilled=False)
        self.clearable = False

        self.white_concreteList = [(0, 0, 0), (0, 0, 6), (0, 0, 7), (0, 0, 8), (0, 0, 9), (0, 0, 10), (0, 0, 11),
                                   (0, 0, 12), (0, 0, 13), (0, 0, 14), (0, 0, 15), (0, 1, 0), (0, 1, 6), (0, 1, 7),
                                   (0, 1, 11), (0, 1, 15), (0, 2, 0), (0, 2, 6), (0, 2, 7), (0, 2, 11), (0, 2, 15),
                                   (0, 3, 0), (0, 3, 6), (0, 3, 7), (0, 3, 8), (0, 3, 9), (0, 3, 10), (0, 3, 11),
                                   (0, 3, 12), (0, 3, 13), (0, 3, 14), (0, 3, 15), (0, 4, 0), (0, 4, 6), (0, 4, 7),
                                   (0, 4, 8), (0, 4, 9), (0, 4, 10), (0, 4, 11), (0, 4, 12), (0, 4, 13), (0, 4, 14),
                                   (0, 4, 15), (0, 5, 0), (0, 5, 6), (0, 6, 0), (0, 6, 6), (0, 7, 0), (0, 7, 6),
                                   (0, 8, 0), (0, 8, 6), (6, 0, 0), (6, 0, 6), (6, 0, 15), (6, 1, 0), (6, 1, 6),
                                   (6, 1, 15), (6, 2, 0), (6, 2, 6), (6, 2, 15), (6, 3, 0), (6, 3, 6), (6, 3, 15),
                                   (6, 4, 0), (6, 4, 6), (6, 4, 15), (6, 5, 0), (6, 5, 6), (6, 6, 0), (6, 6, 6),
                                   (6, 7, 0), (6, 7, 6), (6, 8, 0), (6, 8, 6), ]
        self.yellow_concreteList = [(0, 0, 1), (0, 0, 5), (0, 1, 1), (0, 1, 5), (0, 2, 1), (0, 2, 5), (0, 3, 1),
                                    (0, 3, 2), (0, 3, 3), (0, 3, 4), (0, 3, 5), (0, 4, 1), (0, 4, 5), (0, 5, 1),
                                    (0, 5, 5), (0, 6, 1), (0, 6, 2), (0, 6, 3), (0, 6, 4), (0, 6, 5), (1, 0, 0),
                                    (1, 0, 6), (1, 1, 0), (1, 1, 6), (1, 2, 0), (1, 2, 6), (1, 3, 0), (1, 3, 6),
                                    (1, 4, 0), (1, 4, 6), (1, 5, 0), (1, 5, 6), (1, 6, 0), (1, 6, 6), (2, 3, 0),
                                    (2, 5, 6), (2, 6, 0), (2, 6, 6), (3, 3, 0), (3, 5, 6), (3, 6, 0), (3, 6, 6),
                                    (4, 3, 0), (4, 5, 6), (4, 6, 0), (4, 6, 6), (5, 0, 0), (5, 0, 6), (5, 1, 0),
                                    (5, 1, 6), (5, 2, 0), (5, 2, 6), (5, 3, 0), (5, 3, 6), (5, 4, 0), (5, 4, 6),
                                    (5, 5, 0), (5, 5, 6), (5, 6, 0), (5, 6, 6), (6, 0, 1), (6, 0, 5), (6, 1, 1),
                                    (6, 1, 5), (6, 2, 1), (6, 2, 5), (6, 3, 1), (6, 3, 2), (6, 3, 3), (6, 3, 4),
                                    (6, 3, 5), (6, 4, 1), (6, 4, 5), (6, 5, 1), (6, 5, 5), (6, 6, 1), (6, 6, 2),
                                    (6, 6, 3), (6, 6, 4), (6, 6, 5), ]
        self.glassList = [(0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 8), (0, 1, 9),
                          (0, 1, 10), (0, 1, 12), (0, 1, 13), (0, 1, 14), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 2, 8),
                          (0, 2, 9), (0, 2, 10), (0, 2, 12), (0, 2, 13), (0, 2, 14), (0, 4, 2), (0, 4, 3), (0, 4, 4),
                          (0, 5, 2), (0, 5, 3), (0, 5, 4), (1, 5, 8), (1, 5, 9), (1, 5, 10), (1, 5, 11), (1, 5, 12),
                          (1, 5, 13), (1, 5, 14), (2, 0, 0), (2, 1, 0), (2, 2, 0), (2, 4, 0), (2, 5, 0), (2, 5, 8),
                          (2, 5, 9), (2, 5, 10), (2, 5, 11), (2, 5, 12), (2, 5, 13), (2, 5, 14), (3, 0, 0), (3, 1, 0),
                          (3, 2, 0), (3, 4, 0), (3, 5, 0), (3, 5, 8), (3, 5, 9), (3, 5, 10), (3, 5, 11), (3, 5, 12),
                          (3, 5, 13), (3, 5, 14), (4, 0, 0), (4, 1, 0), (4, 2, 0), (4, 4, 0), (4, 5, 0), (4, 5, 8),
                          (4, 5, 9), (4, 5, 10), (4, 5, 11), (4, 5, 12), (4, 5, 13), (4, 5, 14), (5, 5, 8), (5, 5, 9),
                          (5, 5, 10), (5, 5, 11), (5, 5, 12), (5, 5, 13), (5, 5, 14), (6, 4, 2), (6, 4, 3), (6, 4, 4),
                          (6, 5, 2), (6, 5, 3), (6, 5, 4), ]
        self.red_concreteList = [(0, 5, 7), (0, 5, 8), (0, 5, 9), (0, 5, 10), (0, 5, 11), (0, 5, 12), (0, 5, 13),
                                 (0, 5, 14), (0, 5, 15), (0, 9, 0), (0, 9, 1), (0, 9, 2), (0, 9, 3), (0, 9, 4),
                                 (0, 9, 5), (0, 9, 6), (1, 5, 7), (1, 5, 15), (1, 9, 0), (1, 9, 6), (1, 10, 1),
                                 (1, 10, 2), (1, 10, 3), (1, 10, 4), (1, 10, 5), (2, 5, 7), (2, 5, 15), (2, 9, 0),
                                 (2, 9, 6), (2, 10, 1), (2, 10, 5), (2, 11, 2), (2, 11, 3), (2, 11, 4), (3, 5, 7),
                                 (3, 5, 15), (3, 9, 0), (3, 9, 6), (3, 10, 1), (3, 10, 5), (3, 11, 2), (3, 11, 4),
                                 (3, 12, 3), (4, 5, 7), (4, 5, 15), (4, 9, 0), (4, 9, 6), (4, 10, 1), (4, 10, 5),
                                 (4, 11, 2), (4, 11, 3), (4, 11, 4), (5, 5, 7), (5, 5, 15), (5, 9, 0), (5, 9, 6),
                                 (5, 10, 1), (5, 10, 2), (5, 10, 3), (5, 10, 4), (5, 10, 5), (6, 5, 7), (6, 5, 8),
                                 (6, 5, 9), (6, 5, 10), (6, 5, 11), (6, 5, 12), (6, 5, 13), (6, 5, 14), (6, 5, 15),
                                 (6, 9, 0), (6, 9, 1), (6, 9, 2), (6, 9, 3), (6, 9, 4), (6, 9, 5), (6, 9, 6), ]
        self.lanternList = [(0, 8, 3), (3, 8, 0), (3, 8, 6), (6, 8, 3), ]
        self.crafting_tableList = [(1, 0, 1), ]
        self.chestList = [(1, 0, 5), ]
        self.tntList = [(1, 0, 7), (1, 0, 8), (1, 0, 9), (1, 0, 10), (1, 1, 7), (1, 1, 8), (1, 1, 9), (1, 2, 7),
                        (1, 2, 9), ]
        self.slime_blockList = [(1, 0, 12), (1, 0, 13), (1, 1, 13), (2, 0, 13), (3, 0, 10), ]
        self.sticky_pistonList = [(3, 0, 11), ]
        self.glowstoneList = [(3, 11, 3), ]
        self.dispenserList = [(4, 0, 14), (5, 0, 14), ]

    def transform(self,li,lbb):
        res=[]
        for i in range(len(li)):
            res.append(li[i]+lbb)
        return res

    def build(self, editor, lbb):
        editor.placeBlockGlobal(self.transform(self.glassList, lbb), Block("minecraft:glass"))
        editor.placeBlockGlobal(self.transform(self.slime_blockList, lbb), Block("minecraft:slime_block"))
        editor.placeBlockGlobal(self.transform(self.sticky_pistonList, lbb), Block("minecraft:sticky_piston"))
        editor.placeBlockGlobal(self.transform(self.yellow_concreteList, lbb), Block("minecraft:yellow_concrete"))
        editor.placeBlockGlobal(self.transform(self.red_concreteList, lbb), Block("minecraft:red_concrete"))
        editor.placeBlockGlobal(self.transform(self.lanternList, lbb), Block("minecraft:lantern"))
        editor.placeBlockGlobal(self.transform(self.glowstoneList, lbb), Block("minecraft:glowstone"))
        editor.placeBlockGlobal(self.transform(self.dispenserList, lbb), Block("minecraft:dispenser"))
        editor.placeBlockGlobal(self.transform(self.white_concreteList, lbb), Block("minecraft:white_concrete"))
        self.zCannon.build(editor,lbb+ivec3(4,0,8))
        geometry.placeCuboid(editor,lbb+ivec3(1,0,7),lbb+ivec3(1,0,10),Block("minecraft:tnt"))
        geometry.placeCuboid(editor, lbb + ivec3(1, 1, 7), lbb + ivec3(1, 1, 9), Block("minecraft:tnt"))
        editor.placeBlockGlobal(lbb+ivec3(1,2,9),Block("minecraft:tnt"))
        editor.placeBlockGlobal(lbb+ivec3(1,0,1),Block("minecraft:chest"))
        editor.placeBlockGlobal(lbb + ivec3(1, 0, 5), Block("minecraft:crafting_table"))