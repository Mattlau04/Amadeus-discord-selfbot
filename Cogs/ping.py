import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        '''
        Pong! Get the bot latency with this command.
        '''

        latency = self.bot.latency
        await ctx.send("Pong! `" + str(int(latency * 100)) + "ms`")

def setup(bot):
    bot.add_cog(ping(bot))
