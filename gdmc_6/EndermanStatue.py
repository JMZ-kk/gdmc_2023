from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class EndermanStatue(Building):
    def __init__(self):
        super().__init__((5, 9, 5))
        self.name='enderman'

    def build(self, editor, lbb):
        editor.placeBlockGlobal(lbb + ivec3(1, 0, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 0, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 1, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 1, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 2, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 2, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 3, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 3, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 3, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(1, 4, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 4, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 4, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 5, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 4, 2), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(0, 3, 3), Block('minecraft:black_concrete'))

        geometry.placeCuboid(editor, lbb + ivec3(1,2,2), lbb + ivec3(3,4,4), Block('minecraft:glowstone'))

        editor.placeBlockGlobal(lbb + ivec3(4, 5, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(4, 4, 2), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(4, 3, 3), Block('minecraft:black_concrete'))


        editor.placeBlockGlobal(lbb + ivec3(1, 5, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 5, 1), Block('minecraft:black_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 5, 1), Block('minecraft:black_concrete'))

        editor.placeBlockGlobal(lbb + ivec3(1, 7, 2), Block('minecraft:purple_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(3, 7, 2), Block('minecraft:purple_concrete'))
        editor.placeBlockGlobal(lbb + ivec3(2, 7, 2), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor,lbb + ivec3(1,6,0),lbb + ivec3(3,6,2), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 8, 0), lbb + ivec3(3, 8, 2), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 7, 0), lbb + ivec3(3, 7, 0), Block('minecraft:black_concrete'))
        geometry.placeCuboid(editor, lbb + ivec3(1, 7, 1), lbb + ivec3(3, 7, 1), Block('minecraft:black_concrete'))