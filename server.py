from flask import Flask, request
from flask_restful import Resource, Api,reqparse
import database_functions
import timepy

app = Flask(__name__)
api = Api(app)

database_functions.create_database('doctor_data.db')
data_name = database_functions.create_database('patient_data.db')
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
				#database_functions.create_new_table('password.db',res["username"],['Service','username','password'])
				return {"response":200}
			return {"response":401}

class Login(Resource):
	def get(self):
		pass

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

api.add_resource(Signup,"/signup/<string:prompt>")
api.add_resource(Patient,'/patient/<string:username>')


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



 

