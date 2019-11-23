from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

stairBlock = 156
block = 155

height = 8

pos = mc.player.getTilePos()
xstart = pos.x + 2
y = pos.y
z = pos.z

for x in range(xstart, xstart+25,5):
    
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
    mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
    mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
    mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
    mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)

    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
    mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlock(x, y + 1, z - 1, stairBlock, 2)
    
    mc.setBlocks(x, y, z, x, y + height, z, block, 2)
    
    mc.postToChat("x = " + str(x))
    time.sleep(2)
