from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("img.png")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("comic.ttf", 100)

text = input("Text :")

W, H = img.size
w, h = draw.textsize(text, font=font)

draw.text(((W - w) / 2, (H - h) / 2), text, (255, 255, 255), font=font)

img.show()