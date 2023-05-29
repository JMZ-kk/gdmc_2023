from Building import *
import random
from gdpc import __url__, Editor, Block, Box, lookup
import numpy as np
from glm import ivec2, ivec3
from gdpc.vector_tools import Vec3iLike, Rect, Box, addY, dropY

from gdpc.editor_tools import centerBuildAreaOnPlayer
from gdpc_6.gdpc.lookup import WOOD_TYPES
from BedStructure import *
from LeftBedStructure import *

class DormStructure(Building):
    def __init__(self):
        self.rightBed=BedStructure()
        self.leftBed=LeftBedStructure()
        self.wPadding=3
        self.lPadding=3
        self.height=8
        self.width=2*self.leftBed.size[0]+self.wPadding+5+2
        self.length=2*self.leftBed.size[2]+self.lPadding+2
        super().__init__((self.width, self.height, self.length))
    def build(self, editor, leftBackBottomPoint):
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 0, 0),
                              leftBackBottomPoint + ivec3(self.width-1, self.height-1, 0),Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 0, self.length-1),
                              leftBackBottomPoint + ivec3(self.width-1, self.height-1, self.length-1),Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 0, 1),
                              leftBackBottomPoint + ivec3(0, self.height-1, self.length-2),Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, self.height-1, 1),
                             leftBackBottomPoint + ivec3(self.width-1, self.height-1, self.length-2), Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(self.width-4, 0, 1),
                             leftBackBottomPoint + ivec3(self.width-4, self.height-5, self.length-2), Block("minecraft:white_concrete"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(self.width-4, self.height-4, 1),
                             leftBackBottomPoint + ivec3(self.width-4, self.height-2, self.length-2), Block("minecraft:glass"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(self.width-4, 1, 2),
                             leftBackBottomPoint + ivec3(self.width-4, 2, 3), Block("minecraft:glass"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(self.width-4, 1, 7),
                             leftBackBottomPoint + ivec3(self.width-4, 2, 8), Block("minecraft:glass"))


        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(self.width-1, 0, 1),
                             leftBackBottomPoint + ivec3(self.width-1, 0, self.length-2), Block("minecraft:dark_oak_fence"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(0, 0, 5), Block("minecraft:air"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.width - 4, 0, 5), Block("minecraft:air"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(0, 1, 5), Block("minecraft:air"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.width - 4, 1, 5), Block("minecraft:air"))


        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(4+self.leftBed.size[0]+self.lPadding, self.height - 2, 5), Block("minecraft:lantern",{"hanging":"true"}))

        geometry.placeCuboid(editor,leftBackBottomPoint + ivec3(3+self.leftBed.size[0]-1, 1, 0),leftBackBottomPoint + ivec3(3+self.leftBed.size[0]+1, self.height-2, 0),
                                Block("minecraft:glass"))
        geometry.placeCuboid(editor,leftBackBottomPoint + ivec3(3+self.leftBed.size[0]-1, 1, 10),leftBackBottomPoint + ivec3(3+self.leftBed.size[0]+1, self.height-2, 10),
                                Block("minecraft:glass"))

        # editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2+self.leftBed.size[0], 1, 0),
        #                         Block("minecraft:glass"))
        # editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2+self.leftBed.size[0], 1, 10),
        #                         Block("minecraft:glass"))

        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 0, 1),
                                Block("minecraft:dirt"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 0, 9),
                                Block("minecraft:dirt"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 1, 1),
                                Block("minecraft:allium"))

        geometry.placeCuboid(editor,leftBackBottomPoint + ivec3(0,1,1),leftBackBottomPoint + ivec3(0,2,3),Block("minecraft:glass"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 4, 1), leftBackBottomPoint + ivec3(0, 5, 3), Block("minecraft:glass"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 1, 7), leftBackBottomPoint + ivec3(0, 2, 9),
                             Block("minecraft:glass"))
        geometry.placeCuboid(editor, leftBackBottomPoint + ivec3(0, 4, 7), leftBackBottomPoint + ivec3(0, 5, 9),
                             Block("minecraft:glass"))
        editor.flushBuffer()
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(5,self.height-2,5),Block("minecraft:lantern",{"hanging":"true"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], self.height - 2, 2),
                                Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], self.height - 2, 5),
                                Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], self.height - 2, 8),
                                Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(2*self.wPadding +1 + 2*self.leftBed.size[0]+1, self.height - 2, 5),
                                Block("minecraft:lantern", {"hanging": "true"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 0, 2),
                                Block("minecraft:spruce_trapdoor",{"open":"true","facing":"south"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3 + self.leftBed.size[0]-1, 0, 1),
                                Block("minecraft:spruce_trapdoor", {"open": "true", "facing": "west"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3 + self.leftBed.size[0]+1, 0, 1),
                                Block("minecraft:spruce_trapdoor", {"open": "true", "facing": "east"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 1, 9),
                                Block("minecraft:cornflower"))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3+self.leftBed.size[0], 0, 8),
                                Block("minecraft:spruce_trapdoor",{"open":"true","facing":"north"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3 + self.leftBed.size[0]-1, 0, 9),
                                Block("minecraft:spruce_trapdoor", {"open": "true", "facing": "west"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(3 + self.leftBed.size[0]+1, 0, 9),
                                Block("minecraft:spruce_trapdoor", {"open": "true", "facing": "east"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(0,0,5),Block("minecraft:oak_door",{"hinge":"left"}))
        editor.placeBlockGlobal(leftBackBottomPoint + ivec3(self.width-4,0,5),Block("minecraft:oak_door",{"hinge":"left"}))


        basePoint=leftBackBottomPoint+ivec3(2,0,1)
        self.leftBed.build(editor,basePoint)
        self.rightBed.build(editor,basePoint+ivec3(0,0,6))
        self.leftBed.build(editor, basePoint+ivec3(self.leftBed.size[0]+self.wPadding,0,0))
        self.rightBed.build(editor, basePoint + ivec3(self.leftBed.size[0]+self.wPadding, 0, 6))
