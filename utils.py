import os
import random

# ==================== file mechanics ====================

def write_svg(svg_content: str, filename: str='out.svg', dirname: str='sample_svgs'):
    '''Writes text content to .svg file'''

    os.makedirs(dirname, exist_ok=True)
    filepath = os.path.join(dirname, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
    except Exception as e:
        print(f'[ERROR] Error encountered writing file to .svg: {e}')


def build_svg_doc(content: str, width: int=1000, height: int=1000) -> str:
    '''Builds standard svg document around contents'''

    svg_template = f'''<?xml version="1.0" encoding="UTF-8"?> 
        <svg width="{width}" height="{height}" viewBox="0 0 {width} {height}"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink">
        {content}
    </svg>'''

    return svg_template


def set_bg(fill: str='#000000', view_width: int=1000, view_height: int=1000) -> str:
    '''Makes rectangle as generic background if desired'''
    return f'<rect x="0" y="0" width="{view_width}" height="{view_height}" fill="{fill}" />'



# ==================== random color selectors ====================

def random_hex_code(min_rgb=(0,0,0), max_rgb=(255,255,255)) -> str:
    '''Returns random hex code within given range of rgb values'''
    r = random.randint(min_rgb[0], max_rgb[0])
    g = random.randint(min_rgb[1], max_rgb[1])
    b = random.randint(min_rgb[2], max_rgb[2])
    return f"#{r:02X}{g:02X}{b:02X}"


def random_hex_grey(min_grey=0, max_grey=255) -> str:
    '''Returns random hex code on greyscale of given range'''
    n = random.randint(min_grey, max_grey)
    return f"#{n:02X}{n:02X}{n:02X}"