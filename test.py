import Exec_Kadai_00

def main():
    while True:
        input_kadai_num: int = int(input('\n課題番号の入力(-1で終了します): '))

        if input_kadai_num == -1:
            print("終了します")
            break
            
        elif input_kadai_num == 0:
            input_sub_num: int = int(input('課題のSUB番号を入力してください: '))

            Exec_Kadai_00.exec_kadai_00(input_sub_num)

        else:
            print("Error 終了します")
            break

main()
