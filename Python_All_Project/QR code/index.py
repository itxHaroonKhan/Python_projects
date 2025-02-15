
#Today I make Qr code for my project

import qrcode

data = 'https://www.facebook.com/profile.php?id=100046265633534'

img = qrcode.make(data)

img.save("qrcode.png")



#This is the code for the Qr code
