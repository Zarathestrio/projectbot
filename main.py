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


@bot.group(with_app_command=True, fallback="rps")
async def rps(ctx, arg):
    computer=random.choice(['rock','paper','scissors'])
    if arg == "rock":
        if "scissors" == computer:
            await ctx.reply("You chose rock.\nThe Bot chose " + computer)
            await ctx.reply("You Won!!")
        elif "paper" == computer:
            await ctx.reply("You chose rock.\nThe Bot chose " + computer)
            await ctx.reply("The Bot Won!!")
        else:
            await ctx.reply("You chose rock and the Bot chose " + computer + "\nIt's a tie!!")
    elif arg == "paper":
        if "rock" == computer:
            await ctx.reply("You chose paper.\nThe Bot chose " + computer)
            await ctx.reply("You Won!!")
        elif "scissors" == computer:
            await ctx.reply("You chose paper.\nThe Bot chose " + computer)
            await ctx.reply("The Bot Won!!")
        else:
            await ctx.reply("You chose paper and the Bot chose " + computer + "\nIt's a tie!!")
    elif arg == "scissors":
        if "paper" == computer:
            await ctx.reply("You chose scissors.\nThe Bot chose " + computer)
            await ctx.reply("You Won!!")
        elif "rock" == computer:
            await ctx.reply("You chose scissors.\nThe Bot chose " + computer)
            await ctx.reply("The Bot Won!!")
        else:
            await ctx.reply("You chose scissors and the Bot chose " + computer + "\nIt's a tie!!")
    else:
        await ctx.reply(arg + " is not a valid option!")

@bot.group(with_app_command=True, fallback="commands")
async def commands(ctx):
    embed=discord.Embed(title=f"Commands", description=f"1.\t^initialize: This initializes the bot in your server and begins monitoring for activity!"
    + "\n\n2.\t^rps 'choice': Play Rock Paper Scissors against the bot! Following the command, type your selection to play!"
    + "\n\n3.\t^roll 'number of sides': Choose how many sides are on a dice roll! Following the command, type the amount of sides you want on your die."
    + "\n\n4.\t^countLetters: Count the amount of letters in a word! Following the command type the word you want counted."
    + "\n\n5.\t^userAge: This command tells the user how old their discord account is."
    + "\n\n6.\t^gtn: This is a mini game where you must guess the number (1-50) the bot chooses. Following the command type your guess."
    + "\n\n7.\t^m8b: Think of a question in your head and the Magic 8 Ball will give you your answer!"
    + "\n\n8.\t^coinflip: Flip a coin using this command.")
    await ctx.send(embed=embed)


@bot.group(with_app_command=True, fallback="gtn")
async def gtn(ctx, arg):
    arg = int(arg)
    computer = random.randrange(1,50)
    if arg == computer:
        await ctx.reply("You guessed " + str(arg) + ".\nYou correctly guessed the same number the Bot chose!!")
    else:
        await ctx.reply("You guessed " + str(arg) + ".\nYou did not guess the correct number (" + str(computer) + "). Try again!")

@bot.group(with_app_command=True, fallback="m8b")
async def m8b(ctx):
    computer=random.choice(['It is certain','It is decidedly so.','Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
    'Most likely.', 'Outlook is good.', 'Yes', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you.', 'Cannot predict now.', 
    'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook is not so good.', 'Very doubtful.'])
    await ctx.reply(computer)

@bot.group(with_app_command=True, fallback="coinflip")
async def coinflip(ctx):
    bot = random.choice(['heads!', 'tails!'])
    await ctx.reply("You flipped a coin and it landed on " + bot)



bot.run(TOKEN)
