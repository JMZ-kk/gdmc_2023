from gdpc.old_lookup import ARTIFICIAL, LEAVES, VINES


TREE_LOGS = ('minecraft:acacia_log', 'minecraft:birch_log',
             'minecraft:dark_oak_log', 'minecraft:jungle_log',
             'minecraft:oak_log', 'minecraft:spruce_log')

MUSHROOM_BLOCKS = ('minecraft:mushroom_stem', 'minecraft:red_mushroom_block', 'minecraft:brown_mushroom_block')

RANDOM_SHIT_IN_TREES = ('minecraft:bee_nest', 'minecraft:beehive', 'minecraft:cocoa', 'minecraft:pumpkin')

TREE_BLOCKS = TREE_LOGS + LEAVES + MUSHROOM_BLOCKS + ('minecraft:bamboo', 'minecraft:snow',) + VINES + RANDOM_SHIT_IN_TREES

WATER_BLOCKS = ('minecraft:water','minecraft:ice')

MANMADE_BLOCKS = ('minecraft:birch_planks', 'minecraft:jungle_planks',
                  'minecraft:oak_planks', 'minecraft:acacia_planks',
                  'minecraft:dark_oak_planks', 'minecraft:spruce_planks',
                  'minecraft:crimson_planks', 'minecraft:warped_planks',
                  'minecraft:cut_sandstone', 'minecraft:smooth_sandstone',
                  'minecraft:hay_block' + 'minecraft:farmland') + ARTIFICIAL



