from Building import *
from glm import ivec3
from gdpc import geometry, Block
from EnchantingStructure import *


class EnchantingBuilding(Building):
    def __init__(self):
        self.kindOfWood = "minecraft:oak_planks"
        self.enchantingRoom = EnchantingStructure()
        self.clearable = False
        super().__init__((11, self.enchantingRoom.size[1] + 4, 11))

    def build(self, editor, lbb):
        lanternList = []
        geometry.placeCuboid(editor, lbb,
                             lbb + ivec3(self.enchantingRoom.size[0] + 1, self.enchantingRoom.size[1] + 3, 0),
                             Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb+ivec3(1,3,0),
                             lbb + ivec3(self.enchantingRoom.size[0], self.enchantingRoom.size[1] + 2, 0),
                             Block("minecraft:glass"))
        geometry.placeCuboid(editor, lbb,
                             lbb + ivec3(0, self.enchantingRoom.size[1] + 3, self.enchantingRoom.size[2] + 1),
                             Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb+ivec3(0,3,1),
                             lbb + ivec3(0, self.enchantingRoom.size[1] + 2, self.enchantingRoom.size[2]),
                             Block("minecraft:glass"))
        geometry.placeCuboid(editor, lbb + ivec3(self.enchantingRoom.size[0] + 1, 0, 0),
                             lbb + ivec3(self.enchantingRoom.size[0] + 1, self.enchantingRoom.size[1] + 3,
                                         self.enchantingRoom.size[2] + 1),
                             Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb + ivec3(self.enchantingRoom.size[0] + 1, 3, 1),
                             lbb + ivec3(self.enchantingRoom.size[0] + 1, self.enchantingRoom.size[1] + 2,
                                         self.enchantingRoom.size[2]),
                             Block("minecraft:glass"))
        geometry.placeCuboid(editor, lbb + ivec3(1, self.size[1] - 1, 1),
                             lbb + ivec3(self.enchantingRoom.size[0], self.size[1] - 1, self.enchantingRoom.size[2]+1),
                             Block("minecraft:glass"))

        lanternList.append(lbb + ivec3(2, self.size[1] - 2, 2))
        lanternList.append(lbb + ivec3(8, self.size[1] - 2, 2))
        lanternList.append(lbb + ivec3(2, self.size[1] - 2, 7))
        lanternList.append(lbb + ivec3(8, self.size[1] - 2, 7))
        editor.placeBlockGlobal(lanternList, Block("minecraft:lantern", {"hanging": "true"}))

        # geometry.placeCuboid(editor, lbb + ivec3(3, self.size[1] - 1, 3), lbb + ivec3(7, self.size[1] - 1, 6),
        #                      Block("minecraft:glass"))
        for x in range(self.enchantingRoom.size[2] + 2):
            geometry.placeLine(editor, lbb + ivec3(x + 1, self.enchantingRoom.size[1] - 1, 8),
                               lbb + ivec3(x + 1, 0, 10), Block("minecraft:oak_stairs"))
        self.enchantingRoom.build(editor, lbb + ivec3(1, 0, 1))
