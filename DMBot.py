import discord

# Replace with your own Discord bot token
TOKEN = "your-bot-token-goes-here"

# Replace with the ID of the server you want to send messages to
SERVER_ID = "server-id-goes-here"

# Replace with the message you want to send
MESSAGE = "Hello, everyone! I'm a bot, and I'm here to say hello!"

client = discord.Client()

@client.event
async def on_ready():
    server = client.get_guild(SERVER_ID)

    # Get a list of all members in the server
    members = server.members

    # Send the message to each member
    for member in members:
        await member.send(MESSAGE)

    # Disconnect the bot
    await client.close()

client.run(TOKEN)
