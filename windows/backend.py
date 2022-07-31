from configparser import ConfigParser
from mysql.connector import MySQLConnection
from mysql.connector import Error


def get_details():
    details = []
    config = ConfigParser()
    config.read("config.ini")
    host = config.get("database_details", "host")
    user = config.get("database_details", "user")
    password = config.get("database_details", "password")
    database = config.get("database_details", "database")
    details = (host, user, password, database)
    return details


def create_connection():
    details = get_details()
    try:
        conn = MySQLConnection(
            host=details[0], user=details[1], password=details[2], database=details[3])
        return conn
    except Error:
        print("Make sure that You have created the database or check your config.ini file")


def fetch_details(query, val=None):
    c = create_connection()
    cur = c.cursor()
    if c.is_connected():
        cur.execute(query, val)
        return cur.fetchall()
    else:
        print("Database is not connected")


def execute_query(query, val=None):
    c = create_connection()
    cur = c.cursor()
    cur.execute("set Sql_safe_updates=0;")
    c.commit()
    if c.is_connected():
        try:
            cur.execute(query, val)
            c.commit()
            return True
        except Error as e:
            print(e)
            return e
    else:
        print("Database Not updated")


def call_procedure(function, args=None):
    c = create_connection()
    cur = c.cursor()
    if c.is_connected():
        try:
            cur.callproc(function, args)
            c.commit()
            return True
        except Error as e:
            print(e)
    else:
        print("Not Connected")


if __name__ == "__main__":
    # call_procedure("getidofadmin()",(0,'char'))
    # call_procedure('addadmin',("Nidhi","boisar",7841904200,19,"Female"))
    execute_query(
        "insert into admin values (get_adminid(),'pra','dd',123,19,'m');")
