import requests

data = {"name":"Wow",'username':"maxim45" ,
        "age":"60",'mobile':'927458432',"password":'12345678',
        'address':"204 Susheel",'city':'Mumbai',"state":"Maharashtra",
        "pin_code":"400 103"}

#data  =  {"sickness":"cold","level":"average"}


 #  ,'','mobile','age'  'patient','username','sickness','appointment_date'


#data = {"patient":"Carl","username":"carlmas",'sickness':"cold",'doctor':"maxim35"}


resp = requests.put("http://testingcarl.pythonanywhere.com/signup/0",data)

print(resp.json())

# database_functions.create_database('/home/testingcarl/mysite/doctor_data.db')  
# data_name = database_functions.create_database('/home/testingcarl/mysite/patient_data.db') 

