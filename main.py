import tkinter as tk

root = tk.Tk()
root.title("Kiseki TTS ATB Tracker")

window_width = 400
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set window to be not resizable
root.resizable(False, False)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

# actors = []

# actor_num = int(input("Enter number of actors: "))

# for i in range(actor_num):
#     actor_name = input("Actor " + str(i) + " name: " )
#     actor_SPD = int(input("Actor SPD: "))

#     actors.append([actor_name, actor_SPD])

# actors.sort(key=lambda x: x[1])


# print(actors)