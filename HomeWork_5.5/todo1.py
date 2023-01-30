import psycopg2
conn = psycopg2.connect(database='test_base', user='postgres', password='12345')

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS cont_book(
                id SERIAL PRIMARY KEY, 
                name TEXT, 
                surname TEXT, 
                email TEXT, 
                phone TEXT
            );
            """)
        conn.commit()

def add_client(conn, first_name, last_name, email, phones=None):
    if phones == None:
        phones = ''
    with conn.cursor() as cur:   
        cur.execute(f"INSERT INTO cont_book(name, surname, email, phone) VALUES('{first_name}', '{last_name}', '{email}', '{phones}') RETURNING id;")
        conn.commit()


def add_phone(conn, id, phone):
    with conn.cursor() as cur:
        cur.execute("SELECT phone FROM cont_book WHERE id=%s;", (f"{id}",))
        old_phone = cur.fetchone()[0]
        cur.execute("UPDATE cont_book SET phone=%s WHERE id=%s;", (f'{old_phone}; {phone}', id))
        conn.commit()
    

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute("SELECT name FROM cont_book WHERE id=%s;", (f"{client_id}",))
            old = cur.fetchone()[0]
            cur.execute("UPDATE cont_book SET name=%s WHERE id=%s;", (f'{first_name}', client_id))
            conn.commit()
        if last_name != None:
            cur.execute("SELECT surname FROM cont_book WHERE id=%s;", (f"{client_id}",))
            old = cur.fetchone()[0]
            cur.execute("UPDATE cont_book SET surname=%s WHERE id=%s;", (f'{last_name}', client_id))
            conn.commit()
        if email != None:
            cur.execute("SELECT email FROM cont_book WHERE id=%s;", (f"{client_id}",))
            old = cur.fetchone()[0]
            cur.execute("UPDATE cont_book SET email=%s WHERE id=%s;", (f'{email}', client_id))
            conn.commit()
        if phones != None:
            cur.execute("SELECT phones FROM cont_book WHERE id=%s;", (f"{client_id}",))
            old = cur.fetchone()[0]
            cur.execute("UPDATE cont_book SET phones=%s WHERE id=%s;", (f'{phones}', client_id))
            conn.commit()


def delete_phone(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("UPDATE cont_book SET phone=%s WHERE id=%s;", ('', client_id))
        conn.commit()

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM cont_book WHERE id=%s;", (client_id,))
        conn.commit()

def find_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("SELECT name, surname, email, phone FROM cont_book WHERE id=%s;", (client_id,))
        print(cur.fetchall())



# create_db(conn)

# add_client(conn, 'Игорь', 'Самойлов', 'qwe@mail.ru', '222-222')

# add_phone(conn, 1, '333-333')

# change_client(conn, 1, 'Олег')

# delete_phone(conn, 1)

# delete_client(conn, 1)

# find_client(conn, 1)

conn.close()