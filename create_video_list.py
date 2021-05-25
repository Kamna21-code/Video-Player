# importing necessary modules
import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
import pygame

play_list = [] # creating a global variable of list

def set_text(text_area, content): # inserts content into text area
    text_area.delete("1.0", tk.END)  # existing content is deleted
    text_area.insert(1.0, content)  # new content iss added


class CreateVideoList(): #creating a new class
    def __init__(self, root):
        if root == None:
            window = tk.Tk()
            fonts.configure()
            pygame.init()
            pygame.mixer.init()
        else:
            window = tk.Toplevel(root)

        window.geometry("750x350")
        window.title("Create Video List") # creates a title on the GUI

        enter_video_num = tk.Label(window, text="Enter Video Number") # enters video number
        enter_video_num.grid(row=0, column=1, padx=10, pady=10) # sets the box area

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_to_list = tk.Button(window, text="Add to Playlist",command = self.add_to_playlist) # add to list button
        add_to_list.grid(row=0,column=3,padx=10,pady=10)

        play_button = tk.Button(window, text="Play",command = self.play_button) # play button
        play_button.grid(row=0, column=4, padx=10, pady=10)

        pause_button = tk.Button(window, text = "Stop",command = self.stop) # stop button
        pause_button.grid(row=0, column=5, padx=10, pady=10)

        reset_button = tk.Button(window,text = "Reset",command=self.clear_button) # reset button
        reset_button.grid(row=2, column=2, padx=10, pady=10)

        self.playlist_txt= tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        if root == None:
            window.mainloop()

    def add_to_playlist(self): # This function adds the video to playlist
        key = self.input_txt.get() # Taking input from user
        name = lib.get_name(key)  # getting name from key
        if name is not None:
            new_list = name + "\n"
            play_list.append(new_list) # adding new videos to the playlist
            set_text(self.playlist_txt," ".join(play_list))
            self.status_lbl.configure(text="Add to Playlist button was clicked!")
        else:
            set_text(self.playlist_txt, f"Video {key} not found")


    def play_button(self): # This function palys the video
        key = self.input_txt.get() # getting key from user
        name = lib.get_name(key)
        name = name + "\n"
        dict_name = {}
        for i in play_list:
            dict_name[i] = 0
        dict_name[name] = dict_name[name] + 1 #increasing play count
        set_text(self.video_txt, "{} count = {}".format(name, dict_name[name]))
        self.status_lbl.configure(text="Play Next!")

    def clear_button(self):
        try:
            play_list.clear()
            to_clear = self.playlist_txt.delete("1.0", tk.END) # clears the text area
            set_text(self.playlist_txt, to_clear)
            self.status_lbl.configure(text="Reset All!")
        except:
            pass

    def stop(self):
        try:
            self.status.set("-Stopped") # stops the currently playing song
            pygame.mixer.music.stop()
            set_text(self.playlist_txt)
            self.status_lbl.configure(text="Stop!")
        except:
            pass

if __name__ == "__main__":
    CreateVideoList(None)
