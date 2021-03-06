import time
import mysql.connector as connector

HOST = "192.168.1.93"
PORT = 3306
USER = "root"
PASSWORD = "abcd1234"
DB = "open_codes"


def exec_sql(sql):
    try:
        connection = connector.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
        cursor = connection.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        cursor.close()
        connection.close()
        return values
    except Exception as e:
        return "ERROR : " + str(e)


class OldOpenCode:
    def __init__(self, t_game_unique_id, t_game_issue_no, t_open_code):
        self.game_unique_id = t_game_unique_id
        self.game_issue_no = t_game_issue_no
        self.open_code = t_open_code


def get_old_open_codes(t_game_unique_id, start):
    if game_unique_id.startswith("HF_"):
        pattern = "select * from lottery_result.%s where game_unique_id='%s' AND modify_time>=DATE_ADD(NOW(),INTERVAL -2 DAY) AND open_code IS NOT NULL limit %d,%d"
        sql = pattern % (t_game_unique_id, t_game_unique_id, start, start + 1)
    else:
        pattern = "select * from lottery_result.LF where game_unique_id='%s' AND modify_time>=DATE_ADD(NOW(),INTERVAL -2 DAY) AND open_code IS NOT NULL limit %d,%d"
        sql = pattern % (t_game_unique_id, start, start + 1)
    results = exec_sql(sql)
    old_data = []
    for result in results:
        # print(result)
        data = OldOpenCode(result[1], result[6], result[2])
        old_data.append(data)
    return old_data


class NewOpenCode:
    def __init__(self, t_game_unique_id, t_game_issue_no, t_open_code, t_source):
        self.game_unique_id = t_game_unique_id
        self.game_issue_no = t_game_issue_no
        self.open_code = t_open_code
        self.source = t_source


def get_new_open_codes(t_game_unique_id, t_game_issue_no):
    pattern = "select * from open_codes.open_record where game_unique_id='%s' and game_issue_no='%s'"
    sql = pattern % (t_game_unique_id, t_game_issue_no)
    results = exec_sql(sql)
    new_data = []
    for result in results:
        # print(result)
        data = NewOpenCode(result[1], result[2], result[3], result[7])
        new_data.append(data)
    return new_data


game_unique_id_list = [
    "HF_CQSSC", "HF_XJSSC", "HF_TJSSC","HF_AHD11", "HF_GDD11",
    "HF_JXD11", "HF_SDD11", "HF_SHD11","HF_AHK3", "HF_GXK3",
    "HF_JSK3", "HF_BJK3", "HF_JLK3","HF_GDKL10F", "HF_CQKL10F",
    "HF_BJPK10", "HF_XYFT","HF_BJ28","HF_SHSSL","MARK_SIX",
    "PL3", "X3D", "QXC"
]

for game_unique_id in game_unique_id_list:
    start = 0
    old_results = get_old_open_codes(game_unique_id, start)
    while old_results is not None:
        start = start + 1
        try:
            game_issue_no = old_results[0].game_issue_no
            old_open_code = old_results[0].open_code.decode('utf-8')
        except Exception as e:
            print("没有更多数据了")
            break
        new_results = get_new_open_codes(game_unique_id, game_issue_no)
        for new_result in new_results:
            new_open_code = new_result.open_code
            source = new_result.source
            if old_open_code == new_open_code:
                pattern = "彩种 [%s] 期号 [%s] 数据源 [%s] 测试通过"
                notice = pattern % (game_unique_id, game_issue_no, source)
                print(notice)
            else:
                pattern = "测试未通过, 彩种 [%s] 期号 [%s] 实际开奖结果 [%s]，数据源 [%s] 抓取的结果 [%s] **********************************"
                notice = pattern % (game_unique_id, game_issue_no, old_open_code, source, new_open_code)
                print(notice)
        old_results = get_old_open_codes(game_unique_id, start)
        time.sleep(0.5)
