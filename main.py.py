import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("coding with Evan")
qr.png("mycode.png", scale=8)

d = decode(Image.open("mycode.png"))
print(d[0].data.decode("Priyanshu"))