import os
import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    guild = discord.utils.get(bot.guilds, id=int(GUILD_ID))
    channel = discord.utils.get(guild.text_channels, id=int(CHANNEL_ID))
    
    poll_question = "What's your favorite color?"
    poll_answers = [
        {'text': 'Red', 'emoji': '🔴'},
        {'text': 'Blue', 'emoji': '🔵'},
        {'text': 'Green', 'emoji': '🟢'}
    ]

    poll_message = f"**{poll_question}**\n"
    for i, answer in enumerate(poll_answers):
        poll_message += f"{answer['emoji']} {answer['text']}\n"

    message = await channel.send(poll_message)
    for answer in poll_answers:
        await message.add_reaction(answer['emoji'])

    await bot.close()

bot.run(TOKEN)
