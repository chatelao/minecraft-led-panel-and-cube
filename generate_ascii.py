import json
import os

def hex_to_rgb(hex_color):
    if hex_color == "TRANSPARENT":
        return None
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_luminance(rgb):
    if rgb is None:
        return -1 # For transparent
    r, g, b = rgb
    # Using relative luminance formula
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def get_ascii_char(luminance):
    # ASCII characters from darkest to brightest
    chars = " .:-=+*#%@"
    if luminance == -1:
        return " "
    # luminance is 0-255. Map it to 0-(len(chars)-1)
    idx = int((luminance / 255) * (len(chars) - 1))
    return chars[idx]

def process_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    palette = data['palette']
    pixel_map = data['pixel_map']

    # Pre-calculate ASCII chars for each alias
    alias_to_ascii = {}
    for alias, color in palette.items():
        rgb = hex_to_rgb(color)
        lum = get_luminance(rgb)
        alias_to_ascii[alias] = get_ascii_char(lum)

    ascii_rows = []
    for row in pixel_map:
        # Doubling characters horizontally to account for terminal font aspect ratio
        ascii_row = "".join([alias_to_ascii[alias] * 2 for alias in row])
        ascii_rows.append(ascii_row)

    ascii_art = "\n".join(ascii_rows)
    return f"```\n{ascii_art}\n```"

def main():
    input_dir = 'color_maps'
    output_dir = 'ascii_art'
    os.makedirs(output_dir, exist_ok=True)

    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith('.json'):
            filepath = os.path.join(input_dir, filename)
            ascii_md = process_json(filepath)

            output_filename = os.path.splitext(filename)[0] + '.md'
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w') as f:
                f.write(ascii_md)
            print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
