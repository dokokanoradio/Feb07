from datetime import date, timedelta

# 改良版プログラム2
# 第1回から416260回目までの放送日の内、
# 誕生日(2/7)の放送かつ●十歳の節目の年かつ、
# 放送が●00回目or●50回目

# コンフィグ値
PROGRAM_START = date(2022, 4, 1)  # 放送開始日
PROGRAM_END = date(9999, 12, 31)  # 探索する最後の放送日
BIRTH_DATE = date(1995, 2, 7)  # パーソナリティの生年月日(誕生日)

# 自動で計算
# 第MAX_COUNT回まで調べる
MAX_COUNT = ((PROGRAM_END - PROGRAM_START).days // 7) + 1


# 便利な関数
# i回目の放送日を求める
def get_broadcast_date(i):
    # 初回は1なのでi回目はi-1週間後
    offset = i - 1
    return PROGRAM_START + timedelta(weeks=offset)


# 引数で渡した放送日が誕生日であるか？
def is_broadcast_on_birthday(date):
    # 安直に月と日が一致すれば良い
    return (date.month == BIRTH_DATE.month) and (date.day == BIRTH_DATE.day)


# date時点でのパーソナリティの年齢を求める
# ただしyearしか見ないので注意(誕生日であることを確認してから使うこと)
def get_age(date):
    # 今回の目的ではyearのみを使えばよい
    return date.year - BIRTH_DATE.year


# プログラムココからスタート

# 1回目からMAX_COUNT回目までの放送日を列挙
for i in range(1, MAX_COUNT + 1):
    date = get_broadcast_date(i)

    # 誕生日か？
    if is_broadcast_on_birthday(date):
        age = get_age(date)

        # ●十歳→1の位が0→10で割った余りが0
        if age % 10 == 0:
            # 放送回数を50で割った余りが０
            # 50→100→150→200・・・と50の倍数
            if i % 50 == 0:
                print(f"{date}:{i}回目:{age}歳")
