import qrcode


class CreateMessage:
    def __init__(self):
        self.phonenumbers = None
        self.message = None




phonenumbers = "+46739989135, +46721616183"
message = "det funkar!!! Jag har precis skrivit en app som typ skapar ett sms!"
# payload = f"smsto:{phonenumbers}:{message}"
payload = "smsto:+46123456789, +46234567891:this is where I wrote the message"

# https://pypi.org/project/qrcode/
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(payload)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.show()
# img.save("image.jpg")
