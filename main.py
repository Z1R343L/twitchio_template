from os import getenv

from dotenv import load_dotenv
from ruamel.yaml import YAML
from twitchio.ext.commands import Bot, Context, command

load_dotenv()

yaml = YAML()
with open("config.yml", "rb") as f:
    config = yaml.load(f)


class botclass(Bot):
    def __init__(self):
        super().__init__(token=str(getenv("ACCESS_TOKEN")), prefix=config["prefix"])

    async def event_ready(self):
        print(f"Logged in as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        print(message.content)
        await self.handle_commands(message=message)

    @command()
    async def fc(self, ctx: Context):
        await ctx.send(config['fc'])

    @command()
    async def fcbaby(self, ctx: Context):
        await ctx.send(config['fcbaby'])

    @command()
    async def sysbot(self, ctx: Context):
        await ctx.send(config['invite'])


bot = Bot()
bot.run()
