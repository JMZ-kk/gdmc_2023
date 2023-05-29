from Building import *
from glm import ivec3
from gdpc import geometry, Block
from MonumentStructure import *
import random


class ZCannonStructure(Building):
    def __init__(self,isFilled=True,inverse=False):
        super().__init__((1, 3, 5))
        self.isFilled=isFilled
        self.inverse=inverse
        self.iron_blockList = [(1, 0, 0), (1, 1, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), ]
        self.sticky_pistonList = [(1, 2, 0), (0, 0, 4), ]
        self.repeaterList = [(1, 1, 1), (1, 1, 3), ]
        self.slime_blockList = [(1, 2, 1), (1, 1, 4), ]
        self.stone_buttonList = [(0, 1, 2), ]
        self.dispenserList = [(1, 1, 2), ]

        self.iron_blockList_r = [(1, 0, 4), (1, 1, 4), (1, 0, 3), (1, 0, 2), (1, 0, 1), ]
        self.sticky_pistonList_r = [(1, 2, 4), (0, 0, 0), ]
        self.repeaterList_r = [(1, 1, 3), (1, 1, 1), ]
        self.slime_blockList_r = [(1, 2, 3), (1, 1, 0), ]
        self.stone_buttonList_r = [(0, 1, 2), ]
        self.dispenserList_r = [(1, 1, 2), ]

    def transform(self,li,lbb):
        res=[]
        for i in range(len(li)):
            res.append(li[i]+lbb)
        return res

    def build(self, editor, lbb):
        if self.inverse:
            editor.placeBlockGlobal(self.transform(self.iron_blockList_r, lbb)
                                    , Block("minecraft:iron_block"))
            editor.placeBlockGlobal(self.transform(self.slime_blockList_r, lbb)
                                    , Block("minecraft:slime_block"))
            editor.placeBlockGlobal(lbb + ivec3(1, 2, 4)
                                    , Block("minecraft:sticky_piston", {"facing": "north"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 0, 0)
                                    , Block("minecraft:sticky_piston", {"facing": "up"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 3)
                                    , Block("minecraft:repeater", {"facing": "north", "delay": "2"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "south", "delay": "3"}))
            if self.isFilled:
                editor.placeBlockGlobal(lbb + ivec3(1, 1, 2)
                                        , Block("minecraft:dispenser", {"facing": "up"},
                                                data='{Items: [{Slot: 1b, id: "minecraft:tnt", Count: 64b}]}'))
            else:
                editor.placeBlockGlobal(lbb + ivec3(1, 1, 2)
                                        , Block("minecraft:dispenser", {"facing": "up"}))

            editor.placeBlockGlobal(lbb + ivec3(0, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "west"}))
            editor.placeBlockGlobal(lbb + ivec3(2, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "east"}))
        else:
            editor.placeBlockGlobal(self.transform(self.iron_blockList, lbb)
                                    , Block("minecraft:iron_block"))
            editor.placeBlockGlobal(self.transform(self.slime_blockList, lbb)
                                    , Block("minecraft:slime_block"))
            editor.placeBlockGlobal(lbb + ivec3(1, 2, 0)
                                    , Block("minecraft:sticky_piston", {"facing": "south"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 0, 4)
                                    , Block("minecraft:sticky_piston", {"facing": "up"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "south", "delay": "2"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 3)
                                    , Block("minecraft:repeater", {"facing": "north", "delay": "3"}))
            if self.isFilled:
                editor.placeBlockGlobal(lbb + ivec3(1, 1, 2)
                                        , Block("minecraft:dispenser", {"facing": "up"},
                                                data='{Items: [{Slot: 1b, id: "minecraft:tnt", Count: 64b}]}'))
            else:
                editor.placeBlockGlobal(lbb + ivec3(1, 1, 2)
                                        , Block("minecraft:dispenser", {"facing": "up"}))

            editor.placeBlockGlobal(lbb + ivec3(0, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "west"}))
            editor.placeBlockGlobal(lbb + ivec3(2, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "east"}))