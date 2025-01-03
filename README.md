<div align="center">

# fbchat-muqit

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fbchat-muqit)
![aiohttp - Python Version](https://img.shields.io/pypi/v/aiohttp)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**fbchat-muqit** An Unofficial Facebook Messenger API designed to interact with Facebook and Messenger. It is an early release. Most of the feautures are not available yet. 
As It is Open Unofficial API we are not responsible if you get banned by Facebook. We recommend to use a dummy Facebook account.

</div>

## 🛠️ Installation

You can install fbchat-muqit using pip:

```bash
pip install fbchat-muqit
```

## 📙 Documentation

The API is not fully documented yet [Read Documentation](http://fbchat-muqit.rtfd.io/)

## 📖 Usage Example

A basic example 

```python
import asyncio
from fbchat_muqit import Client

async def main():
    cookies_path = "path to json cookies"
    # Lets login in Facebook
    bot = await Client.startSession(cookies_path)
    if await bot.isLoggedIn():

        """Lets send a Message to a friend when Client is logged in."""

        await bot.sendMessage("I'm Online!", "10000072727288")
        print("Logged in as", bot.uid)
    # listen to all incoming events
    await bot.listen()

asyncio.run(main())

```

Subclassing Client class

```python

from fbchat_muqit import Client, Message, ThreadType
import asyncio
# Create a class use Client as base Class
class Test(Client):

    async def onMessage(self, mid, author_id: str, message_object: Message, thread_id, thread_type=ThreadType.USER, **kwargs):

        """you will receive all messenger messages here every time anyone sends messages in a thread (Group/User)"""
        # author_id is message sender ID
        if author_id != self.uid:
            await message_object.reply("Hello! This is a reply")
            await message_object.react("❤️")
            # mid is message ID
            await self.sendMessage("Hello", thread_id, thread_type, reply_to_id=mid)


async def main():
    cookies_path = "path to json cookies"
    bot = await Test.startSession(cookies_path)
    if await bot.isLoggedIn():
        print("Logged in as", bot_info.uid)

    try:
        await bot.listen()
    except Exception as e:
        print(e)


asyncio.run(main()) 

```

