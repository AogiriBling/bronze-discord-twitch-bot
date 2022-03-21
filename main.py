import discord
from discord.ext import commands
from discord.utils import get
from webserver import keep_alive

import os


my_secretToken = os.environ['TOKEN']

intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
  print(f'Loged in as {bot.user}\n')



#--- bronze ---
@bot.command()
async def bronze(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> /bronze')
    auth = ctx.author
    member = ctx.guild.get_member(ctx.author.id)
    await ctx.send("__**Make sure `discord.gg/freefollowers` is in your status to claim!**__")
    
    for status in member.activities:
        if isinstance(status, discord.CustomActivity):
            if status.name != 'discord.gg/freefollowers':
                    await ctx.message.delete()
                    embed = discord.Embed(color=000000, description="You need to set your status to 'discord.gg/freefollowers'")
                    embed.set_author(name=f'{ctx.guild.name} | Bronze', icon_url='<@&930633377781022761>')
                    await ctx.send(embed=embed)
            else:
                if status.name == 'discord.gg/freefollowers':
                    role = discord.utils.get(ctx.guild.roles, name="B-Rated Ghoul")
                    user = ctx.message.author
                    await user.add_roles(role)
                    embed = discord.Embed(color=000000, description=f"I Have Successfully Given You <@&930633377781022761> {member.mention}")
                    embed.set_author(name=f'{ctx.guild.name} | Bronze', icon_url='https://i.vgy.me/jX7T5Z.png')
                    await ctx.send(embed=embed)

@bot.event
async def on_member_update(before, after):
    role = get(before.guild.roles, name="B-Rated Ghoul")
    if 'discord.gg/freefollowers' in str(before.activities):
      if 'discord.gg/freefollowers' in str(after.activities):
        pass
      else:
        await after.remove_roles(role)

keep_alive()
bot.run(my_secretToken)
