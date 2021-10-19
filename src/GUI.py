#This is create GUI code

#import 
import tkinter as tk
from tkinter import font
from tkinter.constants import BOTTOM, LEFT, NE, S, TOP, W
from tkinter import messagebox
from typing import Sized

#基盤
root = tk.Tk()
root.geometry(
    # "480x320"
    "1920x1080"
)
root.title("Pedestrian_Counter_System") #window title

#events
def help_btn_clicked():  #ヘルプボタンが押されたときの処理
    messagebox.showinfo("タイトル", "ボタンがクリックされました")   

#widget
help_button = tk.Button(
    root,
    text="help",
    font = (font.ROMAN,"30"),
    width=10,height=1,
    border=1,
    command= help_btn_clicked     #ボタンが押されたら
)
date_text = tk.Label(
    root,
    text = "x月y日の通行回数は",
    font = (font.ROMAN,"40")

)
count_text = tk.Label(
    root,
    text = "XXX",
    font = (font.ROMAN,"120")
    
)
touch_text = tk.Label(
    root,
    text = "画面をタップしてください"
    
)
#widgetの配置
help_button.pack(
    anchor = NE
)
date_text.pack(
    anchor=W
)
count_text.pack(
    anchor="center"
)
touch_text.pack(
    side= BOTTOM
)

#アプリ実行
root.mainloop()

