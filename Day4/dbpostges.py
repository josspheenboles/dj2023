#install
#define package & install -->venv
#usign
from psycopg2 import *
#connect to db
connection=connect(database='test',
                   host='localhost',
                   user='postgres',
                   password='qw12QW!@',)
query='select * from test2_trainee'
#create cusrsor
cur=connection.cursor()
cur.execute(query)
trainees=(cur.fetchmany(3))
print(trainees)
for trainee in trainees:
    print('id:',trainee[0])
    print('name:',trainee[1])
    
#close connection
connection.close()
