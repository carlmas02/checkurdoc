from flask import Flask, request
from flask_restful import Resource, Api,reqparse
import database_functions
import timepy

app = Flask(__name__)
api = Api(app)

database_functions.create_database('doctor_data.db')
data_name = database_functions.create_database('patient_data.db')

database_functions.create_new_table("doctor_data.db",'surgeon',['name','username'])
database_functions.create_new_table("doctor_data.db",'mbbs',['name','username'])
database_functions.create_new_table("doctor_data.db",'orthopedic',['name','username'])
database_functions.create_new_table("doctor_data.db",'psychiatrist',['name','username'])

database_functions.create_new_table('doctor_data.db','doctor_info',['name','username','password','mobile','age','address','city','state','pin_code'])
database_functions.create_new_table('patient_data.db','patient_info',['name','username','password','mobile','age','address','city','state','pin_code'])

#Signup for doctor and patient
signup_put_args = reqparse.RequestParser()
signup_put_args.add_argument("name",type=str,help="Name of the user",required = True)
signup_put_args.add_argument("username",type=str,help="Username of the user",required = True)
signup_put_args.add_argument("password",type=str,help="Password of the user",required = True)
signup_put_args.add_argument("mobile",type=str,help="Mobile number of the user",required = True)
signup_put_args.add_argument("age",type=str,help="Age of the user",required = True)
signup_put_args.add_argument("address",type=str,help="Adress of the user",required = True)
signup_put_args.add_argument("city",type=str,help="Adress of the user",required = True)
signup_put_args.add_argument("state",type=str,help="Adress of the user",required = True)
signup_put_args.add_argument("pin_code",type=str,help="Adress of the user",required = True)

patient_req = reqparse.RequestParser()
patient_req.add_argument("sickness",type=str,required=True)
patient_req.add_argument("level",type=str,required=True)

appointment = reqparse.RequestParser()
appointment.add_argument("patient",type=str,help="Name of the Patient",required = True)
appointment.add_argument('username',type=str,help="Username of the Patient",required = True)
appointment.add_argument('sickness',type=str,help="sickness of the user",required = True)
appointment.add_argument('doctor',type=str,help="Username of the doctor",required = True)

login_args = reqparse.RequestParser()
login_args.add_argument("username",type=str,help="Username of the user",required=True)
login_args.add_argument("password",type=str,help="Password of the user",required=True)

prof = reqparse.RequestParser()
prof.add_argument("surgeon",type=bool,help="surgeon response",required=True)
prof.add_argument("mbbs",type=bool,help="mbbs response",required=True)
prof.add_argument("orthopedic",type=bool,help="orthopedic response",required=True)
prof.add_argument("psychiatrist",type=bool,help="psychiatrist response",required=True)


class Signup(Resource):
	def put(self,prompt):
		res = signup_put_args.parse_args()
		if prompt == "0":
			if database_functions.check_if_data_exists('doctor_data.db','doctor_info',res["username"]):
				database_functions.insert_single_value('doctor_data.db','doctor_info',(res['name'],res["username"],res["password"],res["mobile"],res['age'],res['address'],res['city'],res['state'],res['pin_code']))
				database_functions.create_new_table('doctor_data.db',res["username"],['patient','username','sickness','appointment_date'])
				return {"response":200}
			return {"response":401}
		if prompt == "1":
			if database_functions.check_if_data_exists('patient_data.db','patient_info',res["username"]):
				database_functions.insert_single_value('patient_data.db','patient_info',(res['name'],res["username"],res["password"],res["mobile"],res['age'],res['address'],res['city'],res['state'],res['pin_code']))
				#database_functions.create_new_table('patient_data.db',res["username"],['Service','username','password'])
				return {"response":200}
			return {"response":401}

class Login(Resource):
	def post(self,prompt):
		res = login_args.parse_args()
		if prompt == "0":
			data = database_functions.fetch_data('doctor_data.db','doctor_info')
			immu_dict = {}

			for i,j in data:
				immu_dict[i] = j


			for username in immu_dict:
				if username == res['username']:
					if immu_dict[username] == res['password']:
						return {"response":200}
			return {"response":401}


		if prompt == "1":
			data = database_functions.fetch_data('patient_data.db','patient_info')
			immu_dict = {}

			for i,j in data:
				immu_dict[i] = j

			for username in immu_dict:
				if username == res['username']:
					if immu_dict[username] == res['password']:
						return {"response":200}
			return {"response":401}


class Patient(Resource):
	def get(self,username):
		args = patient_req.parse_args()
		avail_doc = database_functions.fetch_all_data("doctor_data.db",args['sickness'])

		return {"available":avail_doc}

	def post(self,username):
		args = appointment.parse_args()
		database_functions.insert_single_value("doctor_data.db",args['doctor'],(args['patient'],args['username'],args['sickness'],timepy.get_time()) ) 
		return 200
		return {'time':timepy.get_time()}

class User(Resource):
	def get(self,prompt,username):
		if prompt == "0":
			data = database_functions.fetch_user_data("doctor_data.db",'doctor_info',username)
			return data

		if prompt == "1":
			data = database_functions.fetch_user_data("patient_data.db",'patient_info',username)
			return data


class Search(Resource):
	def get(self,username):
		pincode = database_functions.get_user_pincode('patient_data.db',username)

		return database_functions.search_pincode('doctor_data.db',pincode)

class Profession(Resource):
	def get(self,name,username):
		resp = prof.parse_args()

		prompt = database_functions.add_profession("doctor_data.db",name,username,resp)
		if prompt==True:
			return {"success":201}
		return {"error":401}

api.add_resource(Signup,"/signup/<string:prompt>")
api.add_resource(Patient,'/patient/<string:username>')
api.add_resource(Login,'/login/<string:prompt>')
api.add_resource(User,'/user/<string:prompt>/<string:username>')
api.add_resource(Search,'/search/<string:username>')
api.add_resource(Profession,'/profession/<string:name>/<string:username>')


if __name__ == "__main__":
	app.run(debug =True,port=2000)



'''
"https://checkurdoc/signup/0" -> SERVER

 SERVER -> DATABASE 

 {"name" : "Carl",
  "username" :"x45096";
  ....	


 }
'''


# REST APIs

#  Post -> post a username

# Put   -> update a username/password

# Get -> fetch details

# Delete  -> delete details



 

