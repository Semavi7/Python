import pyqrcode
from PIL import Image

qr_kod = pyqrcode.create("https://www.dencertenkin.com")

cikti = "qr_kod.png"
qr_kod.png(cikti, scale=10)

cerceve = Image.open(cikti)

cerceve.show()