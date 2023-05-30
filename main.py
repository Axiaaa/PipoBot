from interactions import * 
import os

bot = Client(intents=Intents.ALL)

@listen()
async def on_startup():
    print("Bot is ready!")
    await bot.change_presence(status=Status.AFK, activity=Activity(name="la drogue", type=ActivityType.GAME))


def load_extensions(bot, folder, prefix="", exclude_files=[]):
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        bot.load_extension(f"{prefix}{ext}")

load_extensions(bot, "commandes", "commandes.")
load_extensions(bot, "utils", "utils.")


bot.start("TOKEN")
