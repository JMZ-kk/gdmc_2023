from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class StreetLight(Building):
    def __init__(self,simple=False):
        super().__init__((5, 6, 5))
        self.simple=simple
        self.name='light'

    def build(self, editor, lbb):
        if not self.simple:
            geometry.placeCuboid(editor,lbb,lbb+self.size-ivec3(1,1,1),Block('minecraft:air'))
            editor.placeBlockGlobal(lbb+ivec3(0, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(2, 4, 0), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(4, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(2, 4, 4), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(1, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(2, 4, 1), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(3, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(2, 4, 3), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb+ivec3(2, 4, 2), Block('minecraft:oak_planks'))
            editor.placeBlockGlobal(lbb+ivec3(2, 5, 2), Block('minecraft:campfire'))
            editor.placeBlockGlobal(lbb+ivec3(2, -1, 2), Block('minecraft:dirt'))

            editor.flushBuffer()
            editor.placeBlockGlobal(lbb+ivec3(0, 3, 2), Block('minecraft:lantern', {'hanging': 'true'}))
            editor.placeBlockGlobal(lbb+ivec3(2, 3, 0), Block('minecraft:lantern', {'hanging': 'true'}))
            editor.placeBlockGlobal(lbb+ivec3(4, 3, 2), Block('minecraft:lantern', {'hanging': 'true'}))
            editor.placeBlockGlobal(lbb+ivec3(2, 3, 4), Block('minecraft:lantern', {'hanging': 'true'}))
            geometry.placeLine(editor,lbb+ivec3(2,0,2),lbb+ivec3(2,3,2),Block('minecraft:oak_fence'))
        else:
            geometry.placeCuboid(editor, lbb, lbb + self.size - ivec3(1, 1, 1), Block('minecraft:air'))
            editor.placeBlockGlobal(lbb + ivec3(1, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb + ivec3(2, 4, 1), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb + ivec3(3, 4, 2), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb + ivec3(2, 4, 3), Block('minecraft:oak_fence'))
            editor.placeBlockGlobal(lbb + ivec3(2, 4, 2), Block('minecraft:oak_planks'))
            editor.placeBlockGlobal(lbb + ivec3(2, 5, 2), Block('minecraft:campfire'))

            editor.flushBuffer()
            geometry.placeLine(editor, lbb + ivec3(2, 0, 2), lbb + ivec3(2, 3, 2), Block('minecraft:oak_fence'))



