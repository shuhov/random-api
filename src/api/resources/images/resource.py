import os
import sys

import pyotp
from PIL import Image, ImageDraw, ImageFont

from flask_restplus import Namespace, Resource

api = Namespace('images', description='Random images')


class OTPImage(Resource):

    def get(self):
        name = 'otp_image'
        secret = pyotp.random_base32()
        hotp = pyotp.HOTP(secret, digits=8)
        codes = []
        for i in range(10):
            codes.append(hotp.at(int.from_bytes(os.urandom(2), sys.byteorder)))

        img = Image.new('RGB', (480, 240), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-BI.ttf", size=30)
        x, y = 50, 50
        first_line = x
        for i, code in enumerate(codes):
            if i == 5:
                y = first_line
                x += 200
            draw.text((x, y), "{}. {}".format(i, code), (0, 0, 0), font=font)
            y += 30
        abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files/sample.jpg')
        img.save(abs_path)
        return dict(name=name, path=abs_path), 200
