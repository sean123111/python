# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:23:14 2018

@author: NTPU
"""
inport random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = sean.player.gettilepos()
for i in range(20):
    r=randrange(1,5)
    c=randrange(1,16)
    l=randrange(1,13)
    if r==1:
        x,y,z = sean.setblocks(x,y,z,x+4,y,z,35,c)
        x = x-l
   elif r==2:
        x,y,z = sean.setblocks(x,y,z,x+4,y,z,35,c)
        x = x-l
    elif r==3:
         x,y,z = sean.setblocks(x,y,z,x+4,y,z,35,c)
        x = x-l
    elif r==4:
        x,y,z = sean.setblocks(x,y,z,x+4,y,z,35,c)
        x = x-l
    elif r==4:
        x,y,z = sean.setblocks(x,y+1,z,x+4,y,z,35,c)
        x = x-l
    elif r==4:
         x,y,z = sean.setblocks(x,y+1,z,x+4,y,z,35,c)
        x = x-l