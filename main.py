import discord
import time 
import random
from discord import app_commands
from discord.ext import commands


TOKEN = ""

with open("TOKEN.txt", "r") as file:
    TOKEN = file.readline()

#hello friends


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="^", intents=intents)

bot = Bot()

#tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command(with_app_command=True)
async def test(ctx):
    await ctx.send("Hybrid command")



@bot.group(with_app_command=True, fallback="pfp")
async def pfp(ctx):
    user = ctx.message.author
    pfp = user.avatar
    embed = discord.Embed()
    embed.set_image(url=pfp)
    await ctx.message.reply(embed=embed)

@pfp.command(with_app_command=True)
async def get(ctx, handle):
    try:
        user = await ctx.bot.fetch_user(handle[handle.index("@") + 1: -1])
        pfp = user.avatar
        embed = discord.Embed()
        embed.set_image(url=pfp)
        await ctx.message.reply(embed=embed)
    except Exception:
        await ctx.reply("Please pass a valid tag in order to use the function")


@bot.command(with_app_command=True)
async def countLetters(ctx, arg):
    count = len(arg)

    await ctx.reply("There are " + str(count) + " letters in the word " + arg) 


@bot.group(with_app_command=True, fallback="rps_rock")
async def rps_rock(ctx):
    computer=random.choice(['rock','paper','scissors'])
    if "scissors" == computer:
        await ctx.reply("You chose rock.\nThe Bot chose " + computer)
        await ctx.reply("You Won!!")
    elif "paper" == computer:
        await ctx.reply("You chose rock.\nThe Bot chose " + computer)
        await ctx.reply("The Bot Won!!")
    else:
        await ctx.reply("You chose rock and the Bot chose " + computer + "\nIt's a tie!!")


@bot.group(with_app_command=True, fallback="rps_paper")
async def rps_paper(ctx):
    computer=random.choice(['rock','paper','scissors'])
    if "rock" == computer:
        await ctx.reply("You chose paper.\nThe Bot chose " + computer)
        await ctx.reply("You Won!!")
    elif "scissors" == computer:
        await ctx.reply("You chose paper.\nThe Bot chose " + computer)
        await ctx.reply("The Bot Won!!")
    else:
        await ctx.reply("You chose paper and the Bot chose " + computer + "\nIt's a tie!!")


@bot.group(with_app_command=True, fallback="rps_scissors")
async def rps_scissors(ctx):
    computer=random.choice(['rock','paper','scissors'])
    if "paper" == computer:
        await ctx.reply("You chose scissors.\nThe Bot chose " + computer)
        await ctx.reply("You Won!!")
    elif "rock" == computer:
        await ctx.reply("You chose scissors.\nThe Bot chose " + computer)
        await ctx.reply("The Bot Won!!")
    else:
        await ctx.reply("You chose scissors and the Bot chose " + computer + "\nIt's a tie!!")

bot.run(TOKEN)
