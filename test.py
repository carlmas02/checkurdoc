import requests
import database_functions
data = {"patient":"Carl","username":"test","sickness":"fever",'doctor':"Maxim"}

# resp = requests.post("https://checkurdoc.herokuapp.com/patient/test",data)

# print(resp.json())

# doc  issac -> 1234
#pat    ramesh -> 12345

data = {"name":"Parbat",'username':"parbat" ,
        "age":"5",'mobile':'453745757',"password":'222',
        'address':"Ic Colony",'city':'Mumbai',"state":"Maharashtra",
        "pin_code":"400 103"}


# resp = requests.put("http://127.0.0.1:2000/signup/1",data)

# print(resp.json())


# data = {"username":"parbat","password":"222"}

# resp = requests.post("https://checkurdoc.herokuapp.com/login/1",data)

# print(resp.json())



# resp = requests.get("http://127.0.0.1:2000/user/0/issac")

# print(resp.json())


# resp = requests.get("http://127.0.0.1:2000/searchscreen/400 103")

# print(resp.json())


# resp = requests.post("https://checkurdoc.herokuapp.com/patient/ramesh")

# print(resp.json())




# data = {"patient":"Parbat","username":"parbat",'sickness':"cough",'doctor':"mehul"}

# resp = requests.post("http://127.0.0.1:2000/patient/parbat",data)

# print(resp.json())




# resp = requests.get("https://checkurdoc.herokuapp.com/appointment/issac/issac")

# print(resp.json())


data = {'doctor':"mehul","patient":"Parbat","time":"12am","date":"23-12-2021","number":"1234"}

resp = requests.post("http://127.0.0.1:2000/appointment/parbat/mehul",data)

print(resp.json())


data = {"username":"ramesh","name":"paracetoemol","brand":"Crocin","quantity":"1 Strip",
                "duration":"Twice a day","doctor":"issac"}


# resp = requests.post("https://checkurdoc.herokuapp.com/prescreption/xyz",data)

# print(resp.json())

# resp = requests.get("https://checkurdoc.herokuapp.com/prescreption/ramesh")

# print(resp.json())




data = {"patient":"Reuben Fernandes","username":"wow","sickness":"fever",'doctor':"james"}

#resp = requests.get("http://127.0.0.1:2000/prescreption/reuben")

#print(resp.json())





# data = {"patient":"Reuben Fernandes","username":"reuben","sickness":"fever",'doctor':"Merw"}

# data = requests.post('https://checkurdoc.herokuapp.com/appointment/Merw/wow')

# print(data.json())



# data = {"username":"carl04","name":"paracetoemol","brand":"Crocin","quantity":"1 Strip","duration":"Twice a day","doctor":"Maxim"}

# print(requests.post("http://127.0.0.1:2000/prescreption",data).json())







#signup
#resp = requests.put("https://checkurdoc.herokuapp.com/signup/1",data)
#print(resp.json())


#login
data = {''}

#resp = requests.post('https://checkurdoc.herokuapp.com/login/1',data)


#patient info

# resp = requests.get("https://checkurdoc.herokuapp.com/history/carl_04")

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








# data = requests.get("https://checkurdoc.herokuapp.com/history/kevin_wow")


# print(data.json())

# ## LOGIN
# # username  -> kevin_wow
# # password  -> grgrgg

# #Book appointment 

# data = {"patient":"Kevin","username":"kevin_wow",'sickness':"cold",'doctor':"maxim35"}

# resp = requests.post("https://checkurdoc.herokuapp.com/patient/kevin_wow",data)


# #history

# data = requests.get("https://checkurdoc.herokuapp.com/history/kevin_wow")

# # print(data.json())

# # # -> [{'doctor': 'maxim35', 'appointment_date': '14:49:28'} ,......  ]



# data = requests.get("https://checkurdoc.herokuapp.com/user/0/maxim35")


# print(data.json())

# data = requests.get("https://checkurdoc.herokuapp.com/medicine")

# print(data.json())