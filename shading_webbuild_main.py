#import pygbag.aio as asyncio
import asyncio
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader
from panda3d.core import LVector3
from direct.gui.DirectButton import DirectButton
from direct.gui import DirectGuiGlobals as DGG

import panda3d.core
panda3d.core.loadPrcFileData("", "default-model-extension .egg")


import asyncio
import time

import zmq
from zmq.asyncio import Context, Poller




class Wrapper:

    # I should definitely
    # use the system built in drag main to do this.
    # pretty sure anyway.

    def __init__(self):
        self.b = ShowBase()
        print(self.b)
        #self.b.enableParticles()
        print(self.b)
        self.ob=load_object(self.b)
        print(self.b, self.ob)

        self.selected_text="ground.jpg"


        b=create_button("switch me",(0,0,-0.5),0.05,self.set_tex2,tuple())

        tex1=loader.loadTexture('testgrid.png')
        tex2=loader.loadTexture('ground.jpg')
        tex3=loader.loadTexture('bunny.png')

        tex1 = loader.loadTexture('testgrid.png')
        self.ob.setShaderInput("mytexture1", tex1)
        self.ob.setShaderInput("mytexture2", tex2)
        self.ob.setShaderInput("bunnytex", tex3)

        shader = Shader.load(Shader.SL_GLSL,
                     vertex="03myshader.vert",
                     fragment="03myshader.frag")
        self.ob.setShader(shader)

        self.t=0

    def set_tex2(self,*args):

        if self.selected_text=="ground.jpg":
            tex2=loader.loadTexture("sand.png")
            self.ob.setShaderInput("mytexture2", tex2)
            self.selected_text="sand.png"

        else:
            tex2=loader.loadTexture('ground.jpg')
            self.ob.setShaderInput("mytexture2", tex2)
            self.selected_text="ground.jpg"

    def main(self,delta_t):
        self.t+=delta_t
        self.ob.setHpr((self.t*5,0,0))


def create_button(text,position,scale,function, arguments,text_may_change=0,frame_size=(-4.5,4.5,-0.75,0.75)):
    
    position=LVector3(*position)
    button = DirectButton(text=text,
                    pos=position,
                    scale=scale,
                    frameSize=frame_size,
                    textMayChange=text_may_change)#(.9, 0, .75), text="Open"))
                                   #scale=.1, pad=(.2, .2),
                                   #rolloverSound=None, clickSound=None,
                                   #command=self.toggleusicBox)
    #position[0]+=0.1
    
    button.setPos(*position)
    
    if function!=None and arguments!=None:
        arguments=list(arguments)
        button.bind(DGG.B1PRESS,function,arguments)
        
    return button

def load_object(showbase,name="cube",path="./",pos=(0,20,0),scale=(1,1,1)):
    name=path+name
    try:
        ob = showbase.loader.loadModel(name)
    except OSError as e:
        print("my error",e)
        #wait that probably should be in the create load function
        #can't find the file
        return None

    ob.setPos(*pos)
    ob.reparentTo(showbase.render)
    ob.setScale(*scale)
    ob.setTwoSided(True)

    return ob

async def main():
    W = Wrapper()
    #W.main = GameMain()
    
    url = 'tcp://127.0.0.1:5555'

    ctx = Context.instance()
    
    pull = ctx.socket(zmq.PULL)
    pull.connect(url)
    poller = Poller()
    poller.register(pull, zmq.POLLIN)
    
    while True:
        
        #events = await poller.poll()
        #if pull in dict(events):
            #print("recving", events)
        msg = None
        try:
            msg = await pull.recv_multipart(flags=zmq.NOBLOCK)
            print('recvd', msg)
        except:
            pass
        if msg != None:
            W.set_tex2()
        delta_t = globalClock.dt
        W.b.taskMgr.step()
        W.main(delta_t)
        await asyncio.sleep(0)



if __name__=="__main__":
    asyncio.run( main() )
