from Building import *
from glm import ivec3
from gdpc import geometry, Block
from MonumentStructure import *
import random


class CannonStructure(Building):
    def __init__(self,isFilled=True,inverse=False):
        super().__init__((5, 3, 1))
        self.isFilled=isFilled
        self.inverse = inverse
        self.iron_blockList = [(0, 0, 1), (0, 1, 1), (1, 0, 1), (2, 0, 1), (3, 0, 1), ]
        self.sticky_pistonList = [(0, 2, 1), (4, 0, 1), ]
        self.repeaterList = [(1, 1, 1), (3, 1, 1), ]
        self.slime_blockList = [(1, 2, 1), (4, 1, 1), ]
        self.stone_buttonList = [(2, 1, 0), ]
        self.dispenserList = [(2, 1, 1), ]

        self.iron_blockList_r = [(4, 0, 1), (4, 1, 1), (3, 0, 1), (2, 0, 1), (1, 0, 1), ]
        self.sticky_pistonList_r = [(4, 2, 1), (0, 0, 1), ]
        self.repeaterList_r = [(3, 1, 1), (1, 1, 1), ]
        self.slime_blockList_r = [(3, 2, 1), (0, 1, 1), ]
        self.stone_buttonList_r = [(2, 1, 0), ]
        self.dispenserList_r = [(2, 1, 1), ]

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
            editor.placeBlockGlobal(lbb+ivec3(4, 2, 1)
                                    , Block("minecraft:sticky_piston",{"facing":"west"}))
            editor.placeBlockGlobal(lbb + ivec3(0, 0, 1)
                                    , Block("minecraft:sticky_piston", {"facing": "up"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "east","delay":"3"}))
            editor.placeBlockGlobal(lbb + ivec3(3, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "west","delay":"2"}))
            if self.isFilled:
                editor.placeBlockGlobal(lbb + ivec3(2, 1, 1)
                                        , Block("minecraft:dispenser", {"facing": "up"}, data='{Items: [{Slot: 1b, id: "minecraft:tnt", Count: 64b}]}'))
            else:
                editor.placeBlockGlobal(lbb + ivec3(2, 1, 1)
                                        , Block("minecraft:dispenser", {"facing": "up"}))

            editor.placeBlockGlobal(lbb + ivec3(2, 1, 0)
                                    , Block("minecraft:oak_button", {"facing": "north"}))
            editor.placeBlockGlobal(lbb + ivec3(2, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "south"}))
        else:
            editor.placeBlockGlobal(self.transform(self.iron_blockList, lbb)
                                    , Block("minecraft:iron_block"))
            editor.placeBlockGlobal(self.transform(self.slime_blockList, lbb)
                                    , Block("minecraft:slime_block"))
            editor.placeBlockGlobal(lbb + ivec3(0, 2, 1)
                                    , Block("minecraft:sticky_piston", {"facing": "east"}))
            editor.placeBlockGlobal(lbb + ivec3(4, 0, 1)
                                    , Block("minecraft:sticky_piston", {"facing": "up"}))
            editor.placeBlockGlobal(lbb + ivec3(1, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "east", "delay": "2"}))
            editor.placeBlockGlobal(lbb + ivec3(3, 1, 1)
                                    , Block("minecraft:repeater", {"facing": "west", "delay": "3"}))
            if self.isFilled:
                editor.placeBlockGlobal(lbb + ivec3(2, 1, 1)
                                        , Block("minecraft:dispenser", {"facing": "up"},
                                                data='{Items: [{Slot: 1b, id: "minecraft:tnt", Count: 64b}]}'))
            else:
                editor.placeBlockGlobal(lbb + ivec3(2, 1, 1)
                                        , Block("minecraft:dispenser", {"facing": "up"}))

            editor.placeBlockGlobal(lbb + ivec3(2, 1, 0)
                                    , Block("minecraft:oak_button", {"facing": "north"}))
            editor.placeBlockGlobal(lbb + ivec3(2, 1, 2)
                                    , Block("minecraft:oak_button", {"facing": "south"}))