import pandas as pd
import pyodbc

Connection = pyodbc.connect("Driver={SQL Server};Server=GRENINJA\SQLEXPRESS;Database=Demo1;Trusted_Connection=yes;")

print_data = Connection.cursor()

print_data.execute("select * from employee")

for i in print_data:
    print(i)

print_data.commit()

x = pd.read_sql("select * from employee", Connection)
print(x)