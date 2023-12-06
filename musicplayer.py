import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def _init_(self, master):
        self.master = master
        self.master.title("Simple Music Player")
        self.master.geometry("400x200")

        self.playlist = []
        self.current_track = 0

        pygame.init()

        # GUI Components
        self.label = tk.Label(self.master, text="Music Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, activestyle='none', font=("Helvetica", 12))
        self.listbox.pack(pady=10)

        self.load_button = tk.Button(self.master, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

    def load_music(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        for file_path in file_paths:
            self.playlist.append(file_path)
            self.listbox.insert(tk.END, os.path.basename(file_path))

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        selected_index = self.listbox.curselection()
        if selected_index:
            self.current_track = selected_index[0]
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if _name_ == "_main_":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
