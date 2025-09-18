import customtkinter as ctk
from tkinter import messagebox

class AddAccountDialog(ctk.CTkToplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        
        self.title("Add Account")
        self.grab_set()
        
        self.geometry("300x300")
        self.resizable(False, False)
        
        self.withdraw()
        self.update_idletasks()
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        x = parent_x + (parent_width - 300) // 2
        y = parent_y + (parent_height - 300) // 2
        self.geometry(f"300x300+{x}+{y}")
        self.deiconify()
        
        ctk.CTkLabel(self, text="Account Name:").pack(pady=10)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)
        
        ctk.CTkLabel(self, text="Sandbox Name:").pack(pady=10)
        self.sandbox_entry = ctk.CTkEntry(self)
        self.sandbox_entry.pack(pady=5)
        
        ctk.CTkButton(self, text="Add", command=self.add_account).pack(pady=20)

    def add_account(self):
        name = self.name_entry.get().strip()
        sandbox = self.sandbox_entry.get().strip()
        
        if not name or not sandbox:
            messagebox.showerror("Error", "Please fill in all fields")
            return
            
        self.callback(name, sandbox)
        self.destroy()

class SettingsDialog(ctk.CTkToplevel):
    def __init__(self, parent, callback, current_settings):
        super().__init__(parent)
        self.callback = callback
        
        self.title("Settings")
        self.grab_set()
        
        self.geometry("400x400")
        self.resizable(False, False)
        
        self.withdraw()
        self.update_idletasks()
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        x = parent_x + (parent_width - 400) // 2
        y = parent_y + (parent_height - 400) // 2
        self.geometry(f"400x400+{x}+{y}")
        self.deiconify()
        
        ctk.CTkLabel(self, text="Game ID:").pack(pady=10)
        self.game_id_entry = ctk.CTkEntry(self, width=400)
        self.game_id_entry.pack(pady=5)
        self.game_id_entry.insert(0, current_settings[0])
        
        ctk.CTkLabel(self, text="Sandboxie Path:").pack(pady=10)
        self.sandboxie_entry = ctk.CTkEntry(self, width=400)
        self.sandboxie_entry.pack(pady=5)
        self.sandboxie_entry.insert(0, current_settings[1])
        
        ctk.CTkLabel(self, text="Game Path:").pack(pady=10)
        self.game_entry = ctk.CTkEntry(self, width=400)
        self.game_entry.pack(pady=5)
        self.game_entry.insert(0, current_settings[2])
        
        ctk.CTkButton(self, text="Save", command=self.save_settings).pack(pady=20)

    def save_settings(self):
        game_id = self.game_id_entry.get().strip()
        sandboxie_path = self.sandboxie_entry.get().strip()
        game_path = self.game_entry.get().strip()
        
        if not all([game_id, sandboxie_path, game_path]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
            
        self.callback(game_id, sandboxie_path, game_path)
        self.destroy()