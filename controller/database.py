import psycopg2
from .bases.user import (User, UpdateUser)
import time

class DatabaseController(object):
    def __init__(self, config):
        self.user_table = config.get('users-table')
        self.passwd = config.get('password')
        self.user = config.get('user')
        self.db = config.get('database')
        self.host = config.get('host')
        self.port = config.get('port')
        try:
            self.conn = psycopg2.connect(host=self.host, database=self.db,
                                         user=self.user, password=self.passwd,
                                         port=self.port)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print(err)
            print("Error on connecting")
            exit(255)

    def reconnect(self):
        try:
            print("Reconnecting...")
            self.conn = psycopg2.connect(host=self.host, database=self.db,
                                         user=self.user, password=self.passwd,
                                         port=self.port)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print(err)
            print("Error on connecting")
            exit(255)

    def get_user(self, cpf):
        select_statement = f"select * from {self.user_table} where cpf = \'{cpf}\'"
        self.cursor.execute(select_statement)
        return self.cursor.fetchall()

    def get_users(self):
        select_statement = f"SELECT * FROM {self.user_table}"
        self.cursor.execute(select_statement)
        return self.cursor.fetchall()

    def add_user(self, user: User) -> bool:
        # self.reconnect()
        try:
            insert_statement = f"insert into {self.user_table}(cpf,nome,data_nascimento,cep," \
                               f"rua,bairro,cidade,estado) values" \
                               f"('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (user.cpf, user.nome,
                                                                                      user.data_nascimento,
                                                                                      user.cep, user.rua, user.bairro,
                                                                                      user.cidade, user.estado)
            self.cursor.execute(insert_statement)
            self.conn.commit()
            # self.close_conn()
            return True
        except Exception as err:
            print(err)
            print("Error on inserting")
            return False

    def update_user(self, user: UpdateUser):
        update_statement = ""
        user = user.dict()
        for k in user:
            if k != "cpf" and user[k]:
                update_statement += f"{k} = '{user[k]}',"

        try:
            # remove last comma
            update_statement = f"UPDATE {self.user_table} " \
                               f"SET {update_statement[:-1]}"
            self.cursor.execute(update_statement)
            self.conn.commit()
            # self.close_conn()
            return True
        except Exception as err:
            print(err)
            print("Error on update")
            return False

    def delete_user(self, cpf):
        try:
            delete_statement = f"DELETE FROM {self.user_table} WHERE cpf = '{cpf}'"
            self.cursor.execute(delete_statement)
            self.conn.commit()
            # self.close_conn()
            return True
        except Exception as err:
            print(err)
            print("Error on delete")
            return False

    def create_table(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.user_table} (cpf varchar(20) primary key, nome varchar(50) not null," \
              f"data_nascimento varchar(10) not null, cep varchar(10) not null, rua varchar(40) not null," \
              f"bairro varchar(40) not null, cidade varchar(30) not null," \
              f"estado varchar(40) not null)"

        for i in range(3):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                break
            except Exception as err:
                print("Error on creating table")
                print(err)
                time.sleep(5)

    def close_conn(self):
        self.cursor.close()
        self.conn.close()
