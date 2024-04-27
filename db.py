import sqlite3 #база данных для хранения данных на сайте (пользователей)
'''
User
- id
- login
- password
- fio
'''
con = sqlite3.connect('site.db')
cursor = con.cursor()

#SQL
cursor.execute('''
create table users(
id int autoincrement primary key,
login 
 
)
''')


a = 10 #int (числовой)
b = 'user1' #str (строковый)
c = True #bool (Булевый)
d = 10.4 #float(с плавающей точкой)
'''
Как подключить git к проекту
1. Вкладка VCS->Enable Control...->Ok->
2. Чтобы залить проект на  github, надо сделать коммит
'''
