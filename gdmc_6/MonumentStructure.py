from Building import *
from glm import ivec3
from gdpc import geometry, Block
import random


class MonumentStructure(Building):
    def __init__(self):
        super().__init__((7, 37, 7))
        self.kindOfWood = "minecraft:stone"
        self.G = [(1, 1), (2, 1), (3, 1), (4, 1), (1, 2), (1, 3), (1, 6), (2, 3), (2, 7), (3, 7), (4, 7), (5, 2),
                  (5, 3), (5, 4), (5, 5), (5, 6)]
        self.D = [(2, 1), (3, 1), (4, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 7), (3, 7), (4, 7), (5, 2),
                  (5, 3), (5, 4), (5, 5), (5, 1), (5, 6), (5, 7)]
        self.C = [(2, 1), (3, 1), (4, 1), (1, 2), (1, 6), (2, 7), (3, 7), (4, 7), (5, 2), (5, 3),
                  (5, 4), (5, 5), (5, 6)]
        self.M = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
                  (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (2, 7), (4, 7)]

        self.G_r = [(5, 1), (4, 1), (3, 1), (2, 1), (5, 2), (5, 3), (5, 6), (4, 3), (4, 7), (3, 7), (2, 7), (1, 2),
                    (1, 3), (1, 4), (1, 5), (1, 6)]
        self.D_r = [(2, 1), (3, 1), (4, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 7), (3, 7), (4, 7), (5, 2), (5, 3),
                    (5, 4), (5, 5), (5, 6), (1, 1), (1, 6), (1, 7)]
        self.C_r = [(2, 1), (3, 1), (4, 1), (5, 2), (5, 6), (2, 7), (3, 7), (4, 7), (1, 2), (1, 3),
                    (1, 4), (1, 5), (1, 6)]
        self.Two = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (2, 2), (3, 3), (4, 4), (5, 5), (5, 6), (1, 6), (2, 7),
                    (3, 7), (4, 7)]
        self.Two_r = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (5, 6), (1, 6), (2, 7),
                    (3, 7), (4, 7)]
        self.Zero = [(2, 1), (3, 1), (4, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 7), (3, 7), (4, 7), (5, 2),
                     (5, 3), (5, 4), (5, 5), (5, 6)]
        self.Three = [(1,2),(1,3),(2, 1), (3, 1), (4, 1), (1, 5), (1, 6), (2, 7), (3, 7), (4, 7), (5, 2),
                    (5, 3), (5, 5), (5, 6),(3,4),(4,4)]
        self.Three_r = [(1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (1, 5), (1, 6), (2, 7), (3, 7), (4, 7), (5, 2),
                      (5, 3), (5, 5), (5, 6), (3, 4), (2, 4)]

    def transform(self, lbb, a, axis='x'):
        res = []
        if axis == 'x':
            for i in range(len(a)):
                res.append(lbb + ivec3(a[i][0], a[i][1], 0))
        else:
            for i in range(len(a)):
                res.append(lbb + ivec3(0, a[i][1], a[i][0]))
        return res

    def build(self, editor, lbb):
        geometry.placeCuboid(editor, lbb, lbb + self.size - ivec3(1, 4, 1), Block(self.kindOfWood))
        geometry.placeCuboid(editor,lbb + ivec3(1, self.size[1]-3, 1),lbb + self.size - ivec3(2, 3, 2), Block(self.kindOfWood))
        geometry.placeCuboid(editor, lbb + ivec3(1, self.size[1] - 2, 1), lbb + self.size - ivec3(2, 2, 2),
                             Block("minecraft:campfire"))
        glowList = []
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 12, 0), self.G))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 12, self.size[2] - 1), self.G_r))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 12, 0), self.Two, axis='z'))
        glowList.extend(self.transform(lbb + ivec3(self.size[0] - 1, self.size[1] - 12, 0), self.Two_r, axis='z'))

        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 20, 0), self.D))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 20, self.size[2] - 1), self.D_r))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 20, 0), self.Zero, axis='z'))
        glowList.extend(self.transform(lbb + ivec3(self.size[0] - 1, self.size[1] - 20, 0), self.Zero, axis='z'))

        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 28, 0), self.M))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 28, self.size[2] - 1), self.M))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 28, 0), self.Two, axis='z'))
        glowList.extend(self.transform(lbb + ivec3(self.size[0] - 1, self.size[1] - 28, 0), self.Two_r, axis='z'))

        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 36, 0), self.C))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 36, self.size[2] - 1), self.C_r))
        glowList.extend(self.transform(lbb + ivec3(0, self.size[1] - 36, 0), self.Three, axis='z'))
        glowList.extend(self.transform(lbb + ivec3(self.size[0] - 1, self.size[1] - 36, 0), self.Three_r, axis='z'))

        editor.placeBlockGlobal(glowList, Block("minecraft:glowstone"))
