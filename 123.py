from mcpi.minecraft import Minecraft
mc =  Minecraft.create()

x,y,z, = mc.player.getTilePos()

mc.setSign(x,y,z,68,0,"123","456"," ","789")
