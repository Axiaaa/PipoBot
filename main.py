from interactions import * 
import os, asyncio
from server import keep_alive
from random import randint

keep_alive()
bot = Client(intents=Intents.ALL)

@listen()
async def on_startup():
  print("Bot is ready")
  while True:
        random_activity = randint(1, 2)
        if random_activity == 1:
            await bot.change_presence(
                status= Status.ONLINE,
                activity= Activity(
                    type= ActivityType.WATCHING,
                    name= f"{len(bot.guilds)} serveurs"
                )
                )
        elif random_activity == 2:
            await bot.change_presence(
                status= Status.ONLINE,
                activity= Activity (
                    type= ActivityType.WATCHING,
                    name= f"You"
                    ) 
                )
        await asyncio.sleep(60)


def load_extensions(bot, folder, prefix="", exclude_files=[]):
    """
    Charge les extensions du bot

    Args:
        bot (discord.ext.commands.Bot): Le bot
        folder (str): Le dossier contenant les extensions
        prefix (str, optional): Le préfixe des extensions. Defaults to "".
        exclude_files (list, optional): Les fichiers à exclure. Defaults to [].
    
    Returns:
        None
    """
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        bot.load_extension(f"{prefix}{ext}")

load_extensions(bot, "commandes", "commandes.")
load_extensions(bot, "utils", "utils.")


bot.start(os.environ["TOKEN"])
