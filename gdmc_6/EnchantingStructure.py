from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class EnchantingStructure(Building):
    def __init__(self):
        super().__init__((9, 3, 7))
        self.kindOfWood = "minecraft:oak_planks"

    def build(self, editor, lbb):
        geometry.placeCuboid(editor,lbb,lbb+self.size-ivec3(1,1,1),Block(self.kindOfWood))
        woodList = []
        stickList = []
        redWireList = []
        northRepeaterList=[]
        southRepeaterList = []
        bookshelfLsit=[]
        for z in range(1, 4):
            for x in range(2):
                woodList.append(lbb+(x, 0, z))
            for x in range(7, 9):
                woodList.append(lbb+(x, 0, z))

        for x in range(2, 7):
            woodList.append(lbb+(x, 0, 0))
            woodList.append(lbb+(x, 0, 4))
            stickList.append(lbb+(x, 1, 0))
            bookshelfLsit.append(lbb+(x, 2, 0))
        for z in range(1, 5):
            stickList.append(lbb+(2, 1, z))
            stickList.append(lbb+(6, 1, z))
            bookshelfLsit.append(lbb + (2, 2, z))
            bookshelfLsit.append(lbb + (6, 2, z))
        stickList.append(lbb+(3, 1, 4))
        stickList.append(lbb+(5, 1, 4))
        bookshelfLsit.append(lbb + (3, 2, 4))
        bookshelfLsit.append(lbb + (5, 2, 4))
        woodList.append(lbb+(4, 0, 5))
        woodList.append(lbb+(4, 2, 5))
        redWireList.append((lbb+(4, 1, 5)))
        redWireList.append((lbb + (4, 1, 4)))
        redWireList.append((lbb + (4, 0, 3)))
        redWireList.append((lbb + (1, 1, 2)))
        redWireList.append((lbb + (7, 1, 2)))
        for z in range(1, 4):
            redWireList.append(lbb+(0, 1, z))
            redWireList.append(lbb+(8, 1, z))
        for x in range(2,7):
            redWireList.append(lbb+(x,0,2))
            southRepeaterList.append(lbb+(x,0,1))
            northRepeaterList.append(lbb + (x, 0, 3))

        editor.placeBlockGlobal(woodList, Block(self.kindOfWood))
        editor.placeBlockGlobal(stickList, Block("minecraft:sticky_piston",{"facing":"up"}))
        editor.placeBlockGlobal(northRepeaterList,Block("minecraft:repeater",{"facing":"north"}))
        editor.placeBlockGlobal(southRepeaterList, Block("minecraft:repeater", {"facing": "south"}))
        editor.placeBlockGlobal(redWireList, Block("minecraft:redstone_wire"))
        editor.placeBlockGlobal(bookshelfLsit,Block("minecraft:bookshelf"))

        editor.placeBlockGlobal(lbb + (4, 3, 5), Block("minecraft:stone_pressure_plate"))
        editor.placeBlockGlobal(lbb + (1, 1, 1), Block("minecraft:repeater",{"facing":"west"}))
        editor.placeBlockGlobal(lbb + (1, 1, 3), Block("minecraft:repeater", {"facing": "west"}))
        editor.placeBlockGlobal(lbb + (7, 1, 1), Block("minecraft:repeater",{"facing":"east"}))
        editor.placeBlockGlobal(lbb + (7, 1, 3), Block("minecraft:repeater", {"facing": "east"}))
        editor.placeBlockGlobal(lbb + (4,1,3),Block("minecraft:air"))
        editor.placeBlockGlobal(lbb + (4,3,2),Block("minecraft:enchanting_table"))