from __future__ import annotations

from fbchat_muqit import Client, Message, ThreadType
import asyncio

class Test(Client):
    async def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        await self.markAsReadAll()
        if author_id != self.uid:
            await self.sendLocalFiles("../long_hair.jpg", "A picture for you.", thread_id, thread_type)



async def main():
    cookies_path = "../c.json"
    bot = await Test.startSession(cookies_path)
    if await bot.isLoggedIn():
        print("Logged in as", bot.uid)
    try:
        await bot.listen()
    except Exception as e:
        raise e



asyncio.run(main())
