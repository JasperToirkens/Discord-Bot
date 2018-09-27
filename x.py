import discord
from discord.ext import commands

TOKEN = 'NDg2NzUxMTQwNzA1MjA2MzAy.DnGFHA.bpzm2uWK0zkqOjEaJ1x58GqYbE0'

client = commands.Bot(command_prefix = '&')

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('&kabouterplop'):
        await client.send_message(channel, 'kabouterplop is gay!')
    
    if message.content.startswith('&frikadel'):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await client.send_message(channel, output)

client.run(TOKEN)