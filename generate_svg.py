import json
import os

def process_json_to_svg(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    palette = data['palette']
    pixel_map_32 = data['pixel_map']

    # Use existing 16x16 grid or downsample from 32x32
    if len(pixel_map_32) == 16:
        pixel_map_16 = pixel_map_32
    else:
        # Downsample from 32x32 to 16x16
        # The README says: "All textures have been upscaled to 32x32 using nearest-neighbor interpolation"
        # So we take every second pixel to get back to 16x16.
        pixel_map_16 = []
        for y in range(0, 32, 2):
            row = []
            for x in range(0, 32, 2):
                row.append(pixel_map_32[y][x])
            pixel_map_16.append(row)

    # SVG parameters
    rect_size = 10
    grid_size = 16
    width = rect_size * grid_size
    height = rect_size * grid_size

    svg_header = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
    svg_footer = '</svg>'

    rects = []
    for y in range(grid_size):
        for x in range(grid_size):
            alias = pixel_map_16[y][x]
            color = palette[alias]
            if color == "TRANSPARENT":
                continue

            rect = f'  <rect x="{x * rect_size}" y="{y * rect_size}" width="{rect_size}" height="{rect_size}" fill="{color}" />'
            rects.append(rect)

    svg_content = svg_header + "\n" + "\n".join(rects) + "\n" + svg_footer
    return svg_content

def main():
    input_dir = 'color_maps'
    output_dir = 'svgs'
    os.makedirs(output_dir, exist_ok=True)

    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith('.json'):
            filepath = os.path.join(input_dir, filename)
            svg_content = process_json_to_svg(filepath)

            output_filename = os.path.splitext(filename)[0] + '.svg'
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w') as f:
                f.write(svg_content)
            print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
