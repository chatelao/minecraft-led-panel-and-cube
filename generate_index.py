import os

def get_wiki_link(base_name):
    # Mapping for special cases
    mapping = {
        'tnt_side': 'TNT',
        'grass_block_top': 'Grass_Block',
        'crafting_table_top': 'Crafting_Table',
        'oak_log': 'Oak_Log',
        'oak_planks': 'Oak_Planks',
        'diamond_pickaxe': 'Diamond_Pickaxe',
        'iron_sword': 'Iron_Sword',
        'gold_ingot': 'Gold_Ingot',
        'iron_ingot': 'Iron_Ingot',
        'netherite_ingot': 'Netherite_Ingot',
        'water_bucket': 'Water_Bucket'
    }

    if base_name in mapping:
        wiki_name = mapping[base_name]
    else:
        wiki_name = base_name.replace('_', ' ').title().replace(' ', '_')

    return f"https://minecraft.wiki/w/{wiki_name}"

def main():
    svg_dir = 'svgs'
    svg_files = sorted([f for f in os.listdir(svg_dir) if f.endswith('.svg')])

    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minecraft Textures SVG Overview</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #333;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1200px;
        }
        .card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card img {
            width: 128px;
            height: 128px;
            image-rendering: pixelated;
            margin-bottom: 10px;
        }
        .card a {
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
            margin: 5px 0;
        }
        .card a:hover {
            text-decoration: underline;
        }
        .card .name {
            margin-bottom: 10px;
            font-size: 1.1em;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Minecraft Textures SVG Overview</h1>
    <div class="grid">
"""

    for svg_file in svg_files:
        base_name = os.path.splitext(svg_file)[0]
        # Custom display names
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
        name = display_names.get(base_name, base_name.replace('_', ' ').title())
        wiki_link = get_wiki_link(base_name)
        html_content += f"""
        <div class="card">
            <img src="svgs/{svg_file}" alt="{name}">
            <div class="name">{name}</div>
            <a href="{wiki_link}" target="_blank">View on Minecraft Wiki</a>
            <a href="paint_by_numbers/{base_name}.pdf" target="_blank">Download Paint by Numbers PDF</a>
        </div>
"""

    html_content += """
    </div>
</body>
</html>
"""

    with open('index.html', 'w') as f:
        f.write(html_content)
    print("Generated index.html")

if __name__ == "__main__":
    main()
