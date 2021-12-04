from twilio.rest import Client


account_sid = "ACb46b5d839db74a15419ca6890b23e95f"

auth_token = "d79e6548865c5b8c4ad9c3d9fbf1c7b7"

client = Client(account_sid,auth_token)


def send_message(doctor,patient,time,date,number):
	msg = client.messages.create(

		body = f"Hello, {patient}, Your appointment with Dr.{doctor} is succesful. The date and time slot is as follow : {date} @ {time} .",
		
		from_ = "+18309884967", 
		to = "+91"+number,


		)