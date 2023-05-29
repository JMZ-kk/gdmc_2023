from Building import *
from glm import ivec3
from gdpc import geometry, Block
from MonumentStructure import *
import random


class MonumentBuilding(Building):
    def __init__(self):
        super().__init__((25, 40, 25))
        self.kindOfWood = "minecraft:stone"
        self.body=MonumentStructure()
        self.clearable=False

    def buildAltar(self, editor, lbb):
        geometry.placeCuboid(editor,lbb,lbb+ivec3(4,4,4),Block("minecraft:stone"))
        geometry.placeCuboid(editor, lbb+ivec3(0,5,0), lbb + ivec3(4, 5, 4), Block("minecraft:stone_brick_wall"))
        geometry.placeCuboid(editor, lbb+ivec3(1,6,1), lbb + ivec3(3, 6, 3), Block("minecraft:campfire"))


    def build(self, editor, lbb):
        geometry.placeCuboid(editor, lbb, lbb + ivec3(self.size[0]-1,3,self.size[2]-1), Block(self.kindOfWood))
        self.body.build(editor,lbb+ivec3(9,4,9))
        self.buildAltar(editor,lbb+ivec3(1,4,1))
        self.buildAltar(editor, lbb + ivec3(self.size[0]-6, 4, 1))
        self.buildAltar(editor, lbb + ivec3(1, 4, self.size[2]-6))
        self.buildAltar(editor, lbb + ivec3(self.size[0]-6, 4, self.size[2] - 6))
        airList=[]
        northStairs=[]
        southStairs=[]
        eastStairs=[]
        westStairs=[]
        for i in range(9,16):
            airList.append(lbb+ivec3(0,3,i))
            airList.append(lbb + ivec3(self.size[0]-1, 3, i))
            airList.append(lbb + ivec3(i, 3, 0))
            airList.append(lbb + ivec3(i, 3, self.size[2]-1))

            airList.append(lbb + ivec3(1, 3, i))
            airList.append(lbb + ivec3(self.size[0] - 2, 3, i))
            airList.append(lbb + ivec3(i, 3, 1))
            airList.append(lbb + ivec3(i, 3, self.size[2] - 2))

            airList.append(lbb + ivec3(0, 2, i))
            airList.append(lbb + ivec3(self.size[0] - 1, 2, i))
            airList.append(lbb + ivec3(i, 2, 0))
            airList.append(lbb + ivec3(i, 2, self.size[2] - 1))

            airList.append(lbb + ivec3(0, 1, i))
            airList.append(lbb + ivec3(self.size[0] - 1, 1, i))
            airList.append(lbb + ivec3(i, 1, 0))
            airList.append(lbb + ivec3(i, 1, self.size[2] - 1))

            airList.append(lbb + ivec3(1, 2, i))
            airList.append(lbb + ivec3(self.size[0] - 2, 2, i))
            airList.append(lbb + ivec3(i, 2, 1))
            airList.append(lbb + ivec3(i, 2, self.size[2] - 2))

            airList.append(lbb + ivec3(2, 3, i))
            airList.append(lbb + ivec3(self.size[0] - 3, 3, i))
            airList.append(lbb + ivec3(i, 3, 2))
            airList.append(lbb + ivec3(i, 3, self.size[2] - 3))

            eastStairs.append(lbb + ivec3(0, 0, i))
            westStairs.append(lbb + ivec3(self.size[0] - 1, 0, i))
            southStairs.append(lbb + ivec3(i, 0, 0))
            northStairs.append(lbb + ivec3(i, 0, self.size[2] - 1))

            eastStairs.append(lbb + ivec3(1, 1, i))
            westStairs.append(lbb + ivec3(self.size[0] - 2, 1, i))
            southStairs.append(lbb + ivec3(i, 1, 1))
            northStairs.append(lbb + ivec3(i, 1, self.size[2] - 2))

            eastStairs.append(lbb + ivec3(2, 2, i))
            westStairs.append(lbb + ivec3(self.size[0] - 3, 2, i))
            southStairs.append(lbb + ivec3(i, 2, 2))
            northStairs.append(lbb + ivec3(i, 2, self.size[2] - 3))

            eastStairs.append(lbb + ivec3(3, 3, i))
            westStairs.append(lbb + ivec3(self.size[0] - 4, 3, i))
            southStairs.append(lbb + ivec3(i, 3, 3))
            northStairs.append(lbb + ivec3(i, 3, self.size[2] - 4))


        editor.placeBlockGlobal(airList,Block("minecraft:air"))
        editor.placeBlockGlobal(northStairs,Block("stone_stairs",{"facing":"north"}))
        editor.placeBlockGlobal(southStairs, Block("stone_stairs", {"facing": "south"}))
        editor.placeBlockGlobal(eastStairs, Block("stone_stairs", {"facing": "east"}))
        editor.placeBlockGlobal(westStairs, Block("stone_stairs", {"facing": "west"}))