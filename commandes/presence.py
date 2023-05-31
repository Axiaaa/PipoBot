from interactions import *
from random import randint


class Presence(Extension): 
  @listen()
  async def on_startup():
    while True:
          random_activity = randint(1, 2)
          if random_activity == 1:
              await bot.change_presence(
                  activity=inter.Activity(
                      name="games",
                      type=inter.ActivityType.PLAYING,
                  )
              )
          elif random_activity == 2:
              await bot.change_presence(
                  activity=inter.Activity(
                      name="a movie",
                      type=inter.ActivityType.WATCHING,
                  )
              )
          await asyncio.sleep(60)
          
          
 def setup(bot):
  Presence(bot)
