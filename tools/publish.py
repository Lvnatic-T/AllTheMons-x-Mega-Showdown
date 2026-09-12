import os
import json
import requests

def load_env():
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    os.environ[k] = v

def publish():
    load_env()
    token = os.environ.get("MODRINTH_TOKEN")
    if not token:
        print("Error: MODRINTH_TOKEN not found in .env")
        return

    with open('tools/config.json', 'r') as f:
        config = json.load(f)

    file_name = config.get('file_name', 'mod')
    file_version = config.get('file_version', '1.0.0')
    release_type = config.get('release_type', 'release').lower()
    
    # Map from alpha/beta/stable to alpha/beta/release
    if release_type == 'stable':
        release_type = 'release'
        
    mod_project_id = config.get('mod_project_id')
    datapack_project_id = config.get('datapack_project_id')

    fabric_deps = config.get('fabric_dependencies', [])
    neoforge_deps = config.get('neoforge_dependencies', [])
    datapack_deps = config.get('datapack_dependencies', [])
    
    # Combine fabric and neoforge dependencies for the mod jar
    mod_deps = fabric_deps + neoforge_deps

    changelog = ""
    if os.path.exists("src/CHANGELOG.md"):
        with open("src/CHANGELOG.md", "r") as f:
            changelog = f.read()
    elif os.path.exists("CHANGELOG.md"): # Fallback just in case
        with open("CHANGELOG.md", "r") as f:
            changelog = f.read()

    jar_path = f"build/{file_name}-{file_version}.jar"
    zip_path = f"build/{file_name}-{file_version}.zip"

    headers = {
        "Authorization": token
    }
    
    API_URL = "https://api.modrinth.com/v2/version"

    # Publish Mod JAR
    if os.path.exists(jar_path) and mod_project_id:
        print(f"Publishing {jar_path} to Modrinth (Project: {mod_project_id})...")
        mod_data = {
            "name": f"{file_name} {file_version} (Mod)",
            "version_number": file_version,
            "changelog": changelog,
            "dependencies": mod_deps,
            "game_versions": ["1.21.1"],
            "version_type": release_type,
            "loaders": ["fabric", "neoforge"],
            "featured": True,
            "status": "listed",
            "project_id": mod_project_id,
            "environment": "client_and_server",
            "file_parts": ["file"],
            "primary_file": "file"
        }
        
        with open(jar_path, "rb") as f:
            files = {
                "data": (None, json.dumps(mod_data), "application/json"),
                "file": (os.path.basename(jar_path), f, "application/java-archive")
            }
            resp = requests.post(API_URL, headers=headers, files=files)
            
        if resp.status_code == 200:
            print("Successfully published Mod JAR!")
        else:
            print(f"Failed to publish Mod JAR: {resp.status_code}")
            print(resp.text)
    else:
        print("Skipping Mod JAR publish (file not found or project_id not set).")

    # Publish Datapack ZIP
    if os.path.exists(zip_path) and datapack_project_id:
        print(f"Publishing {zip_path} to Modrinth (Project: {datapack_project_id})...")
        dp_data = {
            "name": f"{file_name} {file_version} (Datapack)",
            "version_number": file_version,
            "changelog": changelog,
            "dependencies": datapack_deps,
            "game_versions": ["1.21.1"],
            "version_type": release_type,
            "loaders": ["datapack", "minecraft"],
            "featured": True,
            "status": "listed",
            "project_id": datapack_project_id,
            "file_parts": ["file"],
            "primary_file": "file"
        }
        
        with open(zip_path, "rb") as f:
            files = {
                "data": (None, json.dumps(dp_data), "application/json"),
                "file": (os.path.basename(zip_path), f, "application/zip")
            }
            resp = requests.post(API_URL, headers=headers, files=files)
            
        if resp.status_code == 200:
            print("Successfully published Datapack ZIP!")
        else:
            print(f"Failed to publish Datapack ZIP: {resp.status_code}")
            print(resp.text)
    else:
        print("Skipping Datapack ZIP publish (file not found or project_id not set).")

if __name__ == '__main__':
    publish()
