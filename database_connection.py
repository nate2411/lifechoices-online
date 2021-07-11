import mysql.connector

my_database = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost', database='my_database')


# ID and phone number be be a string
def create_visitor_table():
    query = "CREATE TABLE visitor ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "surname varchar(50) NOT NULL, " \
            "id_number varchar(13) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "logged_in tinyint NOT NULL, " \
            "time_in varchar(50) NOT NULL, " \
            "time_out varchar(50) DEFAULT 'null' NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()


# Make visitor foreign key
def create_admin_table():
    #     IF THE TABLE DOESNT EXIST, CREATE IT
    query = "CREATE TABLE admins ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "email varchar(50) NOT NULL, " \
            "password varchar(50) NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()


def create_nok_table():
    query = "CREATE TABLE next_of_kin ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "visitor_id int unsigned NOT NULL, " \
            "PRIMARY KEY (id), " \
            "FOREIGN KEY (visitor_id) REFERENCES visitor(id) ); "

    my_cursor = my_database.cursor()
    my_cursor.execute(query)


def insert_visitor(name, surname, id_number, phone_number, logged_in, time_in):

    query = "INSERT INTO visitor ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + id_number + "', '" + phone_number + "', '" + str(logged_in) + "', '" + str(time_in) + "' );"

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()

def insert_nok(name, phone_number, visitor_id):
    query = "INSERT INTO next_of_kin ( name ,phone_number, visitor_id ) " \
            "VALUES ( '" + name + "', '" + phone_number + "', '" + str(visitor_id) + "' );"

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()


def insert_admin(name, email, password):
    query = "INSERT INTO admins ( name ,email ,password ) " \
            "VALUES ( '" + name + "', '" + email + "', '" + password + "' );"

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()


def delete_entry(table_name, column_name, id):
    query = "DELETE FROM " + table_name + " WHERE " + column_name + " = " + id + ";"
    print(query)

    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    my_database.commit()


def read_table(table_name):
    my_cursor = my_database.cursor()
    my_cursor.execute('SELECT * FROM ' + table_name)

    return my_cursor.fetchall()


def describe_table(table_name):
    my_cursor = my_database.cursor()
    my_cursor.execute('DESCRIBE ' + table_name)

    for i in my_cursor:
        print(i)


def show_tables():
    my_cursor = my_database.cursor()
    my_cursor.execute('SHOW TABLES')

    for i in my_cursor:
        print(i)


def drop_table(table_name):
    my_cursor = my_database.cursor()
    my_cursor.execute('DROP TABLE ' + table_name)


def select_from_table(query):
    my_cursor = my_database.cursor()
    my_cursor.execute(query)

    return my_cursor.fetchall()
