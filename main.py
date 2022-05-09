import interactions
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv
from random import randint
load_dotenv()
token = os.getenv("TOKEN")

bot = interactions.Client(
    token = token,
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
    print("Bot is online")


@bot.command(
    name="ping",
    description="Ping Pong!"
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send(content="Pong! 🏓")


@bot.command(
    name="help",
    description="Ask for help"
)
async def help(ctx: interactions.CommandContext):
    mention = ctx.author.mention
    member = ctx.author
    await ctx.send(f"{mention} DMed")
    embed = interactions.Embed(title="Help")
    await member.send(embeds=embed)


@bot.command(
    name="support",
    description="Get a link to the support server"
)
async def support(ctx: interactions.CommandContext):
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
async def whois(ctx: interactions.CommandContext, user: interactions.Member = None):
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
    name="generate",
    description="Dropdowns and buttons!",
    options=[interactions.Option(
        name="choose_one", description="Choose one.", type=interactions.OptionType.STRING, required=True, choices=[interactions.Choice(name="dropdown", value="g_st_menu"), interactions.Choice(name="button", value="g_b")])]
)
async def generate(ctx: interactions.CommandContext, choose_one: str):
    if choose_one == "g_st_menu":
        print(choose_one)
        select_menu = interactions.SelectMenu(
            custom_id="g_st_menu",
            options=[interactions.SelectOption(label="Option 1", value="option-1"),
                     interactions.SelectOption(label="Option 2", value="option-2")],
            placeholder="Placeholder"
        )
        await ctx.send("Hello", components=select_menu)
    else:

        button = [interactions.Button(
            style=interactions.ButtonStyle.DANGER,
            label="Click me!",
            custom_id="g_b"
        )]
        await ctx.send("Hi", components=button)


@bot.component("g_b")
async def g_b(ctx: interactions.ComponentContext):
    await ctx.send("Hi! You've clicked the button!")
    await ctx.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713", ephemeral=True)


@bot.component("g_st_menu")
async def g_st_menu(ctx: interactions.ComponentContext, option: str):
    await ctx.send(f"Hi! You've selected {', '.join(option)}!")
    await ctx.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713", ephemeral=True)

@bot.command(
    name="nitrogen",
    description="I'll gift you nitro.")
async def nitrogen(ctx:interactions.CommandContext):
    button=interactions.Button(
        style=interactions.ButtonStyle.SUCCESS,
        custom_id="accept",
        label="Accept",
        disabled=False
    )
    thumbnail = interactions.EmbedImageStruct(url="https://www.nukebot.org/Nitro.png")._json
    embed = interactions.Embed(
        title="You've been gifted a subscription!",
        description=f"{ctx.author.user.username}#{ctx.author.user.discriminator} gifted you **nitro classic** for ***1 year!***",
        thumbnail=thumbnail
    )
    msg = await ctx.send(embeds=embed, components=button)
    await asyncio.sleep(randint(25,60))
    embed2 = interactions.Embed(
        title="You've been gifted a subscription!",
        description="Hmm, it seems someone already claimed this gift.",
        thumbnail=thumbnail
    )
    button2=interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        custom_id="accept2",
        label="Accept",
        disabled=True)
    await msg.edit(embeds=embed2, components=button2)
@bot.command(name="rules", description="Send rules to the channel", scope=877823624315301908)
async def rules(ctx):
    your_json={
  "content": " ",
  "embeds": [
    {
      "title": "Rules",
      "description": "**Welcome to Fansom!**\nThese are the rules in the server **Fansom**!",
      "color": 16742912,
      "fields": [
        {
          "name": "**1. Respect Everyone and don't cause drama**",
          "value": "Please don't harass/bully anyone or be toxic and avoid having any fights/ creating drama on this server. Swearing or cursing is not allowed in here, doing so will get you in trouble."
        },
        {
          "name": "2. Follow Discord TOS",
          "value": "Make sure to follow Discord Terms of service and guidelines at all times. Any violation will result in an instant ban.\n🔗 https://discord.com/terms\n🔗 https://discord.com/guidelines"
        },
        {
          "name": "3. No form of Racism",
          "value": "Any form of Racism will not be tolerated. The use of Racial slurs (e.g. N-word) is prohibited and will result in a permanent ban."
        },
        {
          "name": "4. No Illegal Actions",
          "value": "Do not talk about or do anything illegal on the server. This includes posting code that can be used to commit a crime. Do not post malicious links or files that could be used to steal accounts or information anywhere. Doing so will get you in trouble."
        },
        {
          "name": "***5. No NSFW***",
          "value": "Do not send any NSFW images/emotes or discuss NSFW topics anywhere on this server. This also includes any suggestive emojis. Any kind of NSFW will ***not be tolerated***."
        },
        {
          "name": "6. Do not spam",
          "value": "Don't spam within channels, this can mean:\n➥Chat Flood: Typing separate lines very quickly\n➥Wall Text: Typing out large blocks of text \n➥Chaining:  Lyrics that make up a song etc\n➥Repetitive Messages: Posting the same images/emojis multiple times \n➥Epileptic Emotes: Posting/reacting with flashy GIFs or Emotes \n\n➥Zalgo: Like t̷̯̳͚̯̉̎͊h̴̨̡̯͔͈̐͑͗͜ì̶͕̹̪̼̗̟̅͂̈́ş̶̟͎̩͋̇̊̊͒̓ͅ\n\nYou can only spam in <#941232755864391701>."
        },
        {
          "name": "7. Don't constantly beg for nitro, roles, items or anything similar.",
          "value": "Don't beg for nitro, roles, items, or anything similar again and again, it's annoying."
        },
        {
          "name": "8. Do not post unapproved advertising.",
          "value": "Only advertise in AD AREA."
        }
      ]
    },
    {
      "title": "**Guidelines:**",
      "description": "**Please verify, go to │✅・verify-here and verify to get access to the server.**",
      "color": 16742912
    },
    {
      "title": "If you need any help, please open a ticket.",
      "description": "For more information, go to <#940775410495524927>",
      "color": 16742912
    },
    {
      "description": "[Click to join the server](https://discord.gg/QwXXNGNkeh)",
      "color": 16742912
    }
  ],
  "attachments": []
}
    embeds = [interactions.Embed(**embed) for embed in your_json["embeds"]]
    channel = await ctx.get_channel()
    await ctx.channel.send("@everyone https://discord.gg/QwXXNGNkeh ", embeds=embeds)
bot.start()
