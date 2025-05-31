from PIL import Image
mac=Image.open('my_com_image.jpg')
#It represent the imag
print(type(mac.show()))
#it reprsent the ht and wd
print(mac.size)
#it rep the file name
print(mac.filename)
# Extra info of img
print(mac.format_description)
