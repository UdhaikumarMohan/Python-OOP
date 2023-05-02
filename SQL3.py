

import pyodbc

connect_Str = "Driver={SQL Server};Server=GRENINJA\SQLEXPRESS;Database=Demo1;Trusted_Connection=yes;"

Connection = pyodbc.connect(connect_Str)

print_data = Connection.cursor()

print_data.execute("select * from employee")

print_rows = print_data.fetchall()

print(print_rows)

for i in print_rows:

    print(i.empname)

    print(f"Employee Name {i.empname}, ID {i.empid}, Age {i.empage}")