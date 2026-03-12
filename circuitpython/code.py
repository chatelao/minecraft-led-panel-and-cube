import board
import neopixel
import json
import os
import time

# Configuration
PIXEL_PIN = board.D6
WIDTH = 32
HEIGHT = 8
NUM_PIXELS = WIDTH * HEIGHT
BRIGHTNESS = 0.1
ORDER = neopixel.GRB

# Initialize NeoPixel matrix
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER)

def get_pixel_index(x, y):
    """
    Map (x, y) coordinates to NeoPixel index.
    Adjust this function if your matrix layout is different (e.g., zigzag).
    """
    # Progressive layout: (0,0) is top-left, rows follow one after another
    return (y * WIDTH) + x

def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple."""
    if hex_color == "TRANSPARENT":
        return (0, 0, 0)
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def load_texture(filename):
    """Load a texture from JSON and downsample it to 16x16."""
    print("Loading", filename)
    with open(filename, 'r') as f:
        data = json.load(f)

    palette = {k: hex_to_rgb(v) for k, v in data['palette'].items()}
    pixel_map_32 = data['pixel_map']

    # Downsample 32x32 to 16x16 (1:2 shrink)
    # The original Minecraft textures are 16x16, upscaled to 32x32 in the JSON.
    # We take every second pixel to get back to 16x16.
    pixel_map_16 = []
    for y in range(0, 32, 2):
        row = []
        for x in range(0, 32, 2):
            row.append(palette[pixel_map_32[y][x]])
        pixel_map_16.append(row)
    return pixel_map_16

def display_textures(tex1, tex2, offset_y):
    """Display an 8-row slice of two 16x16 textures side-by-side."""
    for y in range(HEIGHT):
        for x in range(WIDTH // 2):
            # First texture on the left (16x8 slice)
            pixels[get_pixel_index(x, y)] = tex1[y + offset_y][x]
            # Second texture on the right (16x8 slice)
            pixels[get_pixel_index(x + 16, y)] = tex2[y + offset_y][x]
    pixels.show()

# Get all json files in the current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]
json_files.sort()

if not json_files:
    print("No JSON files found!")
    # Keep the script running so it doesn't just exit
    while True:
        time.sleep(1)

texture_cache = {}

def get_texture(filename):
    """Load texture into cache or return from cache."""
    if filename not in texture_cache:
        # Simple cache management: if cache gets too big, clear it
        if len(texture_cache) > 10:
            texture_cache.clear()
        texture_cache[filename] = load_texture(filename)
    return texture_cache[filename]

current_pair_idx = 0

print("Starting display cycle...")
while True:
    try:
        # Select two textures to display side-by-side
        f1 = json_files[current_pair_idx % len(json_files)]
        f2 = json_files[(current_pair_idx + 1) % len(json_files)]

        t1 = get_texture(f1)
        t2 = get_texture(f2)

        # Since the 8x32 display is only 8 pixels high and textures are 16x16,
        # we alternate between showing the top half and the bottom half.

        # Show top half (rows 0-7)
        display_textures(t1, t2, 0)
        time.sleep(2)

        # Show bottom half (rows 8-15)
        display_textures(t1, t2, 8)
        time.sleep(2)

        # Move to the next pair of textures
        current_pair_idx = (current_pair_idx + 2) % len(json_files)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
