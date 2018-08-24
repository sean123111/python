# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:21:19 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
sean = Minecraft.create()


number = 1
x,y,z = sean.player.gettilepos()

for i in range(number):
    sean.spawnentity(x,y,z,60)
number = number * 2
sean.posttochat("you have made"+str(number)+"fish")