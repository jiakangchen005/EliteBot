import os
import sys
from asyncio import sleep

import discord
from discord.ext import commands, tasks

from live import live

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '$', help_command = None, intents = intents)

token = os.environ['token']

# Start of Bot

allowed = [374691272109195264, 689600423832846366, 202905689146785792, 503308833813299221]
current = -1
mention = None

@client.event
async def on_ready():
	status = discord.Activity(name = "netstat", type = 3)
	await client.change_presence(activity = status)
		
	print("yey")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		if current in allowed:
			await ctx.send(f"<@{current}> Access Denied.")
		else:
			await ctx.send(f"<@{current}> You Do Not Acquire The Privileges To Perform Any Actions. I Boldly Advise You To Acknowledge Your Nefarious Actions And The People You Are Opposing. Let This Message Only Be A Peaceful Cautionary, And Not An Ultimatum.")

def elite(ctx):
	global current
	current = ctx.author.id
	return ctx.author.id == 510116322722447360

@client.command()
@commands.check(elite)
async def kill(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason = reason)
		
@client.command()
@commands.check(elite)
async def pkill(ctx, member : discord.Member, *, reason = None):
	await member.ban(reason = reason)

@client.command()
@commands.check(elite)
async def whois(ctx, member: discord.Member):  
  result = discord.Embed(title = "User Search", url = member.avatar_url, description = f"Results for {member}.", color = discord.Color.blue())
  
  result.set_thumbnail(url = member.avatar_url)
  
  result.add_field(name = "Username", value = f"`{member}`", inline = False)

  result.add_field(name = "User ID", value = f"`{member.id}`", inline = False)

  join = member.created_at.strftime("%b %d, %Y")
  result.add_field(name = "Account Creation Date", value = f"`{join}`", inline = False)
  
  await ctx.send(embed = result)

# End of Bot

live()
client.run(token)
