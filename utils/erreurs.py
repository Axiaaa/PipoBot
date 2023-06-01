from interactions import *

class Erreurs(Extension):

    @listen(disable_default_listeners=True)
    async def on_command_error(self, event: errors):
        """
        Gère les erreurs du bot

        Args:
            event (discord.ext.commands.errors): L'erreur
            
        Returns:
            None        
        """

        if isinstance(event.error, errors.CommandCheckFailure):
            await event.ctx.send(
                f"Vous n'avez pas la permission d'utiliser cette commande !",
                ephemeral=True,
            )
        else:
            await self.bot.on_command_error(self.bot, event)


def setup(bot): 
    Erreurs(bot)