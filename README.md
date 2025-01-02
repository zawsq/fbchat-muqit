<div align="center">

# fbchat-muqit

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fbchat-muqit)

**fbchat-muqit** An Unofficial Facebook Messenger API designed to interact with Facebook and Messenger. It is an early release. Most of the feautures are not available yet. 
As It is Open Unofficial API we are not responsible if you get banned by Facebook. We recommend to use a dummy Facebook account.

</div>

## 🛠️ Installation

You can install fbchat-muqit using pip:

```bash
pip install fbchat-muqit
```

## Documentation

The API is not Documented yet. However, It's design is similar to fbchat v1.9.7
So you can look at [fbchat documentation](https://fbchat.readthedocs.io/en/stable/) until we release our Documentation for fbchat-muqit. While following fbchatv1.9.7 remember that fbchat-muqit is an asynchronous library while fbchat is synchronous.


## 📖 Usage Example

Some basic examples

```python

from fbchat_muqit import Client, Message, ThreadType
import asyncio

# Create a class use Client as base Class
class Test(Client):
    async def onListening(self): #type: ignore
        print("I'm Listening")

    async def onMessage(self, mid, author_id: str, message: str, message_object: Message, thread_id, thread_type=ThreadType.USER, **kwargs):
        """you will rec"""

        # author_id is message sender ID
        if author_id != self.uid:
            await message_object.reply("Hello! This is a reply")
            await message_object.react("❤️")
            # mid is message ID
            await self.sendMessage("Hello", thread_id, thread_type, reply_to_id=mid)

    async def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
        # `added_ids` is a list of uid of the added people
        thread_type = ThreadType.GROUP
        mention = added_ids
        if self.uid not in added_ids:
            await self.sendMessage("Welcome to the Group!", thread_id, thread_type, mentions=mention)

    # There a lot of methods available

async def main():
    cookies_path = "./c.json"
    bot = await Test.startSession(cookies_path)
    if await bot.isLoggedIn():
        # fetch bot account
        fetch_bot = await bot.fetchUserInfo(bot.uid) # retuens dict {id: User}

        bot_info = fetch_bot[bot.uid] # access `User` object

        print("Logged in as", bot_info.name)

    try:
        await bot.listen()
    except Exception as e:
        print(e)


asyncio.run(main())


```

