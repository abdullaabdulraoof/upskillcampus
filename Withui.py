import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
# File type categories
audio = [".mp3", ".wma", ".aac"]
video = [".mp4", ".wmv", ".avi", ".mkv"]
docs = [".docx", ".pdf"]
software = [".exe", ".apk"]
zips = [".zip", ".rar"]

categories = {
    "audio": audio,
    "video": video,
    "docs": docs,
    "software": software,
    "zips": zips,
    "unknown": []
}
def organize_files(base_path):
    # Create directories if they don't exist
    for folder in categories.keys():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Scan the directory
    for root, dirs, files in os.walk(base_path):
        for file in files:
            extention = os.path.splitext(file)[1].lower()
            source_path = os.path.join(root, file)
            # Skip if the file is already in the correct folder
            if any(folder in root for folder in categories.keys()):
                continue
            # Move file to the appropriate folder based on extension
            moved = False
            for folder, extensions in categories.items():
                if extention in extensions:
                    shutil.move(source_path, os.path.join(base_path, folder))
                    moved = True
                    break
            if not moved:
                shutil.move(source_path, os.path.join(base_path, "unknown"))


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)
        messagebox.showinfo("Success", "Files organized successfully!")


def create_ui():
    root = tk.Tk()
    root.title("File Organizer")

    canvas = tk.Canvas(root, height=150, width=300)
    canvas.pack()

    label = tk.Label(root, text="Select a directory to organize:")
    label.pack(pady=10)

    button = tk.Button(root, text="Browse", command=select_directory)
    button.pack(pady=10)

    root.mainloop()


create_ui()
