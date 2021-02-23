from util import MyTimer

# 課題01で使用するリスト
g_source: str = ["たんじろう", "ぎゆう", "ねずこ", "むざん", "ぜんいつ"]

# CSVファイルのパス
CHAR_LIST_CSV: str = "Data/kadai01_charaList.csv"

# 課題01のメイン制御関数
def exec_kadai_01(sub_num: int):
    if sub_num == 1:
        exec01()

    elif sub_num == 2:
        exec02()

    elif sub_num == 3:
        exec03()

    elif sub_num == 4:
        exec04()

    else:
        print('課題00にそのSUB番号はありません')
   
# 課題01-01の実行関数
def exec01():
    global g_source
    input_name = input("検索するキャラクター名を入力してください：")

    # 処理時間測定開始
    MyTimer.sta_timer()

    chk: bool = False
    # kadai 00-6でやったように 「if ** in XX」 の方がすっきりするが、違うやり方で
    for name in g_source:
        if name == input_name:
            chk = True
            break
        else:
            pass

    if chk == True:
        print("{}がキャラクターリストの中に見つかりました".format(input_name))
    else:
        print("{}は見つかりませんでした".format(input_name))

    # 処理時間測定終了
    MyTimer.stp_timer()

# 課題01-02の実行関数
def exec02():
    global g_source

    input_name = input("検索するキャラクター名を入力してください：")

    # 処理時間測定開始
    MyTimer.sta_timer()

    if input_name in g_source:
        print("{}がキャラクターリストの中に見つかりました".format(input_name))
    else:
        print("{}は見つからなかったので、リストに追加します".format(input_name))
        g_source.append(input_name)
        print("リストは次のようになりました：{}".format(g_source))
    
    # 処理時間測定終了
    MyTimer.stp_timer()



from util import MyCsv

# 課題01-03の実行関数
def exec03():
    global g_source

    print("現在のリストの内容は次の通りです")
    print(g_source)

    print("kadai01_charaList.csvから読み出します")
    my_csv = MyCsv(CHAR_LIST_CSV, 1)

    # 「名前」は最初の列に格納
    name_csv = my_csv.get_collomn(0)

    for name in name_csv:
        print("{}を確認中".format(name))
        if name in g_source:
            print("\t既に登録済みで格納しません")
        else:
            g_source.append(name)
            print("\t格納しました")

    print("現在のリストの内容は次の通りです")
    print(g_source)

# 課題01-04の実行関数
def exec04():
    global g_source

    add_charactors: list = []
    my_csv = MyCsv(CHAR_LIST_CSV, 1)

    print("------ 現在のリストとCSVを同期します ------")
    name_csv = my_csv.get_collomn(0)

    for name in name_csv:
        if name in g_source:
            pass
        else:
            g_source.append(name)

    print("------ 同期しました -------")

    while True:
        num: int = int(input("選択してください(0：リスト追加、1:CSVにリストの内容を書き込み、-1:終了: "))
        if num == 0:
            add_chara = input("追加したいキャラクター名を入力してください: ")

            # リストに追加
            g_source.append(add_chara)
            # CSV反映用に別途追加したのだけ保存
            add_charactors.append(add_chara)
            print("リストに追加しました。")
            print("現在のリストの内容は次の通りです")
            print(g_source)
        
        elif num == 1:
            if  not add_charactors:
                print("追加されるキャラクターがいません")
            else:
                print(add_charactors)
                my_csv.writeCharactor(add_charactors)
                add_charactors = []     # 空にしておく
                print("CSVに追加しました")

        else:
            print("終了します")
            break











