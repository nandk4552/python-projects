import pyqrcode
import png

from pyqrcode import pyqrcode

QRstr = "https://www.instagram.com/_.nandu_k/	" #url

url = pyqrcode.create(QRstr)
url.png('/root/qr.png',scale=8)