# Popular Minecraft Textures

This repository contains 19 of the most popular and iconic Minecraft textures, along with their 32x32 color maps in JSON format.

## Texture List

| Texture Name | Preview | Color Map (JSON) |
|--------------|---------|------------------|
| TNT | ![TNT](textures/tnt_side.png) | [tnt_side.json](color_maps/tnt_side.json) |
| Oak Log | ![Oak Log](textures/oak_log.png) | [oak_log.json](color_maps/oak_log.json) |
| Stone | ![Stone](textures/stone.png) | [stone.json](color_maps/stone.json) |
| Diamond | ![Diamond](textures/diamond.png) | [diamond.json](color_maps/diamond.json) |
| Netherite Ingot | ![Netherite Ingot](textures/netherite_ingot.png) | [netherite_ingot.json](color_maps/netherite_ingot.json) |
| Grass Block | ![Grass Block](textures/grass_block_top.png) | [grass_block_top.json](color_maps/grass_block_top.json) |
| Dirt | ![Dirt](textures/dirt.png) | [dirt.json](color_maps/dirt.json) |
| Cobblestone | ![Cobblestone](textures/cobblestone.png) | [cobblestone.json](color_maps/cobblestone.json) |
| Oak Planks | ![Oak Planks](textures/oak_planks.png) | [oak_planks.json](color_maps/oak_planks.json) |
| Crafting Table | ![Crafting Table](textures/crafting_table_top.png) | [crafting_table_top.json](color_maps/crafting_table_top.json) |
| Iron Ingot | ![Iron Ingot](textures/iron_ingot.png) | [iron_ingot.json](color_maps/iron_ingot.json) |
| Gold Ingot | ![Gold Ingot](textures/gold_ingot.png) | [gold_ingot.json](color_maps/gold_ingot.json) |
| Apple | ![Apple](textures/apple.png) | [apple.json](color_maps/apple.json) |
| Bread | ![Bread](textures/bread.png) | [bread.json](color_maps/bread.json) |
| Iron Sword | ![Iron Sword](textures/iron_sword.png) | [iron_sword.json](color_maps/iron_sword.json) |
| Diamond Pickaxe | ![Diamond Pickaxe](textures/diamond_pickaxe.png) | [diamond_pickaxe.json](color_maps/diamond_pickaxe.json) |
| Torch | ![Torch](textures/torch.png) | [torch.json](color_maps/torch.json) |
| Water Bucket | ![Water Bucket](textures/water_bucket.png) | [water_bucket.json](color_maps/water_bucket.json) |
| Glass | ![Glass](textures/glass.png) | [glass.json](color_maps/glass.json) |

## JSON Color Map Format

Each JSON file in the `color_maps/` directory contains two parts:
1. **palette**: A mapping of letter aliases (A, B, C, etc.) to RGB hex color codes.
2. **pixel_map**: A 32x32 grid (array of arrays) of letter aliases representing the texture's pixels.

All textures have been upscaled to 32x32 using nearest-neighbor interpolation to preserve the pixelated look.
