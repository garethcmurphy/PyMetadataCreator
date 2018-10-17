#!/usr/bin/env python3
import base64


class Base64Im:
    def __init__(self):
        self.header = "data:image/png;base64,"
        with open("raw_data_3D_detectors.png", "rb") as image_file:
            data = image_file.read()
            image_bytes = base64.b64encode(data)
            image_str = image_bytes.decode('UTF-8')
            self.im = self.header + image_str


if __name__ == '__main__':
    b = Base64Im()
    print(b.im)
