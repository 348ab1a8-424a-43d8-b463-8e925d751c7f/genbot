import logging

import discord
from discord.ext import commands

import config
from cogs import list_cogs

# Logger Configuration
logging.basicConfig(
    level=logging.INFO,  # DEBUG for more details
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),     # Writes to a file
        logging.StreamHandler()             # Also logs to the console
    ]
)

logger = logging.getLogger("discord_bot")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        for cog in list_cogs():
            await bot.load_extension(cog)

        # Sync Global Commands
        synced = await self.tree.sync()
        logger.info(f"Synced {len(synced)} global command(s).")

        channel = self.get_channel(1383531643113050142)
        if channel:
            await channel.send("07cab3d6-0d7d initialized successfully.")

bot = MyBot()

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(config.DISCORD_TOKEN)