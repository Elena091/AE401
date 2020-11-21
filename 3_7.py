from mcpi.minecraft import Minecraft
mc =  Minecraft.create()

x,y,z, = mc.player.getTilePos()

weight = 50
height = 10
lenght = 50
mc.setBlock(x+1,y-1,z +1,x -1,y-1 ,z - 1,20)
mc.setBlock(x+1,y+1,z+1,weight-1,height-1,z+lenght-10, 0)
mc.player.setTilePos(x+2,z+2,y+2)
