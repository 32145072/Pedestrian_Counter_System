def create_graphs():
    #   ------- import -------
    import matplotlib.pyplot as plt
    import japanize_matplotlib      # これがないと日本語が文字化けする
    import os                      # ファイル保存用のpath指定
    from more_itertools import chunked    # リストを等分
    #import MySQLdb
    from matplotlib.ticker import MaxNLocator

    #   ------- 宣言 -------
    """
    conn = MySQLdb.connect(
        user='ユーザー名',
        passwd='パスワード名',
        host='ホスト名',
        db='データベース名')
    cur = conn.cursor()
    sql = "select * from データベース名"
    cur.execute(sql)
    rows = cur.fetchall()        # データ群
    """
    from random import randint
    rows = []
    c = 0
    for i in range(1,31):
        for ii in range(24):
            c+=1
            rows.append(c)
            rows.append(2021)
            rows.append(1)
            rows.append(i)
            rows.append(ii)
            rows.append(randint(0, 100))
            rows.append(randint(0, 100))
            rows.append(randint(0, 100))
            rows.append(randint(0, 100))

    rows = list(chunked(rows, 9))
    #print(rows)

    l1 = []
    for i in range(1,25):
        l1.append((rows[-i][1], rows[-i][2], rows[-i][3], rows[-i][4], rows[-i][5]))
    DATA_hour = sorted(l1)
    l2 = []
    for i in DATA_hour:
        l2.append(str(i[2])+'-'+str(i[3]))
    WIDTH_DATA_hour = list(chunked(l2, 6))   # 縦軸データ(時)
    
    l3 = []
    l4 = []
    cnt = 0
    while len(l3)!=28:
        cnt+=1
        if not (rows[-cnt][1], rows[-cnt][2], rows[-cnt][3]) in l3:
            l3.append((rows[-cnt][1], rows[-cnt][2], rows[-cnt][3]))
            l4.append((rows[-cnt][1], rows[-cnt][2], rows[-cnt][3], rows[-cnt][6]))
    DATA_day = sorted(l4)
    l5 = []
    for i in DATA_day:
        l5.append((str(i[1])+'-'+str(i[2])))
    WIDTH_DATA_day =  list(chunked(l5, 7))           # 縦軸データ(日)
    
    l6 = []         
    for i in DATA_hour:
        l6.append(i[4])
    LENGTH_DATA_hour = list(chunked(l6, 6))         # 横軸データ(時)
    
    l7 = []
    for i in DATA_day:
        l7.append(i[3])
    LENGTH_DATA_day = list(chunked(l7, 7))          # 横軸データ(日)
    
    save_dir = "src"
    
    png_num = 0    # 画像番号

    #   ------- 処理 -------
 
    # 時毎グラフ作成＆保存
    for i in zip(WIDTH_DATA_hour, LENGTH_DATA_hour):
        png_num+=1
        plt.rcParams["font.size"] = 14      # 全体の文字サイズの変更(デフォルトは12)
        fig,ax = plt.subplots(facecolor="white")    # キャンバスとxy軸で表す部分を作成
        ax.plot(i[0], i[1] ,marker='o')
        ax.set_xlabel("日-時")
        ax.set_ylabel("通行人数", rotation='vertical')
        ax.set_title("1時間毎")
        ax.grid()
        plt.show()
        fig.savefig(os.path.join(save_dir,"graph"+str(png_num)+".png"))

    # 日毎グラフ作成＆保存
    for i in zip(WIDTH_DATA_day, LENGTH_DATA_day):  
        png_num+=1
        plt.rcParams["font.size"] = 14
        fig,ax = plt.subplots(facecolor="white")
        ax.plot(i[0], i[1] ,marker='o')
        ax.set_xlabel("月-日")
        ax.set_ylabel("通行人数", rotation='vertical')
        ax.set_title("1日毎")
        ax.grid()
        plt.show()
        fig.savefig(os.path.join(save_dir,"graph"+str(png_num)+".png"))
        
if __name__ == "__main__":  #該当のファイルがコマンドラインからスクリプトとして実行された場合にのみ以降の処理を実行する
    create_graphs()


