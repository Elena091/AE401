from mcpi.minecraft import Minecraft


mc =  Minecraft.create()

x,y,z = mc.player.getTailPos()

w=100
h=10
l=50


mc.setBlocks(x100,y10,z50)
mc.setBlocks(x+100,y+10,z+50)
