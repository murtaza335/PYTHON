import qrcode as qr
img = qr.make("hey bro whats up ? This qr is geenrated by murtaza using python")
img.save("qrimg.png")