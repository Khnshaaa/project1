import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    database="study",
    user="postgres",
    password="12345678"
)
cur = conn.cursor()

create_table_ = """
CREATE TABLE IF NOT EXISTS students(
    user_id SERIAL PRIMARY KEY , 
    user_name VARCHAR(50)  NOT NULL ,
    GRADE INT DEFAULT  0 
);
"""

cur.execute(create_table_)
conn.commit()

def insert_to_table(user_name  , grade):
    insert = """
    INSERT INTO students(user_name , grade)
    VALUES (%s , %s) RETURNING user_id , user_name , grade ;
    """
    cur.execute(insert, (user_name , grade))
    conn.commit()
    user_data = cur.fetchone()
    return  user_data[0]
    
if __name__== '__main__':
    name = input ()
    grade = int(input())
    user_id = insert_to_table(name , grade)
    print(user_id)

cur.close()
conn.close()

print("goood")

