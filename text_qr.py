import qrcode
#most basic use, pulls up text and looks it up on search engine
img = qrcode.make("Your text here")
img.save("file_name.png")
