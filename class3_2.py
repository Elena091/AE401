from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

count = 0

while count < 1000:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("Position: " + str(x) + "," + ","+ str(z))

    count = count + 1
    time.sleep(5)
