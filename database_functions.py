import sqlite3


def create_database(database):
	'''
	---Creates a database and returns True if executed
	'''
	connection = sqlite3.connect(database)
	return True

def create_new_table(database,table_name,contents):
	'''
	---Creates a table with table name and contents of the table
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	if len(contents) == 2:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text
						)
			''')
	if len(contents) == 3:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text,
						  {contents[2]} text
						)
			''')

	if len(contents) == 4:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text,
						  {contents[2]} text,
						  {contents[3]} text
						)
			''')
	if len(contents) == 5:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text,
						  {contents[2]} text,
						  {contents[3]} text,
						  {contents[4]} text
						)
			''')

	if len(contents) == 9:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text,
						  {contents[2]} text,
						  {contents[3]} text,
						  {contents[4]} text,
						  {contents[5]} text,
						  {contents[6]} text,
						  {contents[7]} text,
						  {contents[8]} text
						)
			''')


	connection.commit()
	c.close()
	return True


def insert_single_value(database,table_name,info):
	'''
	---Inserts a single set of value 
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f"INSERT INTO {table_name} VALUES {info}")

	connection.commit()
	c.close()
	return True


def fetch_data(database,table_name):
	'''
	---Fetches all possible data from the given table name
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'SELECT username,password FROM {table_name} ')
	userinfo = c.fetchall()
	connection.commit()
	c.close()
	return userinfo

def fetch_all_data(database,table_name):
	'''
	---Fetches all possible data from the given table name
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'SELECT * FROM {table_name} ')
	userinfo = c.fetchall()
	connection.commit()
	c.close()
	return userinfo

def delete_all_data(database,table_name):
	'''
	---Deletes all possible data from table_name
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f"DELETE from {table_name}").rowcount

	connection.commit()
	c.close()

def insert_many_values(database,table_name,list_info):
	'''
	---Inserts more than one set of values 
	'''

	connection = sqlite3.connect(database)
	c = connection.cursor()



	c.executemany(f"INSERT INTO {table_name} VALUES (?,?,?)",list_info)
	
	connection.commit()
	c.close()
	return True

def check_if_data_exists(database,table_name,data):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'SELECT username FROM {table_name} where username ="{data}" ')
	
	data  = c.fetchall()
	connection.commit()
	c.close()
	print(data)
	if len(data)==0:
		return True
	return False

def delete_user(database,username):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'''DELETE from userinfo where username = '{username}' ''')
	c.execute(f"DROP TABLE '{username}'")
	connection.commit()
	c.close()
	return True


def delete_table_data(database,table_name,service,username):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'''DELETE from '{table_name}' where service = '{service}' and username = '{username}' ''')
	connection.commit()
	c.close()
	return True


def update_data(database,table_name,insert_table,data):
	connection = sqlite3.connect(database)
	c = connection.cursor()
	line = ''

	if data[0] !=None and data[1] != None:
		line = f'''UPDATE '{table_name}' SET username = '{data[0]}', password="{data[1]}"
						 WHERE Service = '{insert_table[0]}' and username= '{insert_table[1]}' '''
	elif data[0] == None:
		line = f'''UPDATE '{table_name}' SET password="{data[1]}"
						 WHERE Service = '{insert_table[0]}' and username= '{insert_table[1]}' '''
	else :
		line = f'''UPDATE '{table_name}' SET username = '{data[0]}'
						 WHERE Service = '{insert_table[0]}' and username= '{insert_table[1]}' '''

	c.execute(line)
	connection.commit()
	c.close()

def check_if_service_exists(database,table_name,service_name,username):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'SELECT Service,username FROM {table_name} where Service ="{service_name}" and username = "{username}"')
	
	data  = c.fetchall()
	connection.commit()
	c.close()
	if data == []:
		return True
	return False
	

def create_tables(database,table_name):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	# for item in (list_info):
	# 	c.execute(f"CREATE TABLE if not exists '{item}' (doctor text)  ")

	name = ('carl')

	c.execute(f"INSERT into {table_name}(doctor) VALUES(?)",(name,))

	connection.commit()

	c.close()


#insert_single_value('doctor_data.db','doctor_info',(res['name'],res["username"],res["password"],res["mobile"],res['age'],res['address'],res['city'],res['state'],res['pin_code']))

