import os
import requests
from datetime import datetime, timedelta, timezone

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

# Poll Create Request Object
poll_question = {
    'text': "今日行かれますか？",
}
poll_answers = [
    {'answer_id': 1, 'poll_media': {'text': 'はやめいき', 'emoji': {'name': 'sourou', 'id': '1219550208057282620'}}},
    {'answer_id': 2, 'poll_media': {'text': 'おそめいき', 'emoji': {'name': 'chirou', 'id': '1219550492162785300'}}},
    {'answer_id': 3, 'poll_media': {'text': 'きびし', 'emoji': {'name': 'intai', 'id': '1219548466628399174'}}},
    {'answer_id': 4, 'poll_media': {'text': 'いきため', 'emoji': {'name': 'ikitame', 'id': '1244834251241816156'}}}
]
duration_hours = 24  # Poll duration in hours
allow_multiselect = False
layout_type = 1

# Expiry time
expiry_time = (datetime.now(timezone.utc) + timedelta(hours=duration_hours)).isoformat()

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
    'poll': poll_request
}

response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages', json=data, headers=headers)

if response.status_code == 200:
    print('Poll created successfully')
else:
    print(f'Failed to create poll: {response.status_code}, {response.text}')
