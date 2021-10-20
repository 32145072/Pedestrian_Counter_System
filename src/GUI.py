#import
import tkinter as tk
from tkinter import Button, Widget, font
from tkinter.constants import BOTTOM, CENTER, COMMAND, LEFT, N, NE, S, TOP, TRUE, UNDERLINE, W
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import ttk

#==================
#   関数定義(event類)
#==================
def changePage(page):
    # MainPageを上位層にする
    page.tkraise()

def touch_text_tapped(): 
    messagebox.showinfo("info","画面をタップしました。")

#================   
#
#================ 
def main() -> None:
    #基盤
    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Pedestrian_Counter_System") #window title

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    #==============
    #   home画面
    #==============

    home = tk.Frame(root)

    help_button = tk.Button(
            home,
            text="<< Help >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : changePage(help_page)     #ボタンが押されたら
        )
    date_text = tk.Label(
        home,
        text = "\n\tx月y日の通行回数は\n",
        font = tkFont.Font(family="Arial",size=50)

    )
    count_text = tk.Label(
        home,
        text = "XXX",
        font = tkFont.Font(family="Arial",size=140)
        
    )
    touch_text = tk.Button(
        home,
        text = "\n\n\n画面をタップしてください",
        font = tkFont.Font(family="Arial",size=40,underline=TRUE),
        width=80,height=20,
        border = 0,
        command = touch_text_tapped
    )

    home.grid(row=0, column=0, sticky="nsew")

    #================
    #   home_widget配置
    #================
    help_button.pack(
        anchor = NE
    )
    date_text.pack(
        anchor= W
    )
    count_text.pack(
        anchor= CENTER
    )
    touch_text.pack(
        anchor= S
    )

    #==============
    #   help画面
    #==============

    help_page = tk.Frame(root)

    help_test_text = tk.Label(
        help_page,
        text = "ここはヘルプページです",
        font = tkFont.Font(family="Arial",size=30)
        
    )

    #========================
    #   help_widget配置
    #========================

    help_test_text.pack(
        anchor=CENTER
    )

    #=============
    #   画面配置
    #=============

    # help_pageを配置
    help_page.grid(row=0, column=0, sticky="nsew")

    # homeを上位層にする
    home.tkraise()

    # プログラムを始める
    root.mainloop()


#===============
# 本体処理  (プログラム起動したときに実行)
#===============
if __name__ == "__main__":
    main()