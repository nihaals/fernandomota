roleID = 0
serverID = 0

import discord
from discord.ext import commands
import asyncio

assert discord.__version__ == "1.0.0a"

bot = commands.Bot(command_prefix=prefixes)

@bot.event
async def on_ready():
    print("Logged in as:")
    print("Name: " + str(bot.user))
    print("ID: " + str(bot.user.id))
    print(datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S UTC"))

bot.loop.create_task(self.streamLoop())

async def streamLoop():
    def roleHandler(member):
        activity = member.activity
        if isinstance(activity, discord.Streaming):
            for role in member.roles:
                if role.id == roleID:
                    return 0
            return 1

        else:
            for role in member.roles:
                if role.id == roleID:
                    return -1
            return 0

    await self.bot.wait_until_ready()
    await asyncio.sleep(1)
    while True:
        server = bot.get_guild(serverID)
        if not server:
            print("Server not found!")
            exit()

        role = discord.utils.get(server.roles, id=roleID)
        if not role:
            print("Role not found!")
            exit()

        for member in server.members:
            r = roleHandler(member)
            if r == 1:
                await member.add_roles(role)
            elif r == -1:
                await member.remove_roles(role)

        await asyncio.sleep(60)

bot.run(token)
