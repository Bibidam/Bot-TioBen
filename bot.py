import discord

client = discord.Client()

@client.event  
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event 
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == client.user.id:
        return

    if message.content.lower().startswith('mestre'):
        frase = message.content[6:].strip()
        print(frase)
        if frase.lower().startswith('dale') or frase.lower().startswith('eae') :                        
            await message.channel.send('Dale {0.author.mention} chupinga!'.format(message))

client.run("NjAzNDUxNzc0MzA4NzEyNDU5.XTfn5Q.oXoexrsQNabSHkljZKFTSTtlgf8")