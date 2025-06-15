import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # PREFIX COMMANDS

    # APPLICATION COMMANDS / SLASH COMMANDS
    @discord.app_commands.command(name="hello", description="Greet the bots who greets you!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi {interaction.user.mention}! 👋")

    @discord.app_commands.command(name="credits", description="Information about the developer.")
    async def credits(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{self.bot.user} was created by Johnny To."
         + " For more information, visit https://jto.dev/")

async def setup(bot):
    await bot.add_cog(Misc(bot))
