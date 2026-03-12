# Popular Minecraft Textures

This repository contains 19 of the most popular and iconic Minecraft textures, along with their 32x32 color maps in JSON format.

You can view an interactive preview of these textures on the [GitHub Pages site](https://chatelao.github.io/minecraft-led-panel-and-cube/).

## Texture List

| Texture Name | Preview | Color Map (JSON) |
|--------------|---------|------------------|
| TNT | ![TNT](svgs/tnt_side.svg) | [tnt_side.json](color_maps/tnt_side.json) |
| Oak Log | ![Oak Log](svgs/oak_log.svg) | [oak_log.json](color_maps/oak_log.json) |
| Stone | ![Stone](svgs/stone.svg) | [stone.json](color_maps/stone.json) |
| Diamond | ![Diamond](svgs/diamond.svg) | [diamond.json](color_maps/diamond.json) |
| Netherite Ingot | ![Netherite Ingot](svgs/netherite_ingot.svg) | [netherite_ingot.json](color_maps/netherite_ingot.json) |
| Grass Block | ![Grass Block](svgs/grass_block_top.svg) | [grass_block_top.json](color_maps/grass_block_top.json) |
| Dirt | ![Dirt](svgs/dirt.svg) | [dirt.json](color_maps/dirt.json) |
| Cobblestone | ![Cobblestone](svgs/cobblestone.svg) | [cobblestone.json](color_maps/cobblestone.json) |
| Oak Planks | ![Oak Planks](svgs/oak_planks.svg) | [oak_planks.json](color_maps/oak_planks.json) |
| Crafting Table | ![Crafting Table](svgs/crafting_table_top.svg) | [crafting_table_top.json](color_maps/crafting_table_top.json) |
| Iron Ingot | ![Iron Ingot](svgs/iron_ingot.svg) | [iron_ingot.json](color_maps/iron_ingot.json) |
| Gold Ingot | ![Gold Ingot](svgs/gold_ingot.svg) | [gold_ingot.json](color_maps/gold_ingot.json) |
| Apple | ![Apple](svgs/apple.svg) | [apple.json](color_maps/apple.json) |
| Bread | ![Bread](svgs/bread.svg) | [bread.json](color_maps/bread.json) |
| Iron Sword | ![Iron Sword](svgs/iron_sword.svg) | [iron_sword.json](color_maps/iron_sword.json) |
| Diamond Pickaxe | ![Diamond Pickaxe](svgs/diamond_pickaxe.svg) | [diamond_pickaxe.json](color_maps/diamond_pickaxe.json) |
| Torch | ![Torch](svgs/torch.svg) | [torch.json](color_maps/torch.json) |
| Water Bucket | ![Water Bucket](svgs/water_bucket.svg) | [water_bucket.json](color_maps/water_bucket.json) |
| Glass | ![Glass](svgs/glass.svg) | [glass.json](color_maps/glass.json) |

## JSON Color Map Format

Each JSON file in the `color_maps/` directory contains two parts:
1. **palette**: A mapping of letter aliases (A, B, C, etc.) to RGB hex color codes.
2. **pixel_map**: A 32x32 grid (array of arrays) of letter aliases representing the texture's pixels.

All textures have been upscaled to 32x32 using nearest-neighbor interpolation to preserve the pixelated look.
