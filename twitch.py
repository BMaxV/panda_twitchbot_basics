from twitchio.ext import commands

import asyncio

import asyncio
import time

import zmq
from zmq.asyncio import Context, Poller



with open("token.txt","r") as f:
    t=f.read()
    t=t.strip()
    token = t

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=token, prefix='!', initial_channels=['brucemalt'])
        
        
        url = 'tcp://127.0.0.1:5555'

        ctx = Context.instance()

        
        self.zmq_push_socket = ctx.socket(zmq.PUSH)
        self.zmq_push_socket.bind(url)
        
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    @commands.command(name="help")
    async def help(self, command_context):
        command_context.send("!hello - sends hello")
    
    @commands.command(name="switch")
    async def switch(self, command_context):
        
        self.zmq_push_socket.send_multipart(["switch".encode('ascii')])
        asyncio.sleep(1)
        
        #command_context.send("!hello - sends hello")
    
    
    @commands.command(name="hello")
    async def hello(self,command_context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await command_context.send(f'Hello {command_context.author.name}!')

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
