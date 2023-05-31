from interactions import *
from random import randint

class Roll(Extension):
    
    @slash_command(name="roll", description="Lance un dé")
    async def roll(self, ctx : InteractionContext):
        roll = randint(1, 6)
        await ctx.send(f"Tu as fait un {roll} :dice:!")


def setup(bot):
    Roll(bot)
