import discord
from discord import app_commands
from discord.ext import commands


TOKEN = ""

with open("TOKEN.txt", "r") as file:
    TOKEN = file.readline()




class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="^", intents=intents)
    async def setup_hook(self):
        await self.tree.sync(guild=discord.Object(id=1032832201211007046))

bot = Bot()

#tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.hybrid_command(with_app_command=True)
async def test(ctx):
    await ctx.send("Hybrid command")


bot.run(TOKEN)