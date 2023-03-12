import asyncio
from gtts import gTTS


async def convert_text_to_speech(posts):
    async with asyncio.TaskGroup as tg:
        for post in posts:
            tg.create_task(getVoice(post))
