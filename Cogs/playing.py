import discord
from discord.ext import commands

class playing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playing(self, ctx, *args):
        '''
        Change what game you're playing
        '''
        await ctx.message.delete()
        playgame = ' '.join(args)
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=playgame))
        await ctx.send("Changed playing status to `" + playgame + "`.", delete_after=5)

def setup(bot):
    bot.add_cog(playing(bot))
