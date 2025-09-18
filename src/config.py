import json
import os

class Config:
    def __init__(self):
        self.config_file = "launcher_config.json"
        self.default_config = {
            "game_id": "",
            "sandboxie_path": r"C:\Program Files\Sandboxie-Plus\Start.exe",
            "game_path": r"C:\Program Files (x86)\Rise of Kingdoms\Rise of Kingdoms Game\MASS.exe",
            "accounts": []
        }
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def add_account(self, name, sandbox):
        self.config["accounts"].append({
            "name": name,
            "sandbox": sandbox
        })
        self.save_config()

    def remove_account(self, name):
        self.config["accounts"] = [acc for acc in self.config["accounts"] if acc["name"] != name]
        self.save_config()

    def update_settings(self, game_id, sandboxie_path, game_path):
        self.config["game_id"] = game_id
        self.config["sandboxie_path"] = sandboxie_path
        self.config["game_path"] = game_path
        self.save_config()

    def get_accounts(self):
        return self.config["accounts"]

    def get_settings(self):
        return (
            self.config["game_id"],
            self.config["sandboxie_path"],
            self.config["game_path"]
        )