from datetime import date, timedelta

# ベースのプログラム(第1回から416260回目まで列挙)

# コンフィグ値
PROGRAM_START = date(2022, 4, 1)  # 放送開始日
PROGRAM_END = date(9999, 12, 31)  # 探索する最後の放送日

# 自動で計算
# 第MAX_COUNT回まで調べる
MAX_COUNT = ((PROGRAM_END - PROGRAM_START).days // 7) + 1


# 便利な関数
# i回目の放送日を求める
def get_broadcast_date(i):
    # 初回は1なのでi回目はi-1週間後
    offset = i - 1
    return PROGRAM_START + timedelta(weeks=offset)


# プログラムココからスタート

# 1回目からMAX_COUNT回目までの放送日を列挙
for i in range(1, MAX_COUNT + 1):
    date = get_broadcast_date(i)
    print(f"{date}:{i}回目")
