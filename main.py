import interactions, random, asyncio
from interactions import *

bot = interactions.Client(intents=interactions.Intents.ALL)

@interactions.listen()
async def on_startup():
    print("Bot is ready!")
    await bot.change_presence(status=Status.AFK, activity=Activity(name="la drogue", type=ActivityType.GAME))


@listen()
async def on_message_create(event):
    x = event.message.content.lower()
    if event.message.author.id != 1111756058902409327: 
        if "quoi" in x: 
            await event.message.reply("Quoicoubeh")
        if "hein" in x:
            await event.message.reply("Apagnan")

@slash_command(name="bot_changelog", description="Ajoute un changelog pour le bot", scopes=[1111756433046908958], default_member_permissions=Permissions.ADMINISTRATOR)
async def bot_changelog(ctx: SlashContext):
    my_modal = Modal(
    ShortText(label="Version",
                custom_id="version",
                placeholder=f"MINOR.MAJOR.PATCH",
                required=True),

    ParagraphText(label="Changelog",
                    custom_id="changelogtext",
                    placeholder="Entrez les changements",
                    required=True),

title="Ajouter un changelog")
    

    await ctx.send_modal(modal=my_modal)
    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
    embed = Embed(title="Nouveau changelog !\t:tada:", description=f"\nChangements apportés par cette mise à jour :\n\n {modal_ctx.responses['changelogtext']}")
    embed.set_footer(text=f"Pipo#4026 - {modal_ctx.responses['version']}", icon_url=bot.user.avatar_url)
    await ctx.channel.send(embed=embed)
    await modal_ctx.send("Changelog ajouté !", ephemeral=True)



@slash_command(name="bagarre", description="C'est l'heure de la baguarre", scopes=[1111756433046908958])
async def bagarre(ctx : InteractionContext):
    msg = await ctx.send(content="https://cdn.discordapp.com/attachments/1111756433722187808/1112000937054195732/x.jpg")
    await asyncio.sleep(5)

    choix = random.randint(0,1)
    if choix == 0:
        await msg.edit(content="https://cdn.discordapp.com/attachments/1111756433722187808/1111998078023630919/l.jpg")
    elif choix == 1:
        await msg.edit(content="https://cdn.discordapp.com/attachments/1111756433722187808/1111998078732484669/w.jpg")


@slash_command(name="golf", description="Permet de jouer au golf avec un handicapé", scopes=[1111756433046908958])
async def golf(ctx : InteractionContext):
    await ctx.send("\t:person_doing_cartwheel::skin-tone-5:\n\n\t\t\t\t\t\t\t\t:manual_wheelchair::person_golfing::skin-tone-5:")

@slash_command(name="ping", description="Ping le bot", scopes=[1111756433046908958])
async def command_ping( ctx: InteractionContext):
    try : 
        websocket = bot.latency * 100
        await ctx.send(f"Pong ! :ping_pong: {round(websocket)} ms", ephemeral=True)
    except OverflowError: 
        await ctx.send("Le bot démarre... Attendez une dizaine de secondes puis recommencer :)", ephemeral=True)


@slash_command(name="info", description="Affiche les informations du bot", scopes=[1111756433046908958])
async def info(ctx : SlashContext):
        try : 
            embed = Embed(title="Informations du bot", color=Color.from_hex("#FF0000"))
            embed.add_field(name="Développé en", value="Python, avec [interactions.py (v5)](https://github.com/interactions-py/interactions.py)", inline=True)
            embed.add_field(name="Créé le", value=f"<t:1685136462:F>", inline=False)
            embed.add_field(name="Créé par", value=bot.owner, inline=False)
            embed.add_field(name="Serveurs", value=len(bot.guilds), inline=True)
            embed.add_field(name="Latence", value=f"{round(bot.latency * 100)} ms", inline=True)
            embed.add_field("Pour m'inviter sur votre serveur", value = "Cliquez **[ici](https://discord.com/api/oauth2/authorize?client_id=1111756058902409327&permissions=8&scope=bot)**")

            await ctx.send(embed=embed)
        except OverflowError : 
            await ctx.send("La commande est indisponible pour le moment. Réessayes dans quelques minutes.", ephemeral=True)

    
        
bot.start("MTExMTc1NjA1ODkwMjQwOTMyNw.GxoY3U.r-sV9ydUaGSFlQQM5hhhvc4ScY-8fHVU-rscnU")


