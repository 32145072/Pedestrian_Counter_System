#This is create GUI code

#import 
import tkinter as tk
from tkinter import Button, font
from tkinter.constants import BOTTOM, COMMAND, LEFT, NE, S, TOP, TRUE, UNDERLINE, W
from tkinter import messagebox
import tkinter.font as tkFont

#home画面

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

def touch_text_tapped():
    messagebox.showinfo("タイトル","画面をタップしました。")

#widget
help_button = tk.Button(
    root,
    text="help",
    font = tkFont.Font(family="Arial",size=40),
    width=10,height=1,
    border=1,
    command= help_btn_clicked     #ボタンが押されたら
)
date_text = tk.Label(
    root,
    text = "                x月y日の通行回数は",
    font = tkFont.Font(family="Arial",size=40)

)
count_text = tk.Label(
    root,
    text = "\nXXX",
    font = tkFont.Font(family="Arial",size=120)
    
)
touch_text = tk.Button(
    root,
    text = "\n\n\n画面をタップしてください",
    font = tkFont.Font(family="Arial",size=40,underline=TRUE),
    border = 0,
    command = touch_text_tapped
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
    anchor=S
)


#アプリ実行
root.mainloop()

