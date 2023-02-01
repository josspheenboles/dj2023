import  psycopg2
conn = psycopg2.connect(database="test",
                        host="localhost",
                        user="postgres",
                        password="qw12QW!@",
                        )
cursor = conn.cursor()

res=cursor.execute("insert into test2_trainee(name,nationalnum,course_id) values('test',121212,1)")
cursor.execute("SELECT * FROM test2_trainee WHERE id = 1")
print(cursor.fetchall())

conn.close()