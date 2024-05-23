import os
import requests

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

def get_guild_emojis(token, guild_id):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/emojis'
    headers = {
        'Authorization': f'Bot {token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        emojis = response.json()
        for emoji in emojis:
            print(f"Name: {emoji['name']}, ID: {emoji['id']}")
    else:
        print(f'Failed to retrieve emojis: {response.status_code}, {response.text}')

if __name__ == "__main__":
    if not TOKEN or not GUILD_ID:
        print('Please set the DISCORD_BOT_TOKEN and DISCORD_GUILD_ID environment variables.')
    else:
        get_guild_emojis(TOKEN, GUILD_ID)
