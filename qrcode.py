import qrcode as qr

features = qr.QRCode(verison=1,box_size=40,border=3)
features.add_data('https://www.youtube.com')
features.make(fit=True)
img = features.make(fill_color="black",back_color="white")
img.save("qr_img.png")