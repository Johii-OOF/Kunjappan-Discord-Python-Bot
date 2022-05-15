import discord
from discord.ext import commands
import random
import asyncio
import os
import keep_alive
import aiohttp
import requests
import json
from discord import Game


client = commands.Bot(command_prefix="da ", intents=discord.Intents.all())
    


@client.event
async def on_ready():

  await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers | ana help"))

  await client.change_presence(activity=discord.Streaming(name="your browser history",url=f"https://www.youtube.com/watch?v=j7gKwxRe7MQ"))

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sigma Songs"))

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

  print("ready mwonuse")

async def ch_pr():
  await client.wait_until_ready()

  statuses = ["Cyberpunk 2077","with ur mum",f"on {len(client.guilds)} servers | da help","Sigma Songs","with no one","mods","Amongus","uyir lyf","Elden Ring"]

  while not client.is_closed():

    status = random.choice(statuses)

    await client.change_presence(activity=discord.Game(name=status))

    await asyncio.sleep(600)














snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
@commands.cooldown(1, 10, commands.BucketType.user)
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"That message was sent by {snipe_message_author[channel.id]}, nee menden anallo")
        await ctx.send(embed = em)
    except KeyError: 
        await ctx.send(f"fuck off, No deleted messages found in #{channel.name} <a:NoOoOo:907224828652707900> epic fail L 👎" ,delete_after=3)











@client.command(case_insensitive=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, saymsg=None):
    if saymsg == None:
        return await ctx.send("Just use, da say (your text)")

    sayEmbed = discord.Embed(title="Kunjappan said,",
                             color=discord.Color.blue(),
                             description=f"{saymsg}")
    sayEmbed.timestamp = ctx.message.created_at

    await ctx.send(embed=sayEmbed)






@client.command(case_insensitive=True)
@commands.cooldown(1, 300, commands.BucketType.user)
async def hello(ctx):
    await ctx.reply("Bruh, thats so cringe", tts=True)


@client.command(case_insensitive=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def nsfw(ctx):
    responses = [":flag_cn: **MESSAGE FROM THE MINISTRY OF STATE** :flag_cn:\nAll Social Credits have been deducted from your account. \nYou are to be abolished and terminated by the request of the government! Bad work citizen, you have been the most untrustworthy citizen and a scoundrel to our glorious country! \nBy tomorrow, you will face a life-threatening punishment by the request of the government! \nGlory to the Chinese Communist Party!\nhttps://cdn.discordapp.com/attachments/763740330629398588/865242744162484254/CCP.mp4","https://cdn.discordapp.com/attachments/800935772185165835/907968975491711016/Venda_Mwonu_SUS.mp4",]
    await ctx.reply(random.choice(responses), mention_author= True)























@client.command(case_insensitive=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def oruhelp(ctx):
    await ctx.reply(
        "https://media.discordapp.net/attachments/724055819548622968/895557138926149693/image0.gif"
    )


@client.command(case_insensitive=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def padicha(ctx):
    await ctx.send("<:yikes:895312765613391872>")


@client.command(case_insensitive=False,help='This command posts the news link')
@commands.cooldown(1, 5, commands.BucketType.user)
async def news(ctx):
    await ctx.send("https://youtu.be/zcrUCvBD16k", delete_after=10)


@client.command(name='ping',help='latency of the bot')
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(
        f'**Poli Sanam, Ente Latency: {round(client.latency * 1000)}ms <:BiteLip:834635174183698446>**'
    )














format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@client.command()
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(color=ctx.guild.owner.top_role.color)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(
        name=f"Information About **{ctx.guild.name}**: ",
        value=
        f"\n<a:YellowArrowRight:906924676289282068> Owner: **{ctx.guild.owner}** <:BiteLip:834635174183698446>\n<a:YellowArrowRight:906924676289282068> Location: **{ctx.guild.region}** <a:uh:906917859899367464> \n<a:YellowArrowRight:906924676289282068> Creation: **{ctx.guild.created_at.strftime(format)}** \n<a:YellowArrowRight:906924676289282068> Members: **{ctx.guild.member_count} <a:NoOoOo:907224828652707900>**\n<a:YellowArrowRight:906924676289282068> Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories <:pepe_cool:890618729996627988>\n<a:YellowArrowRight:906924676289282068> Verification: **{str(ctx.guild.verification_level).upper()}**"
    )
    await ctx.send(embed=embed)











#avatar
@client.command(aliases=['av'], name='avatar', help='Shows the avatar of the user')
@commands.cooldown(1, 60, commands.BucketType.user)
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    icon_url = member.avatar_url

    avatarEmbed = discord.Embed(
        title=f"AMBO ithu kando {member.name}\'s Avatar, killadi!!",
        color=0xFFFFFF)

    avatarEmbed.set_image(url=f"{icon_url}")

    avatarEmbed.timestamp = ctx.message.created_at

    await ctx.send(embed=avatarEmbed)







#emojify
@client.command(name='emojify', help='Emojifies the text lmao')
@commands.cooldown(1, 5, commands.BucketType.user)
async def emojify(ctx, *, text):
    emojis = []
    for beans in text.lower():
        if beans.isdecimal():
            num2word = {
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
            }
            emojis.append(f':{num2word.get(beans)}:')
        elif beans.isalpha():
            emojis.append(f':regional_indicator_{beans}:')
        else:
            emojis.append(beans)
    await ctx.send(''.join(emojis))










@client.command(
    aliases=['8ball', 'da', 'does', 'will', 'is', 'would', 'am', 'do','are'],
    name='_8ball',
    help='you can also use da, does, will, is, would, do, are')
@commands.cooldown(1, 8, commands.BucketType.user)
async def _8ball(ctx, *, question):
    responses = [
        'ada 👍', 'no 😳', 'idk man', 'brr i forgor 💀', 'yes',
        'fuck off', 'my sources say no',
        'its a no from me', 'onnu poyeda 😒', 'ayee injathi vanam', 'yesnt',
        'fuck off 😑', 'Huh', 'Tf', 'myre', '👌', 'am not that guy', '😑',
        'https://cdn.discordapp.com/emojis/895312765613391872.png?size=128','https://cdn.discordapp.com/attachments/775769580895338508/936544015795503114/Banana_council_disaproves_of_this.mp4',
        'https://tenor.com/view/sopyues-spongebob-spongebob-meme-twerking-twerk-gif-20539152','https://c.tenor.com/LSdPTJ_Uki4AAAAM/haram-heisenberg.gif','man','ah','https://cdn.discordapp.com/attachments/775769580895338508/948561154031104012/Tyler_The_Creator_-_5__480_X_526_.mp4','https://cdn.discordapp.com/attachments/775769580895338508/948557545923051580/Tyler_The_Creator_-_3__240_X_266_.mp4'
    ]
    await ctx.reply(random.choice(responses), mention_author=False)









@client.command(aliases=['gn'], name='wishgn', help='wishes you gn')
@commands.cooldown(1, 5, commands.BucketType.user)
async def wishgn(ctx):
    responses = [
        '<a:uh:906917859899367464>', 'gn homie',
        'sleep tight, demons might be under your bed', 'onnu povamo?', 'bruh','gn girl','umma']
    await ctx.reply(random.choice(responses), mention_author=False)













@client.command(name='meme', help='pulls up a meme')
@commands.cooldown(1, 30, commands.BucketType.user)
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
            res = await r.json()
            title = ("here is a meme")
            url = res['data']['children'][random.randint(0, 25)]["data"]["url"]
            embed = discord.Embed(title=f'{title}',
                                  color=discord.Color.orange(),
                                  timestamp=ctx.message.created_at,
                                  url=f'{url}')
            embed.set_image(url=f"{url}")
            await ctx.send(embed=embed)




  

@client.command(name='cat', help='pulls up a cat')
@commands.cooldown(1, 30, commands.BucketType.user)
async def cat(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/cat/hot.json') as r:
            res = await r.json()
            title = ("Kunjappan gives you a cat photo")
            url = res['data']['children'][random.randint(0, 25)]["data"]["url"]
            embed = discord.Embed(title=f'{title}',
                                  color=discord.Color.orange(),
                                  timestamp=ctx.message.created_at,
                                  url=f'{url}')
            embed.set_image(url=f"{url}")
            await ctx.send(embed=embed)


@client.command(name='dog', help='what da dog doin')
@commands.cooldown(1, 30, commands.BucketType.user)
async def dog(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dog/hot.json') as r:
            res = await r.json()
            title = ("Kunjappan gives you a doggo photo")
            url = res['data']['children'][random.randint(0, 25)]["data"]["url"]
            embed = discord.Embed(title=f'{title}',
                                  color=discord.Color.orange(),
                                  timestamp=ctx.message.created_at,
                                  url=f'{url}')
            embed.set_image(url=f"{url}")
            await ctx.send(embed=embed)














#maths commands below
#divison command
@client.command(aliases=['divide'], name='div', help='ye, it just divides it')
async def div(ctx, num1: float, num2: float):
    answer = num1 / num2

    ans_em = discord.Embed(
        title='Division',
        description=f'Question: {num1} ÷ {num2}\n\nAnswer = {answer}',
        colour=discord.Colour.from_rgb(252, 252, 0))

    await ctx.send(embed=ans_em)

@div.error
async def div_error(ctx, error):
    print(error)
    print(type(error))
    print(dir(error))
    print(error.args)

    if isinstance(error, commands.BadArgument):
        await ctx.send(
            'Bruh, use it correctly type *"da div"* if you dont understand it'
        )

    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            'Bruh, that might be impossible to do or try using it correctly, type *"da div"* if you dont understand it'
        )

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'It needs two values, use it like this - **da div (first number) (second number)**'
        )

    print(ctx.args)
    print(ctx.message)

@client.event
async def on_command_error(ctx, error):
    print('[on_command_error] error:', error)
    print('[on_command_error] ctx:', ctx)










#addition command
@client.command(aliases=['addition', 'sum'],
                name='add',
                help='ye, it just adds it')
async def add(ctx, num1: float, num2: float):
    answer = num1 + num2

    ans_em = discord.Embed(
        title='Addition',
        description=f'Question: {num1} + {num2}\n\nAnswer = {answer}',
        colour=discord.Colour.from_rgb(255, 0, 0))

    await ctx.send(embed=ans_em)

@add.error
async def add_error(ctx, error):
    print(error)
    print(type(error))
    print(dir(error))
    print(error.args)

    if isinstance(error, commands.BadArgument):
        await ctx.send(
            'Bruh, use it correctly type *"da add"* if you dont understand it'
        )

    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            'Bruh, use it correctly type *"da add"* if you dont understand it'
        )

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'It needs two values, use it like this - **da add *(first number)* *(second number)***'
        )

    print(ctx.args)
    print(ctx.message)

@client.event
async def on_command_error(ctx, error):
    print('[on_command_error] error:', error)
    print('[on_command_error] ctx:', ctx)










#substraction
@client.command(aliases=['subtract', 'minus'],
                name='sub',
                help='ye, it just subtracts it')
async def sub(ctx, num1: float, num2: float):
    answer = num1 - num2

    ans_em = discord.Embed(
        title='Subtraction',
        description=f'Question: {num1} - {num2}\n\nAnswer = {answer}',
        colour=discord.Colour.from_rgb(255, 0, 0))

    await ctx.send(embed=ans_em)

@sub.error
async def sub_error(ctx, error):
    print(error)
    print(type(error))
    print(dir(error))
    print(error.args)
    if isinstance(error, commands.BadArgument):
        await ctx.send(
            'Bruh, use it correctly type *"da minus"* if you dont understand it'
        )

    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            'Bruh, use it correctly type *"da minus"* if you dont understand it'
        )

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'It needs two values, use it like this - **da minus *(first number)* *(second number)***'
        )

    print(ctx.args)
    print(ctx.message)

@client.event
async def on_command_error(ctx, error):
    print('[on_command_error] error:', error)
    print('[on_command_error] ctx:', ctx)














#Multiplication
@client.command(aliases=['times', 'multiply'],
                name='multi',
                help='ye, it just multiplies it')
async def multi(ctx, num1: float, num2: float):
    answer = num1 * num2

    ans_em = discord.Embed(
        title='Multiplication',
        description=f'Question: {num1} x {num2}\n\nAnswer = {answer}',
        colour=discord.Colour.from_rgb(255, 0, 0))

    await ctx.send(embed=ans_em)

@multi.error
async def multi_error(ctx, error):
    print(error)
    print(type(error))
    print(dir(error))
    print(error.args)
    if isinstance(error, commands.BadArgument):
        await ctx.send(
            'Bruh, use it correctly type *"da multi"* if you dont understand it'
        )

    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            'Bruh, use it correctly type *"da multi"* if you dont understand it'
        )

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'It needs two values, use it like this - **da multi *(first number)* *(second number)***'
        )

    print(ctx.args)
    print(ctx.message)

@client.event
async def on_command_error(ctx, error):
    print('[on_command_error] error:', error)
    print('[on_command_error] ctx:', ctx)











@client.command(aliases=['info'],
                name='userinfo',
                help='ye, it just gives the info')
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, member: discord.User = None):
    if member is None:
        member = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=member.mention)
    embed.set_author(name=str(member), icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Joined", value=member.joined_at.strftime(date_format))

    embed.add_field(name="Registered",
                    value=member.created_at.strftime(date_format))
    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(member.roles) - 1),
                        value=role_string,
                        inline=False)
    perm_string = ', '.join([
        str(p[0]).replace("_", " ").title() for p in member.guild_permissions
        if p[1]
    ])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='user ID lmao: ' + str(member.id))
    return await ctx.send(embed=embed)






@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def count(ctx):
  message = await ctx.send("1")
  await asyncio.sleep(1)
  await message.edit(content="1,2")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5,6")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5,6,7")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5,6,7,8")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5,6,7,8,9")
  await asyncio.sleep(1)
  await message.edit(content="1,2,3,4,5,6,7,8,9,10")
  await asyncio.sleep(2)
  await message.edit(content="<:rock:931510636175818782>")






@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def maskoff(ctx):
  message = await ctx.send("It's about drive <:rock:931510636175818782> ")
  await asyncio.sleep(1)
  await message.edit(content="It's about power :muscle:")
  await asyncio.sleep(2)
  await message.edit(content="We stay hungry, we devour")
  await asyncio.sleep(2)
  await message.edit(content="Put in the work!")
  await asyncio.sleep(2)
  await message.edit(content="Put in the hours :hourglass_flowing_sand:")
  await asyncio.sleep(2)
  await message.edit(content="And take what's ours!! :triumph:")
  await asyncio.sleep(2)
  await message.edit(content="<a:therock:933744399484071946>")


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
















@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Enich podey, try after {:.2f}s, <a:NotFunnyBlink:906927061296349196> ||<a:uh:906917859899367464> you are annoying <a:uh:906917859899367464>||'.format(error.retry_after)
        await ctx.reply(msg)




keep_alive.keep_alive()
my_secret = os.environ['TOKEN']
client.loop.create_task(ch_pr())
client.run(my_secret)
