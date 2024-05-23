import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容の取得を有効にする
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    guild = discord.utils.get(bot.guilds, id=int(GUILD_ID))
    if guild is None:
        print(f'Guild with ID {GUILD_ID} not found.')
        await bot.close()
        return

    channel = discord.utils.get(guild.text_channels, id=int(CHANNEL_ID))
    if channel is None:
        print(f'Channel with ID {CHANNEL_ID} not found.')
        await bot.close()
        return

    # Poll Create Request Object
    poll_question = {
        'text': "What's your favorite color?",
    }
    poll_answers = [
        {'answer_id': 1, 'poll_media': {'text': 'Red', 'emoji': '🔴'}},
        {'answer_id': 2, 'poll_media': {'text': 'Blue', 'emoji': '🔵'}},
        {'answer_id': 3, 'poll_media': {'text': 'Green', 'emoji': '🟢'}}
    ]
    duration_hours = 24  # Poll duration in hours
    allow_multiselect = False
    layout_type = 1

    # Expiry time
    expiry_time = datetime.utcnow() + timedelta(hours=duration_hours)

    poll_message = f"**{poll_question['text']}**\n"
    for answer in poll_answers:
        poll_message += f"{answer['poll_media']['emoji']} {answer['poll_media']['text']}\n"

    message = await channel.send(poll_message)
    for answer in poll_answers:
        await message.add_reaction(answer['poll_media']['emoji'])

    await bot.close()

bot.run(TOKEN)
