#CROPPING IMG
# print(mac.crop((100,0,1000,1000)))
from PIL import Image
pencils=Image.open('Pencils.jpeg')
# print(pencils.show())
# print(pencils.size())
# x=0
# y=0
# w=1950/3
# h=1300/10
# print(pencils.crop((x,y,w,h)))
red=Image.open('red_color.jpeg')
red.putalpha(128)
# print(red.show())
blue=Image.open('blue.jpeg')
# print(blue.show())
#MIXING BOTH
blue.paste(im=red,box=(0,0),mask=red)
print(blue.show())