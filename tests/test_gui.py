#This is create GUI code
#author: 32145072

"""
初期バージョン
"""

#import 
import tkinter as tk
from tkinter import Button, Widget, font
from tkinter.constants import BOTTOM, CENTER, COMMAND, LEFT, N, NE, S, TOP, TRUE, UNDERLINE, W
from tkinter import messagebox
import tkinter.font as tkFont

#home画面
class Gui(tk.Frame):

    def __init__(self,root=None):
        super().__init__(root,
        width=1920,height=1080,)
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

#widget作成
    def create_widgets(self):
        #events
        # def help_btn_clicked():  #ヘルプボタンが押されたときの処理
            
        #     messagebox.showinfo("info", "ヘルプボタンが押されました")   

        def touch_text_tapped(): 
            messagebox.showinfo("info","画面をタップしました。")
        #create_widgets
        help_button = tk.Button(
            self,
            text="<< Help >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= self.create_help     #ボタンが押されたら
        )
        date_text = tk.Label(
            self,
            text = "\n\tx月y日の通行回数は\n",
            font = tkFont.Font(family="Arial",size=50)

        )
        count_text = tk.Label(
            self,
            text = "XXX",
            font = tkFont.Font(family="Arial",size=140)
            
        )
        touch_text = tk.Button(
            self,
            text = "\n\n\n画面をタップしてください",
            font = tkFont.Font(family="Arial",size=40,underline=TRUE),
            width=80,height=20,
            border = 0,
            command = touch_text_tapped
        )
        #widgetの配置
        help_button.pack(anchor = NE)
        date_text.pack(
            anchor= W
        )
        count_text.pack(
            anchor= CENTER
        )
        touch_text.pack(
            anchor= S
        )
    def create_help(self):
        help = tk.Toplevel(self.root)
        help.title("Pedestrian_Counter_System's help page")
        help.geometry("1920x1080")

        help_text = tk.Label(
            self,
            text = "XXX",
            font = tkFont.Font(family="Arial",size=140)
        )
        help_text.pack(
            side = TOP
        )

            

#基盤
root = tk.Tk()
root.geometry("1920x1080")
root.title("Pedestrian_Counter_System") #window title

app = Gui(root=root)
app.mainloop() #アプリ実行
