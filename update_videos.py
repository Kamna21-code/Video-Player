import tkinter as tk
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideo():
    def __init__(self, root):
        if root == None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)


        window.geometry("750x350")
        window.title("Update Videos")

        enter_video_num = tk.Label(window, text="Enter Video Number") # enters video number
        enter_video_num.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_rating = tk.Label(window, text="Enter New Rating") # enters rating
        enter_rating.grid(row=0, column=3, padx=10, pady=10)

        self.input_txt_rating = tk.Entry(window, width=3)
        self.input_txt_rating.grid(row=0, column=4, padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        add_new_rating = tk.Button(window, text="Add",command = self.add_rating)  # add new rating button
        add_new_rating.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        if root == None:
            window.mainloop()

    def add_rating(self): # adds new rating to the song
        key = self.input_txt.get()
        name = lib.get_name(key)
        rating = lib.get_rating(key)
        if name is not None:
            play_count = lib.set_rating(key,rating) # gets key and rating from the user
            new_rating = self.input_txt_rating.get() # sets new rating
            video_details = f"{name}\nrating: {new_rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
            self.status_lbl.configure(text="Enter New Rating was clicked!")
        else:
            set_text(self.video_txt, f"Video {key} not found")


if __name__ == "__main__":
    UpdateVideo(None)
