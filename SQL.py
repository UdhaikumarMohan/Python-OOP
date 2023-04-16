
import sys
import pyodbc

# For local server

Connection = pyodbc.connect("Driver={SQL Server};Server=GRENINJA\SQLEXPRESS;Database=Demo1;Trusted_Connection=yes;")

# To connect with external server we need to give userID(UID=xxx), password(PWD=xxx)

cursor = Connection.cursor()

# To create table, alter, drop

# cursor.execute("Create table NewTable(Name varchar(50) constraint Newkey primary key, Age int, Designation varchar(50))")

# To insert, update, delete
cursor.execute("insert into employee values(7, 'Guna', 29)")
cursor.execute("update employee set empage = 30 where empname = 'Arun'")

# execution will be reflected in DB only if commit is given.
cursor.commit()

Connection.close()
