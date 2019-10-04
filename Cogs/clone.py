try: #import default dependencies
    import sys
    import subprocess
    import os
except Exception as p:
    print(p)

import discord
from discord.ext import commands

class clone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clone(self, ctx, clonned: discord.User):
        '''
        Clone your account based on someone elses

        syntax: clone @useridk#1337
        '''
        try:
            await ctx.message.delete()
        except Exception as w:
            print(w)
        try:
            avatar = await clonned.avatar_url_as(format='png', size=2048).read()
        except Exception as m:
            print(m)
        try:
            await self.bot.user.edit(password=self.bot.password, username=clonned.name, avatar=avatar)
            await ctx.send("Enjoy your new identity :wink:", delete_after=7)
        except Exception as j:
            if "You are changing your username or Discord Tag too fast. Try again later." in str(j):
                await ctx.send("`Error:` You are changing your username too fast", delete_after=7)
            else:
                print(str(j))
                await ctx.send("An error occured, check console for more details")

    @clone.error
    async def clone_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument: `User to clone`", delete_after=5)
        else:
            print(error)

def setup(bot):
    bot.add_cog(clone(bot))
