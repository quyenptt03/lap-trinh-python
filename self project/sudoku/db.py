from tkinter import *
import pyodbc


connectionString = '''DRIVER={ODBC Driver 17 for SQL Server}; 
                        SERVER=.;DATABASE=SudokuManagement;UID=sa;PWD=sa;Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()

def get_all_puzzle():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''select * from SudokuPuzzle'''
        cursor.execute(select_query)

        records = cursor.fetchall()

        close_connection(connection)

        return records

    except(Exception, pyodbc.Error) as error:
        print("Co loi xay ra", error)

def get_puzzle_by_id(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''select * from SudokuPuzzle where PuzzleID = ?'''
        params = (id)
        cursor.execute(select_query, params)

        record = cursor.fetchone()

        close_connection(connection)
        return record

    except(Exception, pyodbc.Error) as error:
        print("Co loi xay ra", error)

def get_puzzle_solution_by_puzzle_id(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''select * from SudokuGameState where PuzzleID = ?'''
        params = (id)
        cursor.execute(select_query, params)

        record = cursor.fetchone()

        close_connection(connection)
        return record
        
    except(Exception, pyodbc.Error) as error:
        print('co loi xay ra', error)

def update_win_puzzle(id, completed_time):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''update SudokuPuzzle 
                            set Completed = 1, CompletedTime = ?
                            where PuzzleID = ?'''
        params = (completed_time, id)
        cursor.execute(select_query, params)
        connection.commit()

        close_connection(connection)
        return 1
    except(Exception, pyodbc.Error) as error:
        print("co loi", error)
        return 0