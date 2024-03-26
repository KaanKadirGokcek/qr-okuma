from pyzbar import pyzbar
from PIL import Image

qr =  pyzbar.decode(Image.open('vol1.png'))

print(qr[0].data.decode('ascii'))