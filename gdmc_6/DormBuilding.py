from Building import *
import random
from gdpc import __url__, Editor, Block, Box, lookup
import numpy as np
from glm import ivec2, ivec3
from gdpc.vector_tools import Vec3iLike, Rect, Box, addY, dropY

from gdpc.editor_tools import centerBuildAreaOnPlayer
from gdpc_6.gdpc.lookup import WOOD_TYPES
from DormStructure import *
from SwimmingPoolStructure import *
from Farm import *


class DormBuilding(Building):
    def __init__(self):
        self.dorm = DormStructure()
        self.swimmingPool = SwimmingPoolStructure()
        self.farm = Farm()
        self.hp = 2
        self.clearable = False
        super().__init__((self.dorm.size[0] + 3, self.dorm.size[1] + self.hp, self.dorm.size[2] + 6))

    def build(self, editor, lbb):
        geometry.placeCuboid(editor, lbb,
                             lbb + ivec3(self.size[0] - 1, self.hp - 1, self.size[2] - 1),
                             Block("minecraft:white_concrete"))
        self.dorm.build(editor, lbb + ivec3(3, self.hp, 0))
        self.dorm.build(editor, lbb + ivec3(3, self.hp + self.dorm.size[1], 0))
        geometry.placeCuboid(editor, lbb + ivec3(0, self.hp + self.dorm.size[1] - 1, 11),
                             lbb + ivec3(3 + self.dorm.size[1], self.hp + self.dorm.size[1] - 1, 13),
                             Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb + ivec3(0, 1, 0), lbb + ivec3(2, self.hp - 1, self.hp - 2),
                             Block("minecraft:air"))
        geometry.placeCuboid(editor, lbb + ivec3(0, self.hp + self.dorm.size[1] - 1, 0),
                             lbb + ivec3(2, self.hp + self.dorm.size[1] - 1, 16), Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb + ivec3(0, self.hp + 2 * self.dorm.size[1] - 1, 0),
                             lbb + ivec3(2, self.hp + 2 * self.dorm.size[1] - 1, 10), Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb + ivec3(4 + self.dorm.size[1], self.hp - 1 + self.dorm.size[1], 11)
                             , lbb + ivec3(6 + self.dorm.size[1], self.hp - 1 + self.dorm.size[1], 16),
                             Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, lbb + ivec3(3 + self.dorm.size[1], self.hp - 1 + 2 * self.dorm.size[1], 11)
                             , lbb + ivec3(6 + self.dorm.size[1], self.hp - 1 + 2 * self.dorm.size[1], 16),
                             Block("minecraft:white_concrete"))
        self.swimmingPool.build(editor, lbb + ivec3(14, self.hp + 2 * self.dorm.size[1], 2))
        self.farm.build(editor, lbb + ivec3(1, self.hp + 2 * self.dorm.size[1], 2))

        editor.flushBuffer()
        editor.placeBlockGlobal(
            lbb + ivec3(1, 8, 2),
            Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(
            lbb + ivec3(1, 8, 8),
            Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(
            lbb + ivec3(1, 8, 14),
            Block("minecraft:lantern", {"hanging": "true"}))

        editor.placeBlockGlobal(
            lbb + ivec3(6, 8, 12),
            Block("minecraft:lantern", {"hanging": "true"}))

        editor.placeBlockGlobal(
            lbb + ivec3(12, 8, 12),
            Block("minecraft:lantern", {"hanging": "true"}))

        editor.placeBlockGlobal(
            lbb + ivec3(12, 8 + self.dorm.size[1], 12),
            Block("minecraft:lantern", {"hanging": "true"}))

        editor.placeBlockGlobal(
            lbb + ivec3(1, 8 + self.dorm.size[1], 2),
            Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(
            lbb + ivec3(1, 8 + self.dorm.size[1], 8),
            Block("minecraft:lantern", {"hanging": "true"}))

        for i in range(3):
            geometry.placeLine(editor, lbb + ivec3(i, 0, 0), lbb + ivec3(i, self.hp - 1, self.hp - 1),
                               Block("minecraft:quartz_stairs", {"facing": "south"}))
            geometry.placeLine(editor, lbb + ivec3(3, self.hp, 14 + i),
                               lbb + ivec3(2 + self.dorm.size[1], self.hp - 1 + self.dorm.size[1], 14 + i)
                               , Block("minecraft:quartz_stairs", {"facing": "east"}))
            geometry.placeLine(editor, lbb + ivec3(4, self.hp, 14 + i),
                               lbb + ivec3(3 + self.dorm.size[1], self.hp - 1 + self.dorm.size[1], 14 + i)
                               , Block("minecraft:white_concrete"))
            geometry.placeLine(editor, lbb + ivec3(3, self.hp + self.dorm.size[1], 14 + i),
                               lbb + ivec3(2 + self.dorm.size[1], self.hp - 1 + 2 * self.dorm.size[1], 14 + i)
                               , Block("minecraft:quartz_stairs", {"facing": "east"}))
            geometry.placeLine(editor, lbb + ivec3(3, self.hp + self.dorm.size[1] - 1, 14 + i),
                               lbb + ivec3(2 + self.dorm.size[1], self.hp - 2 + 2 * self.dorm.size[1], 14 + i)
                               , Block("minecraft:white_concrete"))
