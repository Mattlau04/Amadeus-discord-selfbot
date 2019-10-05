import discord
import sys
import asyncio
from discord.ext import commands

class stfu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False

    @commands.command()
    async def stfu(self, ctx, target: discord.User="None"):
        '''
        React to every message from someone with STFU

        syntax: stfu @useridk#133
        to disable: do stfu without an argument
        '''
        await ctx.message.delete()
        self.enabled = not self.enabled
        if self.enabled:
            if not target == "None":
                await ctx.send("STFU enabled", delete_after=2)
            else:
                await ctx.send("`Error:` Please specify a target", delete_after=3)
                self.enabled = not self.enabled
        else:
            await ctx.send("Disabled STFU", delete_after=2)
        def check(m):
            return m.author == target and self.enabled
        while True:
            msgtoreact = await self.bot.wait_for('message', check=check)
            try:
                await msgtoreact.add_reaction("🇸")
                await asyncio.sleep(0.1)
                await msgtoreact.add_reaction("🇹")
                await asyncio.sleep(0.1)
                await msgtoreact.add_reaction("🇫")
                await asyncio.sleep(0.1)
                await msgtoreact.add_reaction("🇺")
            except Exception as a:
                print(a)

def setup(bot):
    bot.add_cog(stfu(bot))
