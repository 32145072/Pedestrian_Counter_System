"""
ページ構成：
    home_page: 基本ウィンドウ。日付や通行回数の表示を行う
    help_page: ヘルプページ。画面の操作方法など？
    select_page: グラフページの切り替えを行う   小ウィンドウを出す感じ
    graph_page: dataをグラフ化したものを表示させる
"""

#import

import datetime as dt
import tkinter as tk
from tkinter import Button, Toplevel, Widget, font
from tkinter.constants import ACTIVE, BOTTOM, CENTER, COMMAND, LEFT, N, NE, NW, RIDGE, RIGHT, S, TOP, TRUE, UNDERLINE, W
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import ttk


#=========
#   変数
#=========

now_date = dt.datetime.now()
bg_color = "gray94" #default == gray94

open_select_window = False

#==================
#   関数定義(event類)
#==================
def change_page(page):  #画面遷移させる関数
    # 引数:pageを上位層にする
    page.tkraise()

def close_window(self):
    self.destroy()

def switchButtonState(self):
    if (self["state"] == tk.NORMAL):
        self["state"] = tk.DISABLED
    else:
        self["state"] = tk.NORMAL

def select_window(page,to):
    window = tk.Toplevel(page)
    window.geometry("720x480+600+250")
    window.protocol('WM_DELETE_WINDOW', (lambda: 'pass')()) #ウィンドウの右上の×を無効化
    close_button = tk.Button(
        window,
        text = "close",
        width=10,height=5,border=3,
        command = lambda : [close_window(window),switchButtonState(to)])
    hour_button = tk.Button(
        window,
        text="  Hour  ",
        font = tkFont.Font(family="Arial",size=30),
        pady=8,
        padx=90
    )
    day_button = tk.Button(
        window,
        text="  Day  ",
        font = tkFont.Font(family="Arial",size=30),
        pady=8,
        padx=95

    )
    week_button = tk.Button(
        window,
        text="  Week  ",
        font = tkFont.Font(family="Arial",size=30),
        pady=8,
        padx=80        
    )
    close_button.pack(anchor=NE)
    hour_button.pack(anchor=CENTER,pady=15)
    day_button.pack(anchor=CENTER,pady=20)
    week_button.pack(anchor=CENTER,pady=25)
    
    

def touch_text_tapped(): 
    messagebox.showinfo("info","画面をタップしました。")

#===================
#   create windows
#===================
def main_gui():
    #基盤
    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Pedestrian_Counter_System") #window title

    root.configure(bg=bg_color)

    #grid作成
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    #==============
    #   home画面
    #==============

    home_page = tk.Frame(root)
    home_page.configure(bg=bg_color)

    help_button = tk.Button(
            home_page,
            text="<< Help >>",
            font = tkFont.Font(family="Arial",size=40),
            bg = bg_color,
            activebackground=bg_color,  #ボタンを押したときの色
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(help_page)     #ボタンが押されたら
        )
    date_text = tk.Label(
        home_page,
        bg = bg_color,
        text = (f"\n\n\t{now_date.month}月{now_date.day}日の通行回数は"),
        font = tkFont.Font(family="Arial",size=50)
    )
    count_text = tk.Label(
        home_page,
        bg = bg_color,
        text = "XXX",
        font = tkFont.Font(family="Arial",size=140)
        
    )
    touch_text = tk.Button(
        home_page,
        bg = bg_color,
        activebackground=bg_color,
        text = "\n\n\n画面をタップしてください",
        font = tkFont.Font(family="Arial",size=40,underline=TRUE),
        width=80,height=20,
        border = 0,
        command = touch_text_tapped
    )

    home_page.grid(row=0, column=0, sticky="nsew")

    #========================
    #   home_page_widgets配置
    #========================
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
    help_page.configure(bg=bg_color)

    #create widgets
    help_test_text = tk.Label(
        help_page,
        bg = bg_color,
        text = "ここはヘルプページです",
        font = tkFont.Font(family="Arial",size=30)
    )

    home_button = tk.Button(
            help_page,
            bg = bg_color,
            activebackground=bg_color,
            text="<< Home >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(home_page)     #ボタンが押されたら
        )
    select_button = tk.Button(
            help_page,
            bg = bg_color,
            activebackground=bg_color,
            text="<< select >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(select_page)     #ボタンが押されたら
        )
    graph_button = tk.Button(
            help_page,
            bg = bg_color,
            activebackground=bg_color,
            text="<< graph >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(graph_page)     #ボタンが押されたら
        )

    #========================
    #   help_widgets配置
    #========================

    home_button.pack(
        anchor = NE
    )
    select_button.pack(
        anchor = NE        
    )
    graph_button.pack(
        anchor = NE
    )
    help_test_text.pack(
        anchor=CENTER
    )

    #===================
    #   select画面
    #===================
    select_page = tk.Frame(root)
    select_page.configure(bg=bg_color)

    #create widgets
    help_test_text = tk.Label(
        select_page,
        bg = bg_color,
        text = "ここはセレクトページです",
        font = tkFont.Font(family="Arial",size=30)
        
    )
    home_button = tk.Button(
            select_page,
            bg = bg_color,
            activebackground=bg_color,
            text="<< Home >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(home_page)     #ボタンが押されたら
        )

    help_button = tk.Button(
            select_page,
            bg = bg_color,
            activebackground=bg_color,
            text="<< Help >>",
            font = tkFont.Font(family="Arial",size=40),
            width=10,height=1,
            border=1,
            relief="groove",
            command= lambda : change_page(help_page)     #ボタンが押されたら
        )

    #========================
    #   select_widgets配置
    #========================
    home_button.pack(
        side=LEFT,
        anchor=NW
    )
    help_button.pack(
        side=RIGHT,
        anchor=NE,
    )
    help_test_text.pack(
        anchor=CENTER,
        pady=300
    )

    #==================
    #   graph画面
    #==================

    graph_page = tk.Frame(root)
    graph_page.configure(bg=bg_color)

    #create widgets
    graph_change_range = tk.Button(
        graph_page,
        bg = "grey30",
        fg = "white",
        text = "横軸の幅の変更",
        width=20,height=1,
        border=1,
        pady=5,
        relief="groove",
        font = tkFont.Font(family="Arial",size=35),
        command= lambda : [select_window(graph_page,graph_change_range),switchButtonState(graph_change_range)]
    )

    home_button = tk.Button(
        graph_page,
        bg = bg_color,
        activebackground=bg_color,
        text="<< Home >>",
        font = tkFont.Font(family="Arial",size=40),
        width=10,height=1,
        border=1,
        relief="groove",
        command= lambda : change_page(home_page)     #ボタンが押されたら
        )
    select_button = tk.Button(
        graph_page,
        bg = bg_color,
        activebackground=bg_color,
        text="<< select >>",
        font = tkFont.Font(family="Arial",size=40),
        width=10,height=1,
        border=1,
        relief="groove",
        command= lambda : change_page(select_page)    #ボタンが押されたら
            
        )

    #==================
    #   graph widget配置
    #==================

    home_button.pack(
        side=LEFT,
        anchor=NW
    )
    select_button.pack(
        side=RIGHT,
        anchor=NE,
    )
    graph_change_range.pack(
        pady=50,
        anchor=CENTER
    )

    #=============
    #   画面配置
    #=============

    # 作成したウィンドウを配置(処理的には,これを一番上に持ってくるようにすることで画面遷移させている)
    help_page.grid(row=0, column=0, sticky="nsew")
    select_page.grid(row=0, column=0, sticky="nsew")
    graph_page.grid(row=0, column=0, sticky="nsew")

    # home_pageを起動時に上位層にする
    home_page.tkraise()

    # プログラムを始める
    root.mainloop()


#===============
# 本体処理  (プログラム起動したときに実行)
#===============
if __name__ == "__main__":  #該当のファイルがコマンドラインからスクリプトとして実行された場合にのみ以降の処理を実行する
    main_gui()
