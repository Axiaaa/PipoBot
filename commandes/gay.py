from interactions import * 
from random import randint

class Gay(Extension):

    @slash_command(name="gay", description="2nd degrès | Vérifie à quel point un utilisateur est gay")
    @slash_option(
        name="utilisateur",
        description="utilisateur",
        required=False,
        opt_type=OptionType.USER)
    async def gay(self, ctx : InteractionContext, utilisateur : Member = None):
        """
        Affiche le gaymeter d'un utilisateur

        Args:
            ctx (InteractionContext): Le contexte
            utilisateur (Member, optional): L'utilisateur à tester. Defaults to None.
        
        Returns:
            None
        """
        if utilisateur == None : 
            utilisateur = ctx.author
        embed=Embed(
            title=f"Gaymeter de {utilisateur.display_name}",
            description=f"{utilisateur.mention} est gay à {randint(0,100)}% ! :rainbow_flag:",
            color=0x00ff00,
            footer=f"A prendre au 2nd degrès !",
        )
        await ctx.send(embed=embed)

def setup(bot):
    Gay(bot)