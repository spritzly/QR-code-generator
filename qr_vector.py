import qrcode
import qrcode.image.svg

#used to create svg instead of png, can still edit using the QRCode class as seen in qr_specifics.py
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make('Data goes here', image_factory=factory)
svg_img.save("qr_vector.svg")