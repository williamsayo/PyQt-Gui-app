from PIL import Image
import os

cwd = os.path.split(__file__)[0]
media = os.path.join(cwd,'media')

image = Image.open(os.path.join(media,"profile_pics/default.jpg"))

new_height = 50

new_width = int(new_height/image.height * image.width)

image.thumbnail((new_width,new_height))
image.save(os.path.join(media,"profile_pics/default1.png"))