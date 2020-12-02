#
# MySQL 8 Shell
#

from mysqlsh import mysqlx
# SQL CREATE TABLE statement
CREATE_TBL = """
CREATE TABLE `MyDataBase`.`Caixer` (
  `ID_caixer` int auto_increment,
  `DNI_Caixer` varchar(50) NOT NULL,
  `Nom_caixer` char(50) NOT NULL,
  `Cognom_Caixer` char(50) NOT NULL,
  `Ntelf_Caixer` varchar(15) NOT NULL,
  PRIMARY KEY `id_caixer` (`ID_caixer`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

# column list, user data structure
COLUMNS = ['DNI_Caixer', 'Nom_caixer', 'Cognom_Caixer', 'Ntelf_Caixer']
user_info = {
  'host': 'localhost',
  'port': 33060,
  'user': 'root',
  'password': 'root',
}

# Get a session (connection)
my_session = mysqlx.get_session(user_info)
# Precautionary drop schema
my_session.drop_schema('MyDataBase')
# Create the database (schema)
my_db = my_session.create_schema('MyDataBase')
# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()

# Get the table object
my_tbl = my_db.get_table('Caixer')

# Insert some rows (data)
my_tbl.insert(COLUMNS).values('49951838P', 'Pablo', 'Escobar', '123456789').execute()
my_tbl.insert(COLUMNS).values('49951638U', 'Alan', 'Turing', '147258369').execute()
my_tbl.insert(COLUMNS).values('49951438T', 'Lorem', 'Ipsum', '369258147').execute()


# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()

# Display the results . Demonstrates how to work with results
# Print the column names followed by the rows
column_names = my_res.get_column_names()
column_count = my_res.get_column_count()

for i in range(0,column_count):
    if i < column_count - 1:
        print "{0}, ".format(column_names[i]),
    else:
        print "{0}".format(column_names[i]),
print
for row in my_res.fetch_all():
    for i in range(0,column_count):
        if i < column_count - 1:
            print "{0}, ".format(row[i]),
        else:
            print "{0}".format(row[i]),
    print

# Update a row
# Cambiamos el appellido del cajero con id=1 por "NuevoApellido"
my_tbl.update().set('Cognom_Caixer', 'NuevoApellido').where('ID_caixer LIKE 1').execute()
print("\nShowing results after the updating ID_caixer LIKE 1")



# Execute a simple select (SELECT ∗ FROM)
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row


my_tbl.delete().where("Nom_caixer LIKE 'Lorem'").execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after deleting rows with nombre = Lorem ")
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row
