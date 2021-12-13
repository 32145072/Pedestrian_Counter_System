import test_codes

print(__name__)
print(test_codes.__name__)

if __name__ == "__main__":  #該当のファイルがコマンドラインからスクリプトとして実行された場合にのみ以降の処理を実行する
    print("a")