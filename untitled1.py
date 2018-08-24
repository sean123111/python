# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:20:45 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def buildpramid(x,y,z,block,base):
    base = 18
    height = (base//2)+1
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        #y與y2相同
        z2 = z + base - i
        


        mc.setBlocks(x1+1, y1, z+1, x2-1, y1, z2-1, 24)
        if 1!=0 and i !=height-1:
            x,y,z = mc.player.getTilePos()
             buildpramid(x,y,z,103,)