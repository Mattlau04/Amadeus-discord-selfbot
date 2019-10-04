import discord
from discord.ext import commands

class stfu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False

    @commands.command()
    async def clone(self, ctx, target: discord.User):
        '''
        Pong! Get the bot latency with this command.
        '''

        latency = self.bot.latency
        await ctx.send("Pong! `" + str(int(latency * 100)) + "ms`")

def setup(bot):
    bot.add_cog(stfu(bot))
