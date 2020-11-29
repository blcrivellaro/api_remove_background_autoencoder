import mysql.connector

# Conexao banco de dados
def database_connection():
   mydb = mysql.connector.connect(
          user='*****', 
          password='*****',
          host='localhost',
          database='ImagensApi')

   cursor = mydb.cursor()
   return mydb, cursor

# Criar tabela
def create_table(name_table):
   mydb, cursor = database_connection()
   try:
       cursor.execute("DROP TABLE {}".format(name_table))
   except:
       pass
   cursor.execute("CREATE TABLE {} (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, data DATETIME, imgb64_dirty MEDIUMTEXT, imgb64_clean MEDIUMTEXT)".format(name_table))
   mydb.close()

# Inserir dados tabela
def insert_data(name_table, data, imgb64_dirty, imgb64_clean):
   mydb, cursor = database_connection()
   insert = "INSERT INTO {} (data, imgb64_dirty, imgb64_clean) VALUES ('{}', '{}', '{}')".format(name_table, data, imgb64_dirty, imgb64_clean)
   cursor.execute(insert)
   mydb.commit()
   mydb.close()





