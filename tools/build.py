import os
import json
import zipfile

def build():
    with open('tools/config.json', 'r') as f:
        config = json.load(f)
    
    file_name = config.get('file_name', 'mod')
    file_version = config.get('file_version', '1.0.0')
    
    if not os.path.exists('build'):
        os.makedirs('build')
        
    jar_path = f"build/{file_name}-{file_version}.jar"
    zip_path = f"build/{file_name}-{file_version}.zip"
    
    jar_items = ['META-INF', 'fabric.mod.json', 'LICENSE.md', 'icon.png', 'data', 'assets']
    zip_items = ['pack.mcmeta', 'pack.png', 'LICENSE.md', 'assets', 'data']
    
    def add_to_zip(z_obj, base_dir, items):
        for item in items:
            item_path = os.path.join(base_dir, item)
            if not os.path.exists(item_path):
                print(f"Warning: {item_path} not found, skipping.")
                continue
            if os.path.isdir(item_path):
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        if file == '.gitignore' or file == 'CHANGELOG.md':
                            continue
                        file_path = os.path.join(root, file)
                        # Make path relative to base_dir so "src/" doesn't appear in the zip
                        arcname = os.path.relpath(file_path, base_dir)
                        z_obj.write(file_path, arcname)
            else:
                if item != '.gitignore' and item != 'CHANGELOG.md':
                    arcname = os.path.relpath(item_path, base_dir)
                    z_obj.write(item_path, arcname)

    print(f"Building {jar_path}...")
    with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as j:
        add_to_zip(j, 'src', jar_items)
        
    print(f"Building {zip_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        add_to_zip(z, 'src', zip_items)
        
    print("Build complete!")

if __name__ == '__main__':
    build()
