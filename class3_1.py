from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
while count < 5:
    mc.postToChat("www")
    count = count + 1

    
