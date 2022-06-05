import os
from pathlib import Path
import random
from typing import Tuple
from random import randint

import sys

import unix_fonts

from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)

OUTPUT_PATH = "output/"
BACKGROUND = (24, 24, 24)
SIZE = (400, 400)
CENTER = (SIZE[0] / 2, SIZE[1] / 2)
MIN_AVOIDANCE = 32

items = sys.argv[1:]


def get_center(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return ((b[0] - a[0]) / 2 + a[0], (b[1] - a[1]) / 2 + a[1])


def gray(color: Tuple[int, int, int]) -> int:
    return (color[0] + color[1] + color[2]) / 3


def get_random_color(avoid: Tuple[int, int, int]) -> Tuple[int, int, int]:
    while True:
        col = (randint(0, 255), randint(0, 255), randint(0, 255))
        if gray(col) >= MIN_AVOIDANCE:
            return col


if not os.path.isdir(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)


for i in range(10):
    with Image.new("RGB", SIZE) as image:
        image.paste(BACKGROUND, (0, 0, SIZE[0], SIZE[1]))

        draw = ImageDraw.Draw(image, "RGB")

        for item in items:
            font = ImageFont.truetype(
                unix_fonts.get_random_font(), random.randint(16, 32)
            )
            pos = (randint(0, SIZE[0]), randint(0, SIZE[1]))
            draw.text(
                pos, item, get_random_color(BACKGROUND), align="center", font=font
            )

        image.save(os.path.join(OUTPUT_PATH, "image_%d.png" % i))
