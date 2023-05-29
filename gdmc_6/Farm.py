from Building import *
from glm import ivec3
from gdpc import geometry, Block
from gdpc import __url__, Editor, Box, lookup
import random

class Farm(Building):
    def __init__(self):
        super().__init__((10,2,8))

    def build(self, editor, leftBackBottomPoint):
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint,
            leftBackBottomPoint + self.size - ivec3(1, 1, 1),
            Block("minecraft:white_concrete")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 0, 1),
            leftBackBottomPoint + self.size - ivec3(3, 2, 2),
            Block("minecraft:water")
        )
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 1, 2), Block("minecraft:water"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 1, self.size[2] - 3), Block("minecraft:water"))

        # editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 2, 2), Block("minecraft:glass"))
        # editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 2, self.size[2] - 3), Block("minecraft:glass"))
        geometry.placeCuboid(editor,leftBackBottomPoint + ivec3(0,2,0),leftBackBottomPoint + ivec3(2,2,self.size[2]-1),Block("minecraft:white_concrete"))

        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0] - 2, 0, 2), Block("minecraft:hopper", {"facing": "south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0] - 2, 0, self.size[2] - 3), Block("minecraft:hopper", {"facing": "north"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0] - 1, 1, 3),
                                Block("minecraft:oak_trapdoor", {"facing": "south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0] - 1, 1, self.size[2] - 4),
                                Block("minecraft:oak_trapdoor", {"facing": "north"}))
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(self.size[0] - 2, 0, 3),
            leftBackBottomPoint + ivec3(self.size[0] - 2, 0, self.size[2] - 4),
            Block("minecraft:hopper", {"facing": "east"})
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(self.size[0] - 1, 0, 3),
            leftBackBottomPoint + ivec3(self.size[0] - 1, 0, self.size[2] - 4),
            Block("minecraft:chest", {"facing": "east"})
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 1, 1),
            leftBackBottomPoint + ivec3(self.size[0] - 3, 1, 1),
            Block("minecraft:glass")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 1, self.size[2] - 2),
            leftBackBottomPoint + ivec3(self.size[0] - 3, 1, self.size[2] - 2),
            Block("minecraft:glass")
        )

        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 1, 1), Block("minecraft:air"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 1, self.size[2] - 2), Block("minecraft:air"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 1, 0),
                                Block("minecraft:sticky_piston", {"facing": "south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 1, self.size[2] - 1),
                                Block("minecraft:sticky_piston", {"facing": "north"}))
        editor.placeBlockGlobal(leftBackBottomPoint+ivec3(0,3,0),Block("minecraft:lantern"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(0, 3, self.size[2]-1), Block("minecraft:lantern"))

        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 1, 2),
            leftBackBottomPoint + self.size - ivec3(2, 1, 3),
            Block("minecraft:air")
        )

        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(2, 0, 2),
            leftBackBottomPoint + self.size - ivec3(3, 2, 3),
            Block("minecraft:farmland")
        )
        cropKind = random.choice(["minecraft:wheat", "minecraft:carrots", "minecraft:potatoes", "minecraft:beetroots"])
        if cropKind=="minecraft:beetroots":
            age="3"
        else:
            age="6"
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 1, 2),
            leftBackBottomPoint + self.size - ivec3(3, 1, 3),
            Block(cropKind,{"age":age})
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 2, 0),
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, 0),
            Block("minecraft:redstone_wire")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3, 2, self.size[2] - 1),
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, self.size[2] - 1),
            Block("minecraft:redstone_wire")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, 1),
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, 2),
            Block("minecraft:redstone_wire")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, self.size[2] - 3),
            leftBackBottomPoint + ivec3(self.size[0] - 1, 2, self.size[2] - 2),
            Block("minecraft:redstone_wire")
        )

        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0], 1, 2),
                                Block("minecraft:lever", {"facing": "east"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.size[0], 1, self.size[2] - 3),
                                Block("minecraft:lever", {"facing": "east"}))
