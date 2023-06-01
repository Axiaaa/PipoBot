from interactions import *

class Golf(Extension):
    @slash_command(name="golf", description="Permet de jouer au golf avec un handicapé")
    async def golf(self, ctx : InteractionContext):

        """
        Permet de jouer au golf avec un handicapé

        Args:
            ctx (InteractionContext): Le contexte

        Returns:
            None
        """
        await ctx.send("\t:person_doing_cartwheel::skin-tone-5:\n\n\t\t\t\t\t\t\t\t:manual_wheelchair::person_golfing::skin-tone-5:")

def setup(bot):
    Golf(bot)