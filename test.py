import requests
data = {"name":"Ashely Mascarenhas",'username':"test" ,
        "age":"60",'mobile':'927458432',"password":'12345678',
        'address':"204 Susheel",'city':'Mumbai',"state":"Maharashtra",
        "pin_code":"400 092"}

resp = requests.put("https://checkurdoc.herokuapp.com/signup/0",data)
print(resp.json())
# print(resp.json())

# #data  =  {"sickness":"cold","level":"average"}


#  #  ,'','mobile','age'  'patient','username','sickness','appointment_date'


# #data = {"patient":"Carl","username":"carlmas",'sickness':"cold",'doctor':"maxim35"}




# print(resp.json())

# # database_functions.create_database('/home/testingcarl/mysite/doctor_data.db')  
# # data_name = database_functions.create_database('/home/testingcarl/mysite/patient_data.db') 


# data = {"username":"parth23","password":"1234566678"}

# resp = requests.get("http://127.0.0.1:2000/login/0",data)

# print(resp.json())


# data = requests.get("http://127.0.0.1:2000/search/test")

# print(data.json())


# data = {'surgeon':1,'orthopedic':0,'mbbs':0,'psychiatrist':1}

# data = requests.get("http://127.0.0.1:2000/profession/c/test",data)

# print(data.json())


# data = {"sickness":"mbbs",'level':"medium"}

# resp = requests.get("http://127.0.0.1:2000/patient/c",data)

# print(resp.json())



