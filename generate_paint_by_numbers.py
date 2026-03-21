import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

def get_display_name(base_name):
    display_names = {
        'tnt_side': 'TNT',
        'grass_block_top': 'Grass Block',
        'crafting_table_top': 'Crafting Table',
        'oak_log': 'Oak Log',
        'oak_planks': 'Oak Planks',
        'diamond_pickaxe': 'Diamond Pickaxe',
        'iron_sword': 'Iron Sword',
        'gold_ingot': 'Gold Ingot',
        'iron_ingot': 'Iron Ingot',
        'netherite_ingot': 'Netherite Ingot',
        'water_bucket': 'Water Bucket'
    }
    return display_names.get(base_name, base_name.replace('_', ' ').title())

def draw_paint_by_numbers_page(c, json_filepath):
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    palette = data['palette']
    pixel_map_32 = data['pixel_map']
    base_name = os.path.splitext(os.path.basename(json_filepath))[0]
    title = get_display_name(base_name)

    # Use existing 16x16 grid or downsample from 32x32
    if len(pixel_map_32) == 16:
        pixel_map_16 = pixel_map_32
    else:
        pixel_map_16 = []
        for y in range(0, 32, 2):
            row = []
            for x in range(0, 32, 2):
                row.append(pixel_map_32[y][x])
            pixel_map_16.append(row)

    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - 2*cm, f"Malen nach Zahlen: {title}")

    # Grid parameters
    grid_size = 16
    cell_size = 0.8 * cm
    grid_width = grid_size * cell_size
    grid_height = grid_size * cell_size
    start_x = (width - grid_width) / 2.0
    start_y = height - 4*cm - grid_height

    # Map aliases to numbers (excluding TRANSPARENT)
    sorted_aliases = sorted([a for a in palette.keys() if palette[a] != "TRANSPARENT"])
    alias_to_num = {alias: i + 1 for i, alias in enumerate(sorted_aliases)}

    # Draw Grid
    c.setLineWidth(0.5)
    c.setStrokeColor(colors.black)
    c.setFont("Helvetica", 8)

    for y in range(grid_size):
        for x in range(grid_size):
            alias = pixel_map_16[y][x]
            x_pos = start_x + x * cell_size
            y_pos = start_y + (grid_size - 1 - y) * cell_size

            c.rect(x_pos, y_pos, cell_size, cell_size)

            if base_name == 'matrix':
                # Zigzag: bottom-left (0) to top-left (255)
                # row_from_bottom=0 is the bottom row (y=15), row_from_bottom=15 is the top row (y=0)
                row_from_bottom = grid_size - 1 - y
                if row_from_bottom % 2 == 0:
                    # Even rows from bottom: left to right (0, 1, ..., 15)
                    num = row_from_bottom * grid_size + x
                else:
                    # Odd rows from bottom: right to left (31, 30, ..., 16)
                    num = row_from_bottom * grid_size + (grid_size - 1 - x)
                c.drawCentredString(x_pos + cell_size/2.0, y_pos + cell_size/2.0 - 3, str(num))
            elif alias in alias_to_num:
                num = alias_to_num[alias]
                # Center the number in the cell
                c.drawCentredString(x_pos + cell_size/2.0, y_pos + cell_size/2.0 - 3, str(num))

    # Skip legend for Matrix
    if base_name == 'matrix':
        c.showPage()
        return

    # Legend
    legend_start_y = start_y - 1*cm
    c.setFont("Helvetica-Bold", 14)
    c.drawString(start_x, legend_start_y, "Legende:")

    c.setFont("Helvetica", 12)
    item_height = 0.6 * cm
    cols = 3
    col_width = grid_width / cols

    for i, alias in enumerate(sorted_aliases):
        num = alias_to_num[alias]
        color_hex = palette[alias]

        row = i // cols
        col = i % cols

        x_pos = start_x + col * col_width
        y_pos = legend_start_y - 1*cm - row * item_height

        # Color box
        c.setFillColor(colors.HexColor(color_hex))
        c.rect(x_pos, y_pos, 0.4*cm, 0.4*cm, fill=1)

        # Number and Color name (or just number)
        c.setFillColor(colors.black)
        c.drawString(x_pos + 0.6*cm, y_pos + 0.1*cm, f"{num}: {color_hex}")

    c.showPage()

def generate_pdf(json_filepath, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    draw_paint_by_numbers_page(c, json_filepath)
    c.save()

def generate_unified_pdf(json_filepaths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    for filepath in json_filepaths:
        draw_paint_by_numbers_page(c, filepath)
    c.save()

def main():
    input_dir = 'color_maps'
    output_dir = 'paint_by_numbers'
    os.makedirs(output_dir, exist_ok=True)

    json_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.json')])
    json_filepaths = []

    for filename in json_files:
        filepath = os.path.join(input_dir, filename)
        json_filepaths.append(filepath)
        output_filename = os.path.splitext(filename)[0] + '.pdf'
        output_path = os.path.join(output_dir, output_filename)
        generate_pdf(filepath, output_path)
        print(f"Generated {output_path}")

    # Generate unified PDF
    unified_output_path = os.path.join(output_dir, '_heft_malen_nach_zahlen.pdf')
    generate_unified_pdf(json_filepaths, unified_output_path)
    print(f"Generated unified PDF: {unified_output_path}")

if __name__ == "__main__":
    main()
