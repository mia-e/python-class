import barcode
from barcode.writer import ImageWriter

text = "this is a barcode"
text1 = str(text)
code = barcode.get_barcode_class("code128")
image = code(text, writer=ImageWriter())
save_img = image.save('my final barcode')