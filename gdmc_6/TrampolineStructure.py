from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class TrampolineStructure(Building):
    def __init__(self):
        super().__init__((5, 5, 7))
        self.kindOfWood = "minecraft:white_glazed_terracotta"

    def build(self, editor, lbb):
        geometry.placeCuboid(editor,lbb,lbb+ivec3(4,1,6),Block(self.kindOfWood))
        geometry.placeCuboid(editor,lbb+ivec3(1,0,2),lbb+ivec3(3,0,4),Block("minecraft:air"))
        # geometry.placeCuboid(editor,lbb+ivec3(0,1,1),lbb+ivec3(4,1,5),Block("minecraft:blue_glazed_terracotta"))
        editor.placeBlockGlobal(lbb + ivec3(2,0,2),Block("minecraft:sticky_piston",{"facing":"up"}))
        geometry.placeCuboid(editor, lbb + ivec3(1, 1, 2), lbb + ivec3(3, 1, 4), Block("minecraft:slime_block"))
        # editor.placeBlockGlobal(lbb + ivec3(2,3,0),Block("minecraft:stone"))
        # editor.placeBlockGlobal(lbb + ivec3(2, 3, 6), Block("minecraft:stone"))
        geometry.placeCuboid(editor,lbb+ivec3(1,2,0),lbb+ivec3(3,3,0),Block("minecraft:stone"))
        geometry.placeCuboid(editor, lbb + ivec3(1, 2, 6), lbb + ivec3(3, 3, 6), Block("minecraft:stone"))
        editor.placeBlockGlobal(lbb + ivec3(2, 3, 1), Block("minecraft:tripwire_hook",{"facing":"south"}))
        editor.placeBlockGlobal(lbb + ivec3(2, 3, 5), Block("minecraft:tripwire_hook"))
        editor.placeBlockGlobal(lbb+ivec3(2,2,0),Block("minecraft:redstone_wire"))
        editor.placeBlockGlobal(lbb + ivec3(2, 1, 1), Block("minecraft:redstone_wire"))
        geometry.placeCuboid(editor, lbb + ivec3(2, 3, 2), lbb + ivec3(2, 3, 4), Block("minecraft:tripwire"))
        editor.placeBlockGlobal(lbb, Block("minecraft:quartz_stairs",{"facing":"south"}))
        editor.placeBlockGlobal(lbb + ivec3(0, 1, 1), Block("minecraft:quartz_stairs",{"facing":"south"}))
        editor.placeBlockGlobal(lbb + ivec3(0, 1, 0), Block("minecraft:air"))