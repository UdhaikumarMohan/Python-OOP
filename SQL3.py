

import pyodbc

Connection = Connection = pyodbc.connect("Driver={SQL Server};Server=GRENINJA\SQLEXPRESS;Database=Demo1;Trusted_Connection=yes;")

print_data = Connection.cursor()

print_data.execute("select * from employee")

print_rows = print_data.fetchall()

print(print_rows)

for i in print_rows:

    print(i.empname)