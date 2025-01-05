import os
import discord

class MyBot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyBot(intents=intents)
    client.run(os.getenv("DISCORD_BOT_TOKEN"))

