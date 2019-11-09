import os
import discord
from dotenv import load_dotenv

from src.api.ApiHelper import ApiHelper
from src.helper.parser import RpiArgumentParser


class RpiDiscordBot(discord.Client):
    def __init__(self):
        load_dotenv()
        self.BOT_CHANNEL = os.getenv('BOT_CHANNEL')

        self.API_HELPER = ApiHelper()
        self.PARSER = RpiArgumentParser()

        super(RpiDiscordBot, self).__init__()

    async def on_ready(self):
        for guild in client.guilds:
            for member_id, channel in guild._channels.items():
                if channel.name == self.BOT_CHANNEL:
                    await channel.send('I am online!')
            for member_id, member in guild._members.items():
                if not member.bot:
                    print(f'no bot {member}')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.channel.type.name == 'private' or self.user in message.mentions:
            try:
                cmd, args = self.PARSER.parse_arguments(message.content)
                response = self.API_HELPER.do_command(cmd, args)
            except NotImplementedError as e:
                response = str(e)

            await message.channel.send(response)


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
client = RpiDiscordBot()
client.run(TOKEN)
