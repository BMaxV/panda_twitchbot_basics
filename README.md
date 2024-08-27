# panda_twitchbot_basics

Ok. so.

twitchio uses asyncio mechanics to get messages from twitch chat.
for average shenanigans that's good enough.

panda3d is a 3d game engine, which can run in a async compatible,
BUT

the twitchio. ... bot.run() is blocking, so it's NOT possible to have a

```py
def main():
    my_object
    my_object.bot = twitchio.bot()
    my_object.game = panda3.game()
    while True:
        my_object.bot.main()
        my_object.game.main()
```

so to get commands from the bot to the game/3d thing/overlay I got recommended, because pyzmq allows sending between processes with sockets.

And that works.

the "other_zmq.py" is directly lifted from pyzmq's github and I reused their code to write this stuff.

now there are three parts in this repository that actually do stuff:

 * shading_webbuild_main is the pand3d thing that will open a test cube and switch texttures, either on click of the button, or upon receiving something from the zmq socket.
 * not_bot_sender is a standalone program that uses a zmq socket to periodically send something, so this is your twitchio-less verification script
 * twitch.py is the twitchio script that gets things from twitch chat.
 
What's missing here is the setup for the twitchio bot. You need a twitch account and a token for that to work and naturally, I have not included the token. ;) just make sure you plug that in, in the appropriate place.



