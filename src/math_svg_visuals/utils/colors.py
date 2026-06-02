import random

def random_hex(min_rgb=(0,0,0), max_rgb=(255,255,255)) -> str:
    '''Returns random hex code within given range of rgb values'''
    r = random.randint(min_rgb[0], max_rgb[0])
    g = random.randint(min_rgb[1], max_rgb[1])
    b = random.randint(min_rgb[2], max_rgb[2])
    return f"#{r:02X}{g:02X}{b:02X}"


def random_hex_grey(min_grey=0, max_grey=255) -> str:
    '''Returns random hex code on greyscale of given range'''
    n = random.randint(min_grey, max_grey)
    return f"#{n:02X}{n:02X}{n:02X}"