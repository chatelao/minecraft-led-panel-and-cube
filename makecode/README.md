# Minecraft Textures for 16x16 LED Matrix (MakeCode Maker)

This folder contains the code and tools to display alternating Minecraft textures on a 16x16 NeoPixel LED matrix using a Raspberry Pi Pico.

## Hardware Setup

- **Controller:** Raspberry Pi Pico
- **Display:** 16x16 NeoPixel (WS2812B) LED Matrix
- **Connections:**
  - `GP0` on Pico to `DIN` on the LED matrix.
  - `GND` on Pico to `GND` on the LED matrix.
  - `VBUS` (or a separate 5V power supply) to `5V` on the LED matrix.

*Note: For a full 16x16 matrix (256 LEDs), an external 5V power supply is recommended as the Pico's VBUS might not provide enough current for all LEDs at full brightness.*

## Software Setup

1. Open [maker.makecode.com](https://maker.makecode.com/).
2. Select **Raspberry Pi Pico**.
3. Click on the **Extensions** button (gear icon or in the drawer) and search for `neopixel`. Add the extension.
4. Switch from the **Blocks** view to the **JavaScript** (or TypeScript) view.
5. Copy the entire content of [main.ts](./main.ts) and paste it into the editor, replacing any existing code.
6. Click **Download** and follow the instructions to copy the `.uf2` file to your Raspberry Pi Pico.

## Customization

- **Brightness:** You can adjust the brightness by changing `strip.setBrightness(20)` in the code.
- **Wiring Pattern:** The code assumes a **serpentine (zigzag)** wiring pattern, which is common for flexible LED matrices. If your matrix uses a standard row-major pattern, change the `serpentine` parameter to `false` in the `displayTexture` call.
- **Speed:** Adjust the `pause(2000)` value at the end of the script to change how quickly the textures rotate.

## Regenerating the Code

If you add new JSON color maps to the `color_maps/` directory in the root of the repository, you can regenerate the `main.ts` file by running the following command from the root directory:

```bash
python3 makecode/generate_makecode.py
```
