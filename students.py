import sqlite3
connection = sqlite3.connect('mydatabase.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'name TEXT, age INTEGER, grade TEXT);')

sql.execute('INSERT INTO students (name, age, grade) VALUES ("Shahzod", 20, "A+" );')

sql.execute('INSERT INTO students (name, age, grade) VALUES ("Mansur", 18, "A" );')

sql.execute('INSERT INTO students (name, age, grade) VALUES ("Albert", 22, "A+" );')



connection.commit()
connection.close()

def get_student_by_name(name):
    connection = sqlite3.connect('mydatabase.db')
    sql = connection.cursor()


    result_by_name = sql.execute('SELECT * FROM students WHERE name=?;', (name,)).fetchone()
    return result_by_name
print(get_student_by_name('Shahzod'))


def update_students_grade(name, new_grade):
    connection = sqlite3.connect('mydatabase.db')
    sql = connection.cursor()

    sql.execute('UPDATE students SET grade=? WHERE name=?;', (name, new_grade))

    connection.commit()
    connection.close()
    return 'Оценка добавлена'
    print(update_students_grade('Shahzod', 'B'))

def delete_student(name):
    connection = sqlite3.connect('mydatabase.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM students WHERE name=?;', (name,))

    connection.commit()
    connection.close()
    return 'Студент удален'

print(delete_student('Mansur'))




