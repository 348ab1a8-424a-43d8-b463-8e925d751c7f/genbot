import discord
import config
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()  # Sync global slash commands
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    print("07cab3d6-0d7d initalized successfully")
    channel = bot.get_channel(1383531643113050142)
    await channel.send("07cab3d6-0d7d initalized successfully.")

@bot.command()
async def credits(ctx):
    await ctx.send("Visit https://jto.dev/ for more information.")

async def whoisjto(ctx):
    await ctx.send("An engineer, a father, and duck loving individual.")
    
# Slash command: /hello
@bot.tree.command(name="hello", description="Say hello globally!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}! 👋")

bot.run(config.DISCORD_TOKEN)