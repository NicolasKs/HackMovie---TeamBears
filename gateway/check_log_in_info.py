import sqlite3
from utils.constants.queries_check_log_in_info import CHECK_LOG_IN_INFO


def check_log_in_info_gateway(login_info):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(CHECK_LOG_IN_INFO, login_info)
    result = cursor.fetchall()
    connection.commit()
    connection.close()

    if len(result) == 0:
        raise ValueError('Wrong user name or password')

    return result
