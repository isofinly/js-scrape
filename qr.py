import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
link = open('one-pastvu-links.txt', 'r').readlines()
for i in range(len(link)):
    data = link[i]
    qr.add_data(f'{data}')
    img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
    with open(f'qr_codes/qr{i}.png', 'wb') as f:
        img_1.save(f, 'PNG')
    qr.clear()