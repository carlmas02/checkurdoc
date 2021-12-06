from twilio.rest import Client


account_sid = "ACb46b5d839db74a15419ca6890b23e95f"

auth_token = "a0ff2bc0343066663b31e2c5a624750c"

client = Client(account_sid,auth_token)


def send_message(doctor,patient,time,date,number):
	number = "+91"+number
	msg = client.messages.create(

		body = f"Hello, {patient}, Your appointment with Dr.{doctor} is succesful. The date and time slot is as follow : {date} @ {time} .",
		
		from_ = "+18309884967", 
		to = number,

		)


# data = {"username":"carl","name":"paracetoemol","brand":"Crocin","quantity":"1 Strip","duration":"Twice a day","doctor":"Mehul"}

def send_prescription(username,name,brand,quantity,doctor,number):
	number = "+91"+number
	msg = client.messages.create(

		body = f"Hello, {username}, your prescription is as follow : \n Medicine :{name}, brand :{brand}, quantity: {quantity}. \n Prescribed by Dr. {doctor}  ",
		
		from_ = "+18309884967", 
		to = number,

		)

def test():
	msg = client.messages.create(

		body = f"test msg",
		
		from_ = "+18309884967", 
		to = "+919820758390",


		)

