from interactions import * 


class Utiles(Extension):

    @slash_command("delrole", description="Supprime un rôle", default_member_permissions=Permissions.ADMINISTRATOR)
    @slash_option(
                name="role_name",
                description="Nom",
                required=True,
                opt_type=OptionType.ROLE)
    async def supprimer_role(self,ctx : SlashContext, role_name = Role):
        """
        Supprime un rôle

        Args:
            ctx (SlashContext): Le contexte
            role_name (Role): Le rôle à supprimer

        Returns:
            None
        """        
        await role_name.delete()
        await ctx.send(f"Le rôle ``{role_name.name}`` a bien été supprimé !", ephemeral=True)
        
                        

    @slash_command("delchannel", description="Supprime un salon",default_member_permissions=Permissions.ADMINISTRATOR)
    @slash_option(
        name="channel_nom",
        description="Nom du salon",
        required=True,
        opt_type=OptionType.CHANNEL)
    async def supprimer_salon(self, ctx : SlashContext, channel_nom : GuildChannel):
        """
        Supprime un salon

        Args:
            ctx (SlashContext): Le contexte
            channel_nom (GuildChannel): Le salon à supprimer
        
        Returns:
            None
        """      
        if channel_nom == ctx.channel:
            await ctx.send("Vous ne pouvez pas supprimer ce salon !", ephemeral=True)
            return

        await channel_nom.delete()
        await ctx.send(f"Le salon {channel_nom.name} a bien été supprimé !", ephemeral=True)
        


    @slash_command("nick", description="Change le pseudo d'un membre", default_member_permissions=Permissions.ADMINISTRATOR)
    @slash_option(
        name="pseudo",
        description="Nouveau pseudo",
        required=True,
        opt_type=OptionType.STRING)
    @slash_option(
        name="utilisateur",
        description="utilisateur",
        required=False,
        opt_type=OptionType.USER)
    async def change_pseudo(self, ctx : SlashContext, pseudo : str, utilisateur : Member = None):
        """
        Change le pseudo d'un membre

        Args:
            ctx (SlashContext): Le contexte
            pseudo (str): Le nouveau pseudo
            utilisateur (Member, optional): L'utilisateur. Defaults to None.
        
        Returns:
            None
        """
        if utilisateur == None : 
            utilisateur = ctx.author
        await utilisateur.edit_nickname(new_nickname=pseudo)
        await ctx.send(f"Le pseudo de {utilisateur.tag} a bien été changé en {pseudo}", ephemeral=True)
       
            
    @slash_command("clear", description="Supprime un nombre de messages", default_member_permissions=Permissions.ADMINISTRATOR)
    @slash_option(
        name="nombre_messages",
        description="Nombre de messages à supprimer",
        required=True,
        max_value=50,
        opt_type=OptionType.INTEGER)
    async def clear(self, ctx : SlashContext, nombre_messages : int):
        """
        Supprime un nombre de messages

        Args:
            ctx (SlashContext): Le contexte
            nombre_messages (int): Le nombre de messages à supprimer
        
        Returns: 
            None
        """
        await ctx.channel.purge(nombre_messages)
        await ctx.send(f"Les {nombre_messages} derniers messages ont bien été supprimés", ephemeral=True)
        

def setup(bot):
    Utiles(bot)