import tkinter as tk
window = tk.Tk()
window.geometry("1920x1080")
window.title("画像表示")
canvas = tk.Canvas(window, bg="white", height=1920, width=1080)

canvas.place(x=0,y=0)

img = tk.PhotoImage(file="src\pic\help_1.png",width=1920,height=1080)
canvas.create_image(0,-30,image=img,anchor=tk.NW)

window.mainloop()