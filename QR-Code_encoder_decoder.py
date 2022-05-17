import qrcode

data = "" #Here you will insert any data that you want your qr code to contain. It can be a website, message, etc. 

img = qrcode.make(data)

img.save() #insert the destination of where you want your qr codes saved here, be sure to include .png to the location to create the image.

from pyzbar.pyzbar import decode
from PIL import image

img = image.open('') #Here you will input the location of the file where you created the encoded qr code image. 

result = decode(img)

result(result)