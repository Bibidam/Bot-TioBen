from discord.ext.commands import Bot
from discord import Game
from discord import File
import discord
import random


BOT_PREFIX = ("mestre ","Mestre ")
BOT_TOKEN = "NjAzNDUxNzc0MzA4NzEyNDU5.XTlrMQ.ENN_VqjRo3Av8FuoLtkhYgl126Y"

client = Bot(command_prefix=BOT_PREFIX)

client.remove_command("help")
@client.command(pass_context=True)
async def dale(context):
    possible_responses = [
        'Fala chupinga',
        'Eae meu nobre',
        'Fala meu consagrado',
        'O que é mizera',
        'Fala arrombado',
        'Oi bb'
    ]
    await context.send(random.choice(possible_responses))

@client.command(pass_context=True)
async def mimimi(context,arg):
    try :
        from PIL import Image
        from PIL import ImageFont
        from PIL import ImageDraw 
        print(arg)
        texto = "MiMiMi " + arg
        max_len = 30
        img = Image.open("memes/meme1.png")
        width, height = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("fonts/impact/unicode.impact.ttf", 35)
        size_text = len(texto.lstrip())*8
        draw.text(((width/2)-size_text, height-70),texto[:max_len],font=font)
        img = img.convert("RGB")
        img.save('result.png')
        with open('result.png', 'rb') as picture:
            await context.send(file=File(picture,"result.png"))
    except:
        pass

@client.command(pass_context=True)
async def help(context):
    author = context.message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name="dale", value="Retorna uma saudação aletoria", inline=False)
    embed.add_field(name="mimimi", value="Retorna um meme Mimimi, ex : mestre mimimi \"biscoito não é bolacha\"", inline=False)
    await context.send(author,embed=embed)


@client.event
async def on_ready():
    activity = Game(name="Dando conselhos ao Peter")
    await client.change_presence(activity=activity)
    print("Logged in as "+client.user.name)

client.run(BOT_TOKEN)