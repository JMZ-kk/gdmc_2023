from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class SteveStatue(Building):
    def __init__(self):
        super().__init__((7, 11, 5))
        self.name='steve'

    def build(self, editor, lbb):
        editor.placeBlockGlobal(lbb + ivec3(1, 0, 1), Block('minecraft:gray_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 0, 1), Block('minecraft:gray_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 1, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 1, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 2, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 2, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 3, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 3, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 3, 1), Block('minecraft:blue_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 4, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 4, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 4, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 5, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 5, 2), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 5, 3), Block('minecraft:brown_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 5, 4), Block('minecraft:brown_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 5, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 5, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 5, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(4, 5, 1), Block('minecraft:cyan_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(5, 6, 1), Block('minecraft:brown_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(6, 7, 1), Block('minecraft:brown_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(6, 8, 1), Block('minecraft:oak_fence'))
        editor.placeBlockGlobal(lbb + ivec3(6, 9, 1), Block('minecraft:oak_planks'))
        editor.placeBlockGlobal(lbb + ivec3(6, 10, 1), Block('minecraft:campfire'))
        editor.placeBlockGlobal(lbb + ivec3(0, 6, 4), Block('minecraft:oak_fence'))
        editor.placeBlockGlobal(lbb + ivec3(0, 7, 4), Block('minecraft:oak_planks'))
        editor.placeBlockGlobal(lbb + ivec3(0, 8, 4), Block('minecraft:campfire'))
        editor.placeBlockGlobal(lbb + ivec3(1, 7, 2), Block('minecraft:white_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 7, 2), Block('minecraft:white_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 7, 2), Block('minecraft:brown_concrete'))
        geometry.placeCuboid(editor,lbb + ivec3(1,6,0),lbb + ivec3(3,6,2), Block('minecraft:brown_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 8, 0), lbb + ivec3(3, 8, 2), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 7, 0), lbb + ivec3(3, 7, 0), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 7, 1), lbb + ivec3(3, 7, 1), Block('minecraft:brown_concrete'))