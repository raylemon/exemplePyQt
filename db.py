import sqlite3
from sqlite3 import Error


def connect(db_file, err_callback):
    """
    Connexion à la db
    :param db_file: le nom du fichier db
    :param err_callback: traitement du message d’erreur
    :return: objet de connexion
    """
    connect = None
    try:
        connect = sqlite3.connect(db_file)
    except Error as e:
        err_callback(e)
    return connect


def create_tables(connect: sqlite3.Connection, err_callback):
    """
    Crée les 2 tables requises pour le projet
    :param connect: Objet de connexion à la db
    """

    sql_projects = """create table if not exists T_PROJECTS
(
    ID_PROJECT         INTEGER primary key autoincrement,
    NAME_PROJECT       TEXT not null unique,
    DATE_BEGIN_PROJECT TEXT,
    DATE_END_PROJECT   TEXT
); """

    sql_tasks = """create table T_TASKS
(
    ID_TASK         INTEGER primary key autoincrement,
    NAME_TASK       TEXT not null,
    FK_ID_PROJECT   INTEGER references T_PROJECTS (ID_PROJECT) on delete cascade,
    DATE_BEGIN_TASK TEXT,
    DATE_END_TASK   TEXT
); """

    try:
        connect.execute(sql_projects)
        connect.execute(sql_tasks)
    except Error as e:
        err_callback(e)


def create_project(conn: sqlite3.Connection, p_name: str, p_date_b: str, p_date_e: str, err_callback):
    sql = """insert into T_PROJECTS (NAME_PROJECT, DATE_BEGIN_PROJECT, DATE_END_PROJECT) values (?,?,?)"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (p_name, p_date_b, p_date_e))
        conn.commit()
        return cursor.lastrowid  # n° de clé primaire
    except Error as e:
        err_callback(e)
