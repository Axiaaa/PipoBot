from interactions import *
from random import randint
import asyncio


class Presence(Extension): 

    @listen()
    async def on_startup(self):
        while True:
                random_activity = randint(1, 2)
                if random_activity == 1:
                    await self.bot.change_presence(
                        activity=Activity(
                            name="games",
                            type=ActivityType.PLAYING,
                        )
                    )
                elif random_activity == 2:
                    await self.change_presence(
                        activity=Activity(
                            name="a movie",
                            type=ActivityType.WATCHING,
                        )
                    )
                await asyncio.sleep(60)
            
          
def setup(bot):
    Presence(bot)

