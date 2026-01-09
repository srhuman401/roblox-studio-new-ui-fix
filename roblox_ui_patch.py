import os 
import json

base_path = os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions")

if not os.path.exists(base_path):
    print("Failed: Roblox Versions folder not found")
    exit()
   

flag_data = {
    "FFlagEnableRibbonPlugin3": "false"
}

fixed = 0

for version in os.listdir(base_path):
    version_path = os.path.join(base_path, version)
    studio_exe = os.path.join(version_path, "RobloxStudioBeta.exe")
    if os.path.isfile(studio_exe):
        client_settings = os.path.join(version_path, "ClientSettings")
        os.makedirs(client_settings, exist_ok=True)
        settings_file = os.path.join(client_settings, "ClientAppSettings.json")
        with open(settings_file, "w") as f:
            json.dump(flag_data, f, indent=4)
        fixed += 1

print(f"Fixed {fixed} studio versions, exited without error")