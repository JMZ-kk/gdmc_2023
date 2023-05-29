from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class LeftBedStructure(Building):
    def __init__(self):
        super().__init__((8,7,3))
        self.kindOfWood = "minecraft:birch_planks"

    def build(self, editor, leftBackBottomPoint):
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint,  # Corner 1
            leftBackBottomPoint + ivec3(7,6,2),  # Corner 2
            Block(self.kindOfWood)
        )
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 0, 2), Block("minecraft:chest"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 1, 2), Block("minecraft:oak_slab",{"type":"top"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 2, 2), Block("minecraft:chest"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 3, 2), Block("minecraft:air"))
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3,0,2),  # Corner 1
            leftBackBottomPoint + ivec3(5,2,1),  # Corner 2
            Block("minecraft:air")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3,4,2),  # Corner 1
            leftBackBottomPoint + ivec3(7,5,1),  # Corner 2
            Block("minecraft:air")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3,4,2),  # Corner 1
            leftBackBottomPoint + ivec3(5,4,1),  # Corner 2
            Block("minecraft:air")
        )
        geometry.placeCuboid(
            editor,
            leftBackBottomPoint + ivec3(3,2,0),  # Corner 1
            leftBackBottomPoint + ivec3(5,2,0),  # Corner 2
            Block("minecraft:bookshelf")
        )
        geometry.placeCuboid(editor,
            leftBackBottomPoint + ivec3(3,4,2),  # Corner 1
            leftBackBottomPoint + ivec3(5,4,2),  # Corner 2
            Block("minecraft:dark_oak_fence"))
        geometry.placeCuboid(editor,
            leftBackBottomPoint + ivec3(7,4,2),  # Corner 1
            leftBackBottomPoint + ivec3(7,4,1),  # Corner 2
            Block("minecraft:dark_oak_fence"))
        geometry.placeCuboid(editor,
            leftBackBottomPoint + ivec3(6,0,3),  # Corner 1
            leftBackBottomPoint + ivec3(6,3,3),  # Corner 2
            Block("minecraft:ladder",{"facing":"south"}))
        geometry.placeCuboid(editor,
                             leftBackBottomPoint + ivec3(1, 6, 0),  # Corner 1
                             leftBackBottomPoint + ivec3(3, 6, 0),  # Corner 2
                             Block("minecraft:redstone_wire"))
        editor.flushBuffer()
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(5,4,1), Block("minecraft:white_bed",{"facing":"west"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 5, 1), Block("minecraft:redstone_lamp"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 5, 1), Block("minecraft:glass"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3, 5, 1), Block("minecraft:lever",{"facing":"south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(1, 6, 1), Block("minecraft:redstone_wire"))

        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(4, 0, 2), Block("minecraft:spruce_stairs",{"facing":"south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(4,0,1), Block("minecraft:dark_oak_fence"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(4, 1, 1), Block("minecraft:yellow_carpet"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2, 1, 1), Block("minecraft:redstone_lamp"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3, 1, 2), Block("minecraft:lever",{"facing":"east"}))
