import psycopg2
import logging
from allure import step



class POSTGRESQL:
    def __del__(self):
        self.connection.close()

    def __init__(self, host='', db_user='', db_password='', db_database='', port=''):
        self.log = logging.getLogger(__name__)

        params = {
            "host": host,
            "user": db_user,
            "password": db_password,
            "database": db_database,
            "port": port
        }
        self.connection = psycopg2.connect(**params)

    def select(self, execution):
        result = ""

        with step(execution):
            self.log.debug(execution)
            with self.connection as conn:
                cursor = conn.cursor()
                cursor.execute(execution)
                result = cursor.fetchone()

        return result

    def select_list(self, execution):
        result = ""

        with step(execution):
            self.log.debug(execution)
            with self.connection as conn:
                cursor = conn.cursor()
                cursor.execute(execution)
                result = cursor.fetchall()

        return result

    def get_article(self, id):
        try:
            query = f"SELECT * FROM public.article WHERE id = {id};"
            existed_id = self.select(query)
            result = existed_id
        except TypeError as ex:
            self.log.debug(f"Нет записей в базе с таким ID: {id}")
            result = None
        return result

    def get_dict_of_values(self):
        try:
            query = f"SELECT * FROM public.article;"
            values = self.select_list(query)
            dict_values = {i[0]: [i[1], i[2], i[3], i[4]] for i in values}
        except TypeError as ex:
            self.log.debug(f"Произошла ошибка {ex}")
            dict_values = None
        return dict_values



if __name__ == '__main__':
    con = POSTGRESQL(db_url='localhost', db_user='postgres', db_password='pass1', db_database='postgres', port='10432')
    res = con.get_dict_of_values()
    print(res)
