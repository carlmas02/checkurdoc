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

	if len(contents) == 6:
		c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
						( {contents[0]} text,
						  {contents[1]} text,
						  {contents[2]} text,
						  {contents[3]} text,
						  {contents[4]} text,
						  {contents[5]} text
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


def get_doctor_name(database,username):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f' SELECT name FROM doctor_info where username ="{username}" ')
	userinfo = c.fetchall()

	return userinfo



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


def search_pincode(database,pincode):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f' SELECT name,address,username,mobile FROM doctor_info where pin_code ="{pincode}" ')
	userinfo = c.fetchall()
	data = []

	if len(userinfo) == 0:
		return -1

	for item in userinfo:
		temp = {"name":item[0],'Address':item[1],'username':item[2],'number':item[3]}
		data.append(temp)

	connection.commit()
	c.close()
	return data

# data = search_pincode("doctor_data.db",'400 02')
# print(data)

def add_profession(database,name,username,resp):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	if resp['surgeon'] == True:
		c.execute(f"INSERT INTO surgeon VALUES {(name,username)}")

	if resp['orthopedic'] == True:
		c.execute(f"INSERT INTO orthopedic VALUES {(name,username)}")

	if resp['mbbs'] == True:
		c.execute(f"INSERT INTO mbbs VALUES {(name,username)}")

	if resp['psychiatrist'] == True:
		c.execute(f"INSERT INTO psychiatrist VALUES {(name,username)}")	

	connection.commit()
	c.close()
	return True



def get_user_pincode(database,user_name):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f' SELECT pin_code FROM patient_info where username ="{user_name}" ')
	userinfo = c.fetchone()
	connection.commit()
	c.close()
	if len(userinfo)==0:
		return {"r":1}
	return userinfo[0]


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

def fetch_user_data(database,table_name,user_name):
	'''
	---Fetches all possible data from the given table name
	'''
	connection = sqlite3.connect(database)
	c = connection.cursor()

	c.execute(f'SELECT * FROM {table_name} where username ="{user_name}" ')
	userinfo = c.fetchone()

	data = {"name":userinfo[0],'username':userinfo[1] ,
        "age":userinfo[4],'mobile':userinfo[3],"password":userinfo[2],
        'address':userinfo[5],'city':userinfo[6],"state":userinfo[7],
        "pin_code":userinfo[8]}

	connection.commit()
	c.close()
	return data


def patient_history(database,username):
	connection = sqlite3.connect(database)
	c = connection.cursor()

	data = []

	c.execute(f'SELECT * FROM {username} ')
	userinfo = c.fetchall()

	for item in userinfo:
		temp = {"doctor":item[0],'appointment_time':item[1],'appointment_date':item[2]}
		data.append(temp)

	connection.commit()
	c.close()
	return data 



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


def create_medicine_db():
	connection = sqlite3.connect("medicine_data.db")
	c = connection.cursor()

	c.execute(f'''CREATE TABLE IF NOT EXISTS medicine 
						( name text,
						  brand text,
						  quantity text,
						  uses text
						)
			''')

	connection.commit()

	c.close()

def add_medicine(name,brand,quantity,uses):
	connection = sqlite3.connect("medicine_data.db")
	c = connection.cursor()

	c.execute(f"INSERT INTO medicine VALUES {(name,brand,quantity,uses)}")

	connection.commit()

	c.close()

def get_medicine():
	connection = sqlite3.connect("medicine_data.db")
	c = connection.cursor()

	c.execute(f"SELECT * from medicine ")

	data = c.fetchall()

	return_data = []

	for item in data:
		return_data.append({"name":item[0],"brand":item[1],"quantity":item[2],"uses":item[3] })

	return return_data



#add_medicine("Hydrochlorothiazide","Microzide","25 mg","Blood Pressure")


def confirm_appointment(username,doctor_username):
	connection = sqlite3.connect("doctor_data.db")
	c = connection.cursor()

	c.execute(f"UPDATE {doctor_username} SET appointment_status = 1 WHERE username = '{username}' ")

	connection.commit()

	c.close()
	return True

confirm_appointment("lyann","gifford")



def get_appointment_list(username):
	connection = sqlite3.connect("doctor_data.db")
	c = connection.cursor()

	c.execute(f" SELECT * from {username} ")

	data = c.fetchall()

	return_data = []

	for item in data:
		return_data.append({"patient":item[0],"username":item[1],"sickness":item[2],"appointment_time":item[3],"appointment_date":item[4],"appointment_status":item[5]})

	return return_data


def get_phone_number(username):
	connection = sqlite3.connect("patient_data.db")
	c = connection.cursor()

	c.execute(f"SELECT mobile from patient_info WHERE username = '{username}'")

	data = c.fetchone()
	
	connection.commit()
	c.close()

	return {"number":data[0]}


get_phone_number("lyann")


def add_patient_prescription(details):
	connection = sqlite3.connect("medicine_data.db")
	c = connection.cursor()

	c.execute(f'''CREATE TABLE IF NOT EXISTS prescription 
						( username text,
						  name text,
						  brand text,
						  quantity text,
						  duration text,
						  doctor text
						)
			''')

	connection.commit()

	c.execute(f"INSERT INTO prescription VALUES {details}")

	connection.commit()

	c.close()

def get_prescription(username):
	connection = sqlite3.connect("medicine_data.db")
	c = connection.cursor()

	c.execute(f" SELECT * from prescription WHERE username = '{username}' ")

	data = c.fetchall()

	return_data = []

	for item in data:
		return_data.append({"name":item[1],"brand":item[2],"quantity":item[3],"duration":item[4],"doctor":item[5]})

	return return_data

# get_prescription('carl04')



# add_patient_prescription(("carl04","a","b","c","d","maxim"))


# #res = {"name":"Ashely Mascarenhas",'username':"ashmas" ,
#         "age":"60",'mobile':'927458432',"password":'12345678',
#         'address':"204 Susheel",'city':'Mumbai',"state":"Maharashtra",
#         "pin_code":"400 103"}


#insert_single_value('patient_data.db','patient_info',(res['name'],res["username"],res["password"],res["mobile"],res['age'],res['address'],res['city'],res['state'],res['pin_code']))




