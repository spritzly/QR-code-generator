import qrcode

# by using the QRCode class, you can specify specific details of the qr code

qr = qrcode.QRCode(
    version=None, 
    error_correction=qrcode.constants.ERROR_CORRECT_Q, 
    box_size=10, 
    border=4
)
qr.add_data('data goes here')
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')
img.save('qr_file.png')

'''
- version determines the size of the qr code (can set between 1-40), set to None and
use the fit parameter in qr.make to do this automatically

- error_correction defaults to ERROR_CORRECT_M, which >15% errors corrected,
there's also ERROR_CORRECT_L (>7%), ERROR_CORRECT_Q(>25%), and ERROR_CORRECT_H(>30%)

- box_size determines the number of pixels in the qr code

- border determines how many boxes thick the border should be, default is the 
minimum of 4

- fill_color is the color of the pixels in the qr code, back_color is the color
of the background
'''
