import sqlite3
conn = sqlite3.connect('mydatabase.db')
sql = conn.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER,name TEXT,age INTEGER,grade TEXT);')
sql.execute('INSERT INTO students (id,name,age,grade) VALUES (354355,"Kolya",17,"5 4 3 3");')
sql.execute('INSERT INTO students (id,name,age,grade) VALUES (3543587,"Alya",10,"5 4 5 5 5 4");')
sql.execute('INSERT INTO students (id,name,age,grade) VALUES (35435324,"Asya",17,"2 2 4 3 3");')
sql.execute('INSERT INTO students (id,name,age,grade) VALUES (354354245,"Kostya",18,"5 4 5 3");')
conn.commit()
while True:

 action = input("Выберите действие: ")
 if action == "просмотр":
   name1 = input('Введите имя ученика: ')
   def get_student_by_name(a):
      sql.execute('SELECT*FROM students WHERE name=?',(name1,))
      result = sql.fetchall()
      conn.commit()
      print(result)
   get_student_by_name(name1)
 elif action == "обновление":
     grade1 = int(input("Введите оценку: "))
     name1 = input('Введите имя ученика: ')
     def update_student_grade(b):
         sql.execute('UPDATE students SET grade=? WHERE name=?;', (grade1, name1))
         conn.commit()

         print("Оценка успешно обновлена!")
     update_student_grade(name1)

 elif action =="удаление" :
   name1 = input('Введите имя ученика: ')
   def delete_student(c):
       sql.execute('DELETE FROM students WHERE name=?',(name1,) )
       conn.commit()
       print('Операция успешно выполнена!')
   delete_student(name1)

