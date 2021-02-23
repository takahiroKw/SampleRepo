import time

class MyTimer:
    start_time: int
    timer_status: str

    def __init__(self):
        self.start_time = 0
        self.timer_status = "STOP"


    def sta_timer(self):
        self.timer_status = "START"
        self.start_time = time.time_ns()

    def stp_timer(self):
        if timer_status == "START":
            elapsed_time: int  = time.time_ns() - start_time
            print("<< 経過時間：{} ns >>".format(elapsed_time))
            self.timer_status = "STOP"
            self.start_time = 0
        else:
            print("<< 経過時間を測定できません >>")
            self.timer_status = "STOP"
            self.start_time = 0

import csv

class MyCsv:
    g_file_path: str
    g_header_row: int

    def __init__(self, file_path : str, header_row : int):
        self.g_file_path = file_path
        self.g_header_row = header_row

    def get_collomn(self, col: int):
        retval: list
        with open(self.g_file_path, "r", encoding="utf_8_sig") as f:
            csv_reader = csv.reader(f, delimiter=",")

            # CSVの記載内容を2次元リストに格納
            content_list = [row for row in csv_reader]

            # 指定列数が開いているCSVとあっているか？
            if col < len(content_list[0]):
                # 2次元リストから指定列だけ取り出して新たなリストに代入
                col_data = [data[col] for data in content_list]

                # 指定列(ヘッダ情報はのぞく)の情報だけ格納されたリストを返却
                retval =  col_data[self.g_header_row:]
            # 指定の列が大きすぎたら何も返さない
            else:
                print("指定の要素数が大きすぎます")
                retval = []

        return retval

    def writeCharactor(self, add_chara_list: list):
        print(add_chara_list)
        with open(self.g_file_path, "a", encoding="utf_8_sig", newline="") as f:
            writer = csv.writer(f)
            # 現状、所属情報は未対応なので"-"を書き込む
            add_elm = [[add_chara, "-"] for add_chara in add_chara_list]

            print(add_elm)

            writer.writerows(add_elm)
        





