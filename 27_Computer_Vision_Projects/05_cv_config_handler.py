"""
PROPER DEFINITION:
Configuration management in software engineering involves centralizing application 
settings (like HSV values, file paths, or camera IDs) into a single, manageable 
location. In CV projects, this allows for rapid experimentation without modifying 
the core logic. Common formats include JSON, YAML, or simple Python dictionaries. 
This practice ensures that parameters used for one environment (e.g., indoor lighting) 
can be easily swapped for another.
"""

import json
import os

class ConfigManager:
    """Handles loading and saving configuration for CV projects."""
    
    def __init__(self, config_file="cv_config.json"):
        self.config_file = config_file
        self.settings = {
            "camera_id": 0,
            "hsv_lower": [0, 120, 70],
            "hsv_upper": [10, 255, 255],
            "output_filename": "cloak_output.avi",
            "debug_mode": True
        }

    def load_config(self):
        """Loads settings from a JSON file if it exists."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.settings.update(json.load(f))
            print(f"Configuration loaded from {self.config_file}")
        else:
            print("Config file not found, using defaults.")

    def save_config(self):
        """Saves current settings to a JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)
        print(f"Configuration saved to {self.config_file}")

def config_demo():
    print("--- CV Configuration Management ---")
    
    cm = ConfigManager()
    
    # Show default settings
    print(f"Default HSV Lower: {cm.settings['hsv_lower']}")
    
    # Modify and save
    cm.settings['hsv_lower'] = [5, 130, 80]
    cm.save_config()
    
    # Load back
    cm.load_config()
    print(f"Updated HSV Lower from config: {cm.settings['hsv_lower']}")
    
    # Cleanup for demo
    if os.path.exists("cv_config.json"):
        os.remove("cv_config.json")
        print("Demo config file cleaned up.")

if __name__ == "__main__":
    config_demo()
