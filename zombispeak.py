import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = 'z!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, '**Gratulacje! Dolaczyles na serwer:** ***ZombieSpeak***! **Milej zabawy :D**')
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Moderowanie czatu :)'))
    print('Działa')
     
@client.event
async def on_message(message):
    if message.content.startswith('Siema bot'):
        await client.send_message(message.channel,'Cześć <@%s>!'  %(message.author.id))
    if message.content.startswith('siema Bot'):
        await client.send_message(message.channel,'Cześć <@%s>!'  %(message.author.id))
    if message.content.startswith('siema bot'):
        await client.send_message(message.channel,'Cześć <@%s>!'  %(message.author.id))
    if message.content.startswith('Masno'):
        randomlist = ["Fest","Ni"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('masno'):
        randomlist = ["Fest","Ni"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'Kurła':
        await client.send_message(message.channel,'Kuuuurła kiedyś to było...')
    if message.content == 'kurła':
        await client.send_message(message.channel,'Kuuuurła kiedyś to było...')
    if message.content == 'kurla':
        await client.send_message(message.channel,'Kuuuurła kiedyś to było...')
    if message.content == 'Kurla':
        await client.send_message(message.channel,'Kuuuurła kiedyś to było...')
    if ('kurwa') in message.content:
       await client.delete_message(message)
    if ('japierdole') in message.content:
       await client.delete_message(message)
    if ('chuj') in message.content:
       await client.delete_message(message)
    if ('huj') in message.content:
       await client.delete_message(message)
    if ('kurwo') in message.content:
       await client.delete_message(message)
    if ('Kurwa') in message.content:
       await client.delete_message(message)
    if ('Japierdole') in message.content:
       await client.delete_message(message)
    if ('Ja pierdole') in message.content:
       await client.delete_message(message)
    if ('ja pierdole') in message.content:
       await client.delete_message(message)
    if ('Chuj') in message.content:
       await client.delete_message(message)
    if ('Huj') in message.content:
       await client.delete_message(message)
    if ('Kurwo') in message.content:
       await client.delete_message(message)
    if ('KURWA') in message.content:
       await client.delete_message(message)
    if ('JAPIERDOLE') in message.content:
       await client.delete_message(message)
    if ('CHUJ') in message.content:
       await client.delete_message(message)
    if ('HUJ') in message.content:
       await client.delete_message(message)
    if ('KURWO') in message.content:
       await client.delete_message(message)     
client.run(str(os.environ.get('NTI5NjkwOTE0NDcwNDk0MjM4.Dw0gyA.7pyD13NIE6lIk4zJ5y0tH49IvKs')
