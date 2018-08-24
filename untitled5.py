# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:13:06 2018

@author: NTPU
"""
inport random
from mcpi.minecraft import Minecraft
sean = Minecraft.create()

x,y,z = sean.player.gettilepos()

for i in range(10):
    x,y,z = sean.player.gettilepos()
    x=x+j
    r = randrange(0,16)
    sean.setblock(x,y,z,35,r)
    z=z+1
    r=randrange(0.16)
    while true:
        hits = sean.events.pollblockhits()
        if len(hits)>0:
            h = hits[0]
            
            block = sean.getblockwithdata(h.pos)
            data = block data
            
            if data==r:
                sean.posttochat("you have found it")
                sean.setblock(h.pos,57)
                break
            elif data>r:
                sean.posttochat("find smaller")
            elif data<r:
                sean.posttochat("find bigger")