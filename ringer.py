import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "$")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! **{round(client.latency * 1000)}ms!**')

@client.command()
async def Salman(ctx):
    await ctx.send("oh he is pro!")

@client.command()
async def Esai(ctx):
    await ctx.send("Esai is always pro!!")

@client.command()
async def Hello(ctx):
    await ctx.send("HI")

@client.command()
async def Naren(ctx):
    await ctx.send("Oh nothing to say about him!")

@client.command()
async def info(ctx):
    await ctx.send("""
    **One important news the message you send need to be same as the commands no mixing of capitals and smalls**
    > $Hello - sends a hi to you.
    > $Naren - shows info about Naren.  
    > $Salman - shows info about Salman.
    > $Riyaz - shows info about Riyaz.
    > $Esai - shows info about Esai.
    > $lol - responses to lol.
    > $goodnight - greets you!
    >$say`your message` - bot conveys your message.
    >$kill - say a funny message that the pinged user has been killed
    
    **This is for the mods and admins**
    > $kick - kicks an user from the server
    > $ban - bans an user from the server
    > $purge - purge 10 messages(if typed $purge`3` it will remove 3 messages) 
     """)

@client.command()
async def invite(ctx):
    await ctx.send("I am a private bot you can't invite me to your server!")

@client.command()
async def Riyaz(ctx):
    await ctx.send("RIYAZ IS PUBG PRO!!" )

@client.command()
async def fight(ctx):
     await ctx.send("Gentlemen, you can’t fight in here. This is the war room")

@client.command()
async def goodnight(ctx):
     await ctx.send("Goodnight sweet dreams!")

@client.command()
async def sorry(ctx):
     await ctx.send("i am really sorry!")

@client.command()
async def lol(ctx):
     await ctx.send("lel")

@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, * , reason=None):
 await member.kick(reason=reason)
 await ctx.send(f'@{member} has been kicked')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f'@{member} has been banned!')

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kill(ctx, member: discord.Member):
    await ctx.send(f'You have killed {member.mention}! RIP!!! {member.mention}:skull_crossbones:')

@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.send(mesg)

@client.command()
async def coinflip(ctx):
    choices = (":red_circle: :purple_circle: HEADS :red_circle: :purple_circle: ", ":red_circle: :purple_circle: TAILS :red_circle: :purple_circle: ")
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def goodorbad(ctx):
    choices = ("BAD :x: ", "GOOD :white_check_mark: ")
    ranstuff = random.choice(choices)
    await ctx.send(ranstuff)

client.run("NjIyNzQ2MTMxNzg4NTk1MjAw.XuItLw.2C2vsv68ED46FuRGIGA2ZkyPzq0")
