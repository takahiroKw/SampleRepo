import Exec_Kadai_00

while True:
    input_kadai_num: int = int(input('\n課題番号の入力(0で終了します): '))

    if input_kadai_num == 0:
        print("終了します")
        break
        
    elif input_kadai_num == 1:
        Exec_Kadai_00.exec01()

    elif input_kadai_num == 2:
        Exec_Kadai_00.exec02()

    elif input_kadai_num == 3:
        Exec_Kadai_00.exec03()

    elif input_kadai_num == 4:
        Exec_Kadai_00.exec04()

    elif input_kadai_num == 5:
        Exec_Kadai_00.exec05()

    elif input_kadai_num == 6:
        Exec_Kadai_00.exec06()

    else:
        print("Error 終了します")
        break
