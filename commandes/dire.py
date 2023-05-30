from interactions import *

class Dire(Extension):
    @slash_command(name="dire", description="Fais parler le bot")
    @slash_option(name="texte", description="Ce que le bot doit dire", opt_type=OptionType.STRING)
    async def dire(self,ctx: InteractionContext, texte : str):
        await ctx.send("Message envoyé :white_check_mark:", ephemeral=True)
        await ctx.channel.send(texte)

def setup(bot):
    Dire(bot)
    