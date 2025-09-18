import customtkinter as ctk
import subprocess
import os
from config import Config
from dialogs import AddAccountDialog, SettingsDialog
from tkinter import messagebox

class GameLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.config = Config()
        
        self.title("RoK Multi Launcher")
        self.geometry("800x600")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        sidebar = ctk.CTkFrame(self, width=100, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(4, weight=1)
        
        ctk.CTkButton(sidebar, text="+", width=70, command=self.show_add_dialog).grid(row=0, column=0, padx=15, pady=15)
        ctk.CTkButton(sidebar, text="⚙", width=70, command=self.show_settings_dialog).grid(row=1, column=0, padx=15, pady=15)
        
        self.account_frame = ctk.CTkScrollableFrame(self)
        self.account_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.refresh_account_list()

    def refresh_account_list(self):
        for widget in self.account_frame.winfo_children():
            widget.destroy()
            
        for account in self.config.get_accounts():
            frame = ctk.CTkFrame(self.account_frame)
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=f"Account: {account['name']}").pack(side="left", padx=10)
            ctk.CTkLabel(frame, text=f"Sandbox: {account['sandbox']}").pack(side="left", padx=10)
            
            delete_btn = ctk.CTkButton(
                frame,
                text="Delete",
                fg_color="red",
                hover_color="darkred",
                command=lambda acc=account: self.delete_account(acc)
            )
            delete_btn.pack(side="right", padx=10)
            
            launch_btn = ctk.CTkButton(
                frame,
                text="Launch",
                command=lambda acc=account: self.launch_game(acc)
            )
            launch_btn.pack(side="right", padx=10)

    def delete_account(self, account):
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the account '{account['name']}'?"):
            self.config.remove_account(account['name'])
            self.refresh_account_list()

    def launch_game(self, account):
        game_id, sandboxie_path, game_path = self.config.get_settings()
        
        if not all([game_id, sandboxie_path, game_path]):
            messagebox.showerror("Error", "Please configure settings first")
            return
        
        game_dir = os.path.dirname(game_path)
        cmd = f'"{sandboxie_path}" /box:{account["sandbox"]} "{game_path}" {game_id} win 0^|1'
        print(f"Executing cmd: {cmd}")
        
        subprocess.Popen(
            cmd, 
            shell=True,
            cwd=game_dir
        )

    def show_add_dialog(self):
        AddAccountDialog(self, self.add_account)

    def add_account(self, name, sandbox):
        self.config.add_account(name, sandbox)
        self.refresh_account_list()

    def show_settings_dialog(self):
        SettingsDialog(self, self.save_settings, self.config.get_settings())

    def save_settings(self, game_id, sandboxie_path, game_path):
        self.config.update_settings(game_id, sandboxie_path, game_path)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = GameLauncher()
    app.mainloop()