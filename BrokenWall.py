from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()

xStart= pos.x
yStart = pos.y
z = pos.z

brokenWall = []
height, width = 5, 10

for i in range(height):
    y = yStart + i

    for j in range(width):
        x = xStart + j
        brokenBlocks = [48, 67, 4, 4, 4]
        block = random.choice(brokenBlocks)

        mc.setBlock(x,y,z,block)
