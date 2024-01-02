import os
import discord
from dotenv import load_dotenv

load_dotenv()
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


ROLE_MESSAGE_ID = int(os.getenv("ROLE_MESSAGE_ID"))
REACTION = os.getenv("REACTION")
ROLE = os.getenv("ROLE")


intents = discord.Intents.default()
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == ROLE_MESSAGE_ID and payload.emoji.name == REACTION:
        guild = bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=ROLE)
        await payload.member.add_roles(role)
        
@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == ROLE_MESSAGE_ID and payload.emoji.name == REACTION:
        guild = bot.get_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = discord.utils.get(guild.roles, name=ROLE)
        await member.remove_roles(role)


api_key = os.getenv("API_KEY")
bot.run(api_key)
