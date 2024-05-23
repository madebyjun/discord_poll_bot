import os
import requests
from datetime import datetime, timedelta

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

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
expiry_time = (datetime.utcnow() + timedelta(hours=duration_hours)).isoformat()

poll_request = {
    'question': poll_question,
    'answers': poll_answers,
    'expiry': expiry_time,
    'allow_multiselect': allow_multiselect,
    'layout_type': layout_type,
}

headers = {
    'Authorization': f'Bot {TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    'poll': poll_request,
    'content': f"**{poll_question['text']}**\n" +
               '\n'.join([f"{answer['poll_media']['emoji']} {answer['poll_media']['text']}" for answer in poll_answers])
}

response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages', json=data, headers=headers)

if response.status_code == 200:
    print('Poll created successfully')
else:
    print(f'Failed to create poll: {response.status_code}, {response.text}')
