from optparse import Option
import interactions
from datetime import datetime


bot = interactions.Client(
    token="ODc5NjIzMTMzOTExNDY1OTk2.YSSa4Q.-O3W2U9OcyN-142NVJC8ehiXUa0",
    presence=interactions.ClientPresence(
        activities=[
            interactions.PresenceActivity(
                type=interactions.PresenceActivityType.GAME,
                name="Fansom"
            )
        ],
        status=interactions.StatusType.DND
    )
)


@bot.event
async def on_ready():
    print("Bot is online.")


@bot.command(
    name="ping",
    description="Ping Pong!"
)
async def _ping(ctx: interactions.CommandContext):
    await ctx.send(content="Pong! 🏓")


@bot.command(
    name="help",
    description="Ask for help"
)
async def _help(ctx: interactions.CommandContext):
    mention = ctx.author.mention
    member = ctx.author
    await ctx.send(f"{mention} DMed")
    embed = interactions.Embed(title="Help")
    await member.send(embeds=embed)


@bot.command(
    name="support",
    description="Get a link to the support server"
)
async def _support(ctx: interactions.CommandContext):
    button = [
        interactions.Button(
            style=interactions.ButtonStyle.LINK,
            label="Join",
            url="https://discord.gg/QwXXNGNkeh"
        )
    ]
    await ctx.send(content="Here you go!", components=button)


@bot.command(
    name="whois",
    description="Who is someone",
    options=[
        interactions.Option(
                type=interactions.OptionType.USER,
                name="user",
                description="Select a user",
                required=False
        ),
    ],
)
async def _whois(ctx: interactions.CommandContext, user: interactions.Member = None):
    if user == None:
        user = ctx.author
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    fields = [
        interactions.EmbedField(
            name="Avatar URL", value=f"[Here]({user.user.avatar_url})", inline=False),
        interactions.EmbedField(
            name="ID", value=str(user.user.id), inline=False),
        interactions.EmbedField(
            name="Joined time", value=f"<t:{round(user.joined_at.timestamp())}>", inline=True),
        interactions.EmbedField(
            name="Account creation", value=f"<t:{user.user.id.epoch}>", inline=True), ]
    author = interactions.EmbedAuthor(text=f"{user.user.username}",
                                      url=user.user.avatar_url)._json
    thumbnail = interactions.EmbedImageStruct(url=user.user.avatar_url)._json
    footer = interactions.EmbedFooter(
        text=f"Requested by {ctx.author.user.username}#{ctx.author.user.discriminator} | Today at {current_time}", icon_url=ctx.author.user.avatar_url)._json
    embed = interactions.Embed(
        title=f"{user.user.username}",
        description=f"{user.mention}",
        color=0xff9100,
        author=author,
        thumbnail=thumbnail,
        footer=footer,
        fields=fields
    )
    await ctx.send(embeds=embed)


@bot.command(
    name="infinity_loop",
    description="Dropdowns and buttons!",
    options=[interactions.Option(
        name="choose_one", description="Choose one.", type=interactions.OptionType.STRING, required=True, choices=[interactions.Choice(name="button", value="inf_b"), interactions.Choice(name="dropdown", value="inf_st_menu")])]
)
async def _infinity_loop(ctx: interactions.CommandContext, choose_one: str):
    pass


bot.start()
