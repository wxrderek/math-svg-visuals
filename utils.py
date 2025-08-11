import os

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