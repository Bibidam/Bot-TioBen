from discord.ext.commands import Bot
from discord import Game
from discord import File
import random


BOT_PREFIX = ("mestre ","Mestre ")
BOT_TOKEN = "NjAzNDUxNzc0MzA4NzEyNDU5.XTlpfw.0zi8WXv3mMLuamvXzDVPhUZ99oc"

client = Bot(command_prefix=BOT_PREFIX)

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

@client.event
async def on_ready():
    activity = Game(name="Dando conselhos ao Peter")
    await client.change_presence(activity=activity)
    print("Logged in as "+client.user.name)

client.run(BOT_TOKEN)