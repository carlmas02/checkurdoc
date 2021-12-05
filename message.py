from twilio.rest import Client


account_sid = "ACb46b5d839db74a15419ca6890b23e95f"

auth_token = "bcf6fbf31d463aed1a392271dc31b914"

client = Client(account_sid,auth_token)


def send_message(doctor,patient,time,date,number):
	number = "+91"+number
	msg = client.messages.create(

		body = f"Hello, {patient}, Your appointment with Dr.{doctor} is succesful. The date and time slot is as follow : {date} @ {time} .",
		
		from_ = "+18309884967", 
		to = number,

		)

data = {'doctor':"mehul","patient":"Parbat","time":"12am","date":"23-12-2021","number":"9820758390"}

# send_message("xyz","rum",data["time"],data["date"],data["number"])



def test():
	msg = client.messages.create(

		body = f"test msg",
		
		from_ = "+18309884967", 
		to = "+919820758390",


		)

