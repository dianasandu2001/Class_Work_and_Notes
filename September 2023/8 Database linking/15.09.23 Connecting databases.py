import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='people',
    user='dbuser',
    password='pass_word',
    autocommit=True
)


def get_employees_by_lastname(lastname):
    sql = "SELECT ID, lastname, firstname, salary FROM employees"
    sql += "WHERE lastname='" + lastname + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! Im {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return


def update_salary(id, new_salary):
    sql = "UPDATE employees SET salary=" + str(new_salary) + "WHERE ID=" + str(id)
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print("Salary is updated")


lastname = input("Enter your last name")
get_employees_by_lastname(lastname)
id = int(input("Enter id number: "))
new_salary = float(input("Enter new salary: "))
update_salary(id, new_salary)
