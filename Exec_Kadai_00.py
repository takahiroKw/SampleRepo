from util import MyTimer

def exec_kadai_00(sub_num: int):
    if sub_num == 1:
        exec01()

    elif sub_num == 2:
        exec02()

    elif sub_num == 3:
        exec03()

    elif sub_num == 4:
        exec04()

    elif sub_num == 5:
        exec05()

    elif sub_num == 6:
        exec06()

    else:
        print('課題00にそのSUB番号はありません')
   

def exec01():
    print("========= 課題00-1 =========")

    name1:str = "ねずこ"
    name2:str = "ぜんいつ"

    print("{}と{}は仲間です".format(name1, name2))

def exec02():
    print("========= 課題00-2 =========")

    name1:str = "ねずこ"
    name2:str = "むざん"

    if name1 != "むざん":
        print("{}は仲間です".format(name1))
    else:
        print("{}は仲間ではありません".format(name1))
    
    if name2 != "むざん":
        print("{}は仲間です".format(name2))
    else:
        print("{}は仲間ではありません".format(name2))

def exec03():
    print("========= 課題00-3 =========")

    names:str = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]

    names.append("ぜんいつ")

    print(names)

def exec04():
    names:str = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]

    names.append("ぜんいつ")

    for name in names:
        print(name)
    
def exec05():
    child_func05()

def exec06():
    sum06(input('検索するキャラ名を入力：'))

# 以下、子関数
def child_func05():
    print("子関数を呼び出しました")
   
def sum06(input_name:str):
    # 処理時間測定開始
    MyTimer.sta_timer()

    names:str = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]

    names.append("ぜんいつ")

    if input_name in names:
        print('{}は含まれます'.format(input_name))
    else:
        print('{}は含まれていません'.format(input_name))
    
    # 処理時間測定終了
    MyTimer.stp_timer()

