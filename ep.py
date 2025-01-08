from __future__ import annotations

from fbchat_muqit import Client, Message, ThreadType, ThreadLocation
import asyncio

class Test(Client):
    async def onMessage(self, author_id, thread_id, message_object, **kwargs):

        print(message_object)
        if author_id != self.uid:
            await message_object.reply("Hi")
    async def onReply(self, mid: str, author_id: str, message: str, message_object: Message, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        print(message_object)

async def main():
    cookies_path = "../c.json"
    bot = await Test.startSession(cookies_path)
    if await bot.isLoggedIn():
        print("Logged in as", bot.uid)
    try:
        await bot.listen()
    finally:
        await bot.stopListening()



asyncio.run(main())
