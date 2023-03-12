import asyncio
from gtts import gTTS
from praw.models import MoreComments


async def get_voice(post):
    text = post.title

    comments = post.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        text += '\n' + comment.body

    tts = gTTS(text=text, lang='en', slow=False, tld='us')
    tts.save(f"{post.id}.mp3")


async def convert_text_to_speech(posts):
    async with asyncio.TaskGroup() as tg:
        for post in posts:
            tg.create_task(get_voice(post))
