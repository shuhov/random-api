import os
import sys
from io import StringIO

import pyotp
from PIL import Image, ImageDraw
import numpy as np
from flask import send_file
from flask_restplus import Resource

from random_api.api.resources.images import ns_images


@ns_images.route("")
class BaseImage(Resource):

    def get(self):
        arr = np.random.randint(0,255,(100,100,3), dtype='uint8')
        image = Image.fromarray(arr, 'RGB')
        image.seek(0)

        output = StringIO()
        image.save(output, format="PNG")
        return send_file(output, mimetype='image/png')


@ns_images.route("otp_list")
class OTPImage(Resource):

    def get(self):
        secret = pyotp.random_base32()
        hotp = pyotp.HOTP(secret, digits=8)
        codes = []
        for i in range(10):
            codes.append(hotp.at(int.from_bytes(os.urandom(2), sys.byteorder)))

        image = Image.new('RGB', (480, 240), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        x, y = 50, 50
        first_line = x
        for i, code in enumerate(codes):
            if i == 5:
                y = first_line
                x += 200
            draw.text((x, y), "{}. {}".format(i, code), (0, 0, 0))
            y += 30


        output = StringIO()
        image.save(output, format="PNG")
        return send_file(output, mimetype='image/png')
