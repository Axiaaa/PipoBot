from interactions import * 
import os



class Reload(Extension): 

    async def owner_check(ctx: InteractionContext):
        return ctx.author.id == 240430740158939139

    @check(check=owner_check)
    @slash_command(name="reload", description="Cette commande permet de recharger les extensions du bot.")
    async def reload(self, ctx : InteractionContext):
        
        def reload_extensions(bot, folder, prefix="", exclude_files=[]):
            extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
            for ext in extensions:
                bot.reload_extension(f"{prefix}{ext}")


        reload_extensions(self.bot, "commandes", "commandes.")
        reload_extensions(self.bot, "utils", "utils.")

        await ctx.respond(content="Fait !", ephemeral=True)




def setup(bot): 
    Reload(bot)