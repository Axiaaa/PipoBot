import interactions, asyncio
from interactions import *
from random import randint, choice


bot = interactions.Client(intents=interactions.Intents.ALL)

def PierreFeuilleCiseaux(choix: str):
    x = choice(["pierre", "papier", "ciseaux"])
    if (x == "pierre" and choix == "papier") or (x == "papier" and choix == "ciseaux") or (x == "ciseaux" and choix == "pierre"):
        return "w"
    elif (x == "pierre" and choix == "ciseaux") or (x == "papier" and choix == "pierre") or (x == "ciseaux" and choix == "papier"):
        return "l"
    else:
        return "d"
    

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

    choix = randint(0,1)
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



@slash_command(name="shifumi", description="Lance une partie de shifumi contre le bot",scopes=[1111756433046908958])
async def shifumi(ctx: InteractionContext):
    
    buttons : list[ActionRow] = [
    ActionRow(
        Button(
            style=ButtonStyle.GREEN, 
            custom_id=f"{ctx.user.id}_shifumi_pierre",
            emoji=":rock:"
        ),
        Button(
            style=ButtonStyle.DANGER,
            custom_id=f"{ctx.user.id}_shifumi_papier",
            emoji=":roll_of_paper:"            
        ),
        Button(
            style=ButtonStyle.BLUE,
            emoji=":scissors:",
            custom_id=f"{ctx.user.id}_shifumi_ciseaux"

        ))       
    ]
    await ctx.send(embed=Embed(
        title=f"Shifumi avec {ctx.author.display_name}",
        description="**Pierre** :rock:\n\n**Feuille** :roll_of_paper:\n\n**Ciseaux** :scissors:\n\nCliquez sur un des boutons pour choisir ? :arrow_heading_down:"), components=buttons)
    

@listen(event_name="on_component")
async def button_ciseaux(event): 

    x = event.ctx.custom_id.split("_")
    if f"{event.ctx.author.id}" == x[0] : 
        match x[2] :
            case "ciseaux" :
                resultat = PierreFeuilleCiseaux("ciseaux")
                if resultat == "l":
                    await event.ctx.edit_origin(components=(), embed=Embed(
                        title="Défaite",
                        description=f":scissors:\t**VS**\t:rock:\n\nVous avez perdu car j'ai choisi de faire la pierre ! :smiling_imp:",
                        color="#FF0000"
                    ))
                elif resultat == "w":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Victoire",
                        description=f":scissors:\t**VS**\t:roll_of_paper:\n\nVous avez gagné car j'ai choisi de faire la feuille !\nBien joué :tada:",
                        color= "#32CD32"
                    ))
                elif resultat == "d":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                    title="Egalité !",
                    description=f":scissors:\t**VS**\t:scissors:\n\nJ'ai choisi de faire les ciseaux et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                    ))
            case "pierre" :
                resultat = PierreFeuilleCiseaux("pierre")
                if resultat == "l":
                    await event.ctx.edit_origin(components=(), embed=Embed(
                        title="Défaite",
                        description=f":rock:\t**VS**\t:roll_of_paper:\n\nVous avez perdu car j'ai choisi de faire la feuille ! :smiling_imp:",
                        color="#FF0000"
                    ))
                elif resultat == "w":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Victoire",
                        description=f":rock:\t**VS**\t:scissors:\n\nVous avez gagné car j'ai choisi de faire les ciseaux !\nBien joué :tada:",
                        color= "#32CD32"
                    ))
                elif resultat == "d":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                    title="Egalité !",
                    description=f":rock:\t**VS**\t:rock:\n\nJ'ai choisi de faire la pierre et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                    ))
            case "papier" :
                resultat = PierreFeuilleCiseaux("pierre")
                if resultat == "l":
                    await event.ctx.edit_origin(components=(), embed=Embed(
                        title="Défaite",
                        description=f":roll_of_paper:\t**VS**\t:scissors:\n\nVous avez perdu car j'ai choisi de faire les ciseaux ! :smiling_imp:",
                        color="#FF0000"
                    ))
                elif resultat == "w":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Victoire",
                        description=f":roll_of_paper:\t**VS**\t:rock:\n\nVous avez gagné car j'ai choisi de faire la pierre !\nBien joué :tada:",
                        color= "#32CD32"
                    ))
                elif resultat == "d":
                    await event.ctx.edit_origin(components=(),embed=Embed(
                    title="Egalité !",
                    description=f":roll_of_paper:\t**VS**\t:roll_of_paper:\n\nJ'ai choisi de faire la feuille et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                    ))
                
    else : 
        if x[1] != "shifumi" :
            return
        await event.ctx.send("Vous ne pouvez pas intéragir avec le jeu des autres !", ephemeral=True)



bot.start(os.environ["TOKEN"])


