import sqlite3

connection = sqlite3.connect('bank.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (name TEXT,last_name TEXT, phone_number INTEGER, balance REAL);')


def register_user(name, last_name, phone_number, balance=0):
    connection = sqlite3.connect('bank.db')
    sql = connection.cursor()

    sql.execute("INSERT INTO users (name, last_name, phone_number, balance) VALUES (?,?,?,?);",
                (name, last_name, phone_number, balance))

    connection.commit()
    connection.close()

    print('Регистрация успешно прошла!')


register_user('Шахзод', 'Абдуваитов', 500784817)


def search(name, last_name, phone_number):
    connection = sqlite3.connect('bank.db')
    sql = connection.cursor()

    result = sql.execute("SELECT * FROM users WHERE name=? AND last_name=? AND phone_number=?;",
                         (name, last_name, phone_number)).fetchone()

    return result


print(search('Шахзод', 'Абдуваитов', 500784817))


def replenishment_of_balance(amount, last_name):
    conn = sqlite3.connect('bank.db')
    sql = conn.cursor()

    sql.execute('UPDATE users SET balance = balance + ? WHERE last_name = ?', (amount, last_name))
    conn.commit()
    conn.close()

    return 'Деньги успешно приняты на баланс'


print(replenishment_of_balance(200, 'Абдуваитов'))


def withdrawals_from_balance(amount, last_name):
    conn = sqlite3.connect('bank.db')
    sql = conn.cursor()

    sql.execute('UPDATE users SET balance = balance - ? WHERE last_name = ?', (amount, last_name))
    conn.commit()
    conn.close()

    return 'Деньги успешно сняты с баланса'


print(withdrawals_from_balance(100,'Абдуваитов'))

def view_your_balance(last_name):
    connection = sqlite3.connect('bank.db')
    sql = connection.cursor()

    result = sql.execute('SELECT balance FROM users WHERE last_name = ?', (last_name,))
    return result.fetchone()


print(view_your_balance('Абдуваитов'))

def deposit(amount, days):
    dep = amount * 8 * (days / 365) / 100

    return dep


last_name = input('Введите свою фамилию: ')
user_balance = view_your_balance(last_name)
print(user_balance)
amount = int(input('Сколько снимим с баланса на депозит: '))
withdrawals_from_balance(amount, last_name)
days = int(input('Введите кол-во дней: '))
print(deposit(amount, days))