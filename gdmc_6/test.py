from typing import Optional, Iterable, Set, Tuple, Union
import random
from gdpc import __url__, Editor, Block, Box, lookup
import numpy as np
from glm import ivec2, ivec3
from gdpc.vector_tools import Vec3iLike, Rect, Box, addY, dropY

from gdpc.editor_tools import centerBuildAreaOnPlayer
from gdpc_6.gdpc.lookup import WOOD_TYPES
from BedStructure import *
from LeftBedStructure import *
from DormBuilding import *
from EnchantingBuilding import *
from TrampolineStructure import *
from MonumentStructure import *
from MonumentBuilding import *
from MeetingBuilding import *
from CannonStructure import *
from ZCannonStructure import *
from Farm import *
from MunitionsFactory import *
from StreetLight import *
from SteveStatue import *
from EndermanStatue import *
from VillageStructure import *
from Shop import *
import time

editor = Editor(buffering=True)

a=[1,2,3,4]
b=[5]
b.extend(a)
print(b)
# a=EndermanStatue()
# a.build(editor, ivec3(2309,68,232))