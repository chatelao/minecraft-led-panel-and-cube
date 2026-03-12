import json
import os
import string
from PIL import Image

def get_alias(index):
    """Generate aliases like A, B, ..., Z, AA, AB, ..."""
    chars = string.ascii_uppercase
    result = ""
    while index >= 0:
        result = chars[index % 26] + result
        index = index // 26 - 1
    return result

def process_image(filepath):
    img = Image.open(filepath).convert('RGBA')
    img = img.resize((32, 32), Image.NEAREST)
    pixels = img.load()

    palette = {}
    pixel_map = []

    color_to_alias = {}
    next_alias_idx = 0

    for y in range(32):
        row = []
        for x in range(32):
            r, g, b, a = pixels[x, y]
            if a == 0:
                hex_color = "TRANSPARENT"
            else:
                hex_color = f"#{r:02X}{g:02X}{b:02X}"

            if hex_color not in color_to_alias:
                alias = get_alias(next_alias_idx)
                color_to_alias[hex_color] = alias
                palette[alias] = hex_color
                next_alias_idx += 1

            row.append(color_to_alias[hex_color])
        pixel_map.append(row)

    return {
        "palette": palette,
        "pixel_map": pixel_map
    }

def main():
    textures_dir = 'extracted_textures'
    output_dir = 'texture_data'
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(textures_dir):
        if filename.endswith('.png'):
            filepath = os.path.join(textures_dir, filename)
            data = process_image(filepath)
            output_filename = os.path.splitext(filename)[0] + '.json'
            with open(os.path.join(output_dir, output_filename), 'w') as f:
                json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
