import json
import os

def hex_to_makecode(hex_str):
    if hex_str == "TRANSPARENT":
        return "0x000000"
    return hex_str.replace("#", "0x")

def process_texture(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    palette = data['palette']
    pixel_map_32 = data['pixel_map']

    # Downsample to 16x16
    pixel_map_16 = []
    for y in range(0, 32, 2):
        for x in range(0, 32, 2):
            pixel_map_16.append(pixel_map_32[y][x])

    # Convert to colors
    colors = [hex_to_makecode(palette[alias]) for alias in pixel_map_16]
    return colors

def main():
    input_dir = 'color_maps'
    output_file = 'makecode/main.ts'

    textures = []
    names = []

    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith('.json'):
            filepath = os.path.join(input_dir, filename)
            colors = process_texture(filepath)
            textures.append(colors)
            names.append(os.path.splitext(filename)[0])

    ts_content = f"""// Generated code for Minecraft Textures on 16x16 LED Matrix
// Target: Raspberry Pi Pico (Maker MakeCode)
// Requirement: "neopixel" extension

const textures: number[][] = [
"""
    for i, colors in enumerate(textures):
        ts_content += f"    [{', '.join(colors)}], // {names[i]}\n"

    ts_content += """];

// Configure NeoPixel strip on GP0 with 256 LEDs (16x16)
let strip = neopixel.create(pins.GP0, 256, NeoPixelMode.RGB);
strip.setBrightness(20); // Set brightness to a reasonable level

/**
 * Displays a texture on the 16x16 matrix.
 * @param index The index of the texture in the textures array.
 * @param serpentine Whether the matrix is wired in a serpentine/zigzag pattern.
 */
function displayTexture(index: number, serpentine: boolean = true) {
    let texture = textures[index];
    for (let y = 0; y < 16; y++) {
        for (let x = 0; x < 16; x++) {
            let pixelIndex = y * 16 + x;
            let stripIndex = 0;

            if (serpentine) {
                // In serpentine layout, every odd row is reversed
                if (y % 2 == 1) {
                    stripIndex = y * 16 + (15 - x);
                } else {
                    stripIndex = y * 16 + x;
                }
            } else {
                stripIndex = y * 16 + x;
            }

            strip.setPixelColor(stripIndex, texture[pixelIndex]);
        }
    }
    strip.show();
}

let currentTexture = 0;

forever(function () {
    displayTexture(currentTexture);
    currentTexture = (currentTexture + 1) % textures.length;
    pause(2000); // Wait for 2 seconds
});
"""

    with open(output_file, 'w') as f:
        f.write(ts_content)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    main()
