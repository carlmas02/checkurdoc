import requests

data = {"patient":"Carl","username":"test","sickness":"fever",'doctor':"Maxim"}

# resp = requests.post("https://checkurdoc.herokuapp.com/patient/test",data)

# print(resp.json())



# data = {"name":"Kevin Gomez",'username':"kev" ,
#         "age":"34",'mobile':'453743257',"password":'grgrgg',
#         'address':"Mira road, gif tower",'city':'Mumbai',"state":"Gujarat",
#         "pin_code":"400 092"}

# resp = requests.put("https://checkurdoc.herokuapp.com/signup/0",data)
# print(resp.json())


# print(resp.json())

# #data  =  {"sickness":"cold","level":"average"}


#  #  ,'','mobile','age'  'patient','username','sickness','appointment_date'


# #data = {"patient":"Carl","username":"carlmas",'sickness':"cold",'doctor':"maxim35"}




# print(resp.json())

# # database_functions.create_database('/home/testingcarl/mysite/doctor_data.db')  
# # data_name = database_functions.create_database('/home/testingcarl/mysite/patient_data.db') 


# data = {"username":"test","password":"12345678"}

# resp = requests.get("https://checkurdoc.herokuapp.com/search/test")

# print(resp.json())


# resp = requests.get("https://checkurdoc.herokuapp.com/user/1/test")

# print(resp.json())



# data = requests.get("http://127.0.0.1:2000/search/carmas")

# print(data.json())


# data = {'surgeon':1,'orthopedic':0,'mbbs':0,'psychiatrist':1}

# data = requests.get("http://127.0.0.1:2000/profession/c/test",data)

# print(data.json())


# data = {"sickness":"mbbs",'level':"medium"}

# resp = requests.get("/s/c",data)

# print(resp.json())



# data = requests.get("https://checkurdoc.herokuapp.com/searchscreen/400 12")

# print(data.json())


# data = {"name":"Kevin Gomez",'username':"kevin_wow" ,
#         "age":"34",'mobile':'453743257',"password":'grgrgg',
#         'address':"Mira road, gif tower",'city':'Mumbai',"state":"Gujarat",
#         "pin_code":"400 092"}

# data = requests.put("http://127.0.0.1:2000/signup/1",data)

# print(data.json())

data = {"patient":"Kevin","username":"kevin_wow",'sickness':"cold",'doctor':"maxim35"}

data = requests.get("http://127.0.0.1:2000/history/kevin_wow",data)


print(data.json())