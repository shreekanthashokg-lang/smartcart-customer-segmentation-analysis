
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="111Asg323240",
    database="student_db"
)

cursor = conn.cursor()

tb = """
CREATE TABLE student(
    usn INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    ph INT(100),
    email VARCHAR(50),
    marks FLOAT
)
"""

cursor.execute(tb)
print("Table created successfully")
cursor = conn.cursor()

name = input("Enter name: ")
ph = int(input("Enter phone: "))
email = input("Enter email: ")
marks = float(input("Enter marks: "))

query = "INSERT INTO student(name, ph, email, marks) VALUES (%s,%s,%s,%s)"
cursor.execute(query, (name, ph, email, marks))
conn.commit()

print("Data inserted successfully")
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
cursor = conn.cursor()

usn = int(input("Enter the USN: "))
ch = input("Enter the field to be modified (ph/email): ")

if ch == "ph":
    ph = int(input("Enter the phone: "))
    cursor.execute(
        "UPDATE student SET ph=%s WHERE usn=%s",
        (ph, usn)
    )
    conn.commit()
    print("Updated successfully")

elif ch == "email":
    email = input("Enter the email: ")
    cursor.execute(
        "UPDATE student SET email=%s WHERE usn=%s",
        (email, usn)
    )
    conn.commit()
    print("Updated successfully")
    cursor = conn.cursor()

usn = int(input("Enter USN: "))
val = (usn,)

delete = "DELETE FROM student WHERE usn=%s"
cursor.execute(delete, val)
conn.commit()

print("Record deleted successfully")
cursor.close()
conn.close()