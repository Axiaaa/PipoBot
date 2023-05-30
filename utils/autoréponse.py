from interactions import *



class Autoréponse(Extension):

    @listen()
    async def on_message_create(self, event):
        x = event.message.content.lower()
        if event.message.author.id != 1111756058902409327: 
            if "quoi" in x: 
                await event.message.reply("Quoicoubeh")
            if "hein" in x:
                await event.message.reply("Apagnan")
            if "<@1111756058902409327>" in x:
                await event.message.reply("Vous m'avez mentionné ? :eyes:\nPour voir mes commandes, faites `/help` !")
def setup(bot):
    Autoréponse(bot)
    