import os
import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline

class AImusicGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Music Generator")
        self.model_directory = ""
        self.setup_gui()

    def setup_gui(self):
        self.model_dir_button = tk.Button(self.root, text="Choose Model Directory", command=self.choose_model_directory)
        self.model_dir_button.pack(pady=10)

        self.generate_button = tk.Button(self.root, text="Generate Music", command=self.generate_music)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Music", command=self.save_music)
        self.save_button.pack(pady=10)

        self.adjust_button = tk.Button(self.root, text="Adjust Music Parameters", command=self.adjust_parameters)
        self.adjust_button.pack(pady=10)

        self.share_button = tk.Button(self.root, text="Share Music", command=self.share_music)
        self.share_button.pack(pady=10)

    def choose_model_directory(self):
        self.model_directory = filedialog.askdirectory()
        if self.model_directory:
            messagebox.showinfo("Directory Selected", f"Model directory set to: {self.model_directory}")

    def generate_music(self):
        if not self.model_directory:
            messagebox.showwarning("No Directory", "Please choose a model directory first.")
            return

        # Load the model from the chosen directory
        model = pipeline('text-to-music', model=self.model_directory)
        music = model("Generate a piece of music")
        self.generated_music = music
        messagebox.showinfo("Music Generated", "Music has been generated successfully.")

    def save_music(self):
        if not hasattr(self, 'generated_music'):
            messagebox.showwarning("No Music", "Please generate music first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if save_path:
            with open(save_path, 'wb') as f:
                f.write(self.generated_music)
            messagebox.showinfo("Music Saved", "Music has been saved successfully.")

    def adjust_parameters(self):
        # Placeholder for adjusting music parameters
        messagebox.showinfo("Adjust Parameters", "Adjusting music parameters is not implemented yet.")

    def share_music(self):
        # Placeholder for sharing music
        messagebox.showinfo("Share Music", "Sharing music is not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AImusicGeneratorApp(root)
    root.mainloop()
