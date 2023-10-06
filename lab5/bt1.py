import pyodbc

connectionString = '''DRIVER={ODBC Driver 17 for SQL Server}; 
                        SERVER=.;DATABASE=QLSinhVien;UID=sa;PWD=sa;Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn
def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)

        records = cursor.fetchall()
        print(f"Danh sach cac lop la: ")
        for row in records:
            print('*'*50)
            print("Ma lop: ", row[0])
            print("Ten lop: ", row[1])

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print("Co loi", error)

def get_all_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select SinhVien.ID, HoTen, Lop.ID, TenLop from SinhVien, Lop where SinhVien.MaLop = Lop.ID"""
        cursor.execute(select_query)

        records = cursor.fetchall()
        print(f"Danh sach sinh vien la: ")
        print ("{:<8} {:<30} {:<10} {:<10}".format('Ma SV','Ten SV','Ma Lop','Ten lop'))
        for row in records:
            print ("{:<8} {:<30} {:<10} {:<10}".format(row[0],row[1],row[2],row[3]))

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi: ', error)

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop where id = ?"""
        params = (class_id)
        cursor.execute(select_query, params)
        
        records  = cursor.fetchone()

        print(f"Thong tin lop co id = {class_id} la: ")
        print("Ma lop: ", records[0])
        print("Ten lop: ", records[1])

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi: ', error)

def get_student_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from SinhVien where id = ?"""
        params = (student_id)
        cursor.execute(select_query, params)
        
        records  = cursor.fetchone()

        print(f"Thong tin sinh vien co id = {student_id} la: ")
        print("Ma SV: ", records[0])
        print("Ten SV: ", records[1])
        print("Ma lop: ", records[2])

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi: ', error)

def get_class_by_name(class_name:str):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop where TenLop = ?"""
        params = (class_name)
        cursor.execute(select_query, params)
        
        record  = cursor.fetchone()

        print(f"Thong tin lop co ten = {class_name} la: ")
        print("Ma lop: ", record[0])
        print("Ten lop: ", record[1])

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi: ', error)

def get_students_by_name_class(classID:int, name:str):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select SinhVien.ID, HoTen, Lop.ID 
                            from SinhVien,Lop 
                            where Lop.ID=? and HoTen like N'%'+?+'%'"""
        params = (classID, name)
        cursor.execute(select_query, params)

        records = cursor.fetchall()
        print ("{:<8} {:<30} {:<10}".format('Ma SV','Ten SV','Ma Lop'))
        for row in records:
            print ("{:<8} {:<30} {:<10}".format(row[0],row[1],row[2]))

        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print('co loi', error)

def insert_class(class_id, class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """Insert into Lop(ID, TenLop) values (?,?)"""
        params = (class_id, class_name)

        cursor.execute(select_query, params)
        connection.commit()
        print('da them thanh cong')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('co loi', error)

def delete_class(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """delete from Lop where ID=?"""
        params = (class_id)

        cursor.execute(select_query, params)
        connection.commit()
        print('da xoa thanh cong lop co id = ', class_id)

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('co loi', error)


def update_class(class_id, new_class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """update Lop 
                            set TenLop = ?
                            where ID = ?"""
        params = (new_class_name, class_id)

        cursor.execute(select_query, params)
        connection.commit()
        print('da xoa thanh cong lop co id = ', class_id)

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('co loi', error)

def insert_student(id, name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''exec InsertStudent @id=?, @HoTen=?, @MaLop=?'''
        params = (id, name, class_id)

        cursor.execute(select_query, params)
        connection.commit()
        print('da them sinh vien thanh cong')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print('co loi', error)
# get_all_class()
# get_all_student()
# get_class_by_id(1)
# get_student_by_id(2)
# get_class_by_name("CTK44B")
# get_students_by_name_class(3, 'Trung')
# insert_class(6, "CTK45C")
# delete_class(6)
# update_class(5, 'ctk45b')
# get_all_class()
insert_student(16, 'Nguyễn Thị CCC', 3)
get_all_student()