import glob
import random
from typing import Tuple


def get_unix_fonts() -> Tuple[str]:
    return glob.glob("/usr/share/fonts/*/*.otf", recursive=True)


def get_random_font() -> str:
    return random.choice(get_unix_fonts())
