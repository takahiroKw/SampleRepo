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

    names:str = ["たんじろう", "ぎゆう","ねずこ","むざん"]

    names.append("ぜんいつ")

    print(names)

def exec04():
    names:str = ["たんじろう", "ぎゆう","ねずこ","むざん"]

    names.append("ぜんいつ")

    for name in names:
        print(name)
    
def exec05():
    child_func05()

def exec06():
    print("1 + 3 = {}".format(str(sum06(1, 3))))

# 以下、子関数
def child_func05():
    print("子関数を呼び出しました")
   
def sum06(a:int, b:int):
    return a + b
   