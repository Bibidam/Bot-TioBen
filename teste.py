from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

msg_recive = "dale boy"
texto = "MiMiMi " + msg_recive
max_len = 30
img = Image.open("memes/meme1.png")
width, height = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("fonts/impact/unicode.impact.ttf", 35)
# font = ImageFont.load("fonts/impact/unicode.impact.ttf")
size_text = len(texto.lstrip())*8
print(size_text)
draw.text(((width/2)-size_text, height-70),texto[:max_len],font=font)
img = img.convert("RGB")
img.save('result.png')