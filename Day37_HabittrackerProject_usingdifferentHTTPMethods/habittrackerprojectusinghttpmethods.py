#here we're going to post data to the pixela api to create a user account

import requests
from datetime import datetime

USERNAME = "rups"
TOKEN = "df23685465jef902"
GRAPH_ID = "graph1"

pixela_endpt = "https://pixe.la/v1/users"
user_params = {
"token" : TOKEN,
    "username" : USERNAME ,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url = pixela_endpt , json = user_params)
# print(response.status_code)
# print(response.text)

#2. Create a Graph
#/v1/users/<username>/graphs, pixela_endpt = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpt}/rups/graphs"
graph_params = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "kilometers",
    "type" : "float",
    "color": "ajisai",
}
headers = {
"X-USER-TOKEN" : TOKEN
}

# graph_postdata = requests.post(url = graph_endpoint,json = graph_params,headers = headers)
# print(graph_postdata.text)
# print(graph_postdata.status_code)
# #to check the created graph - https://pixe.la/v1/users/rups/graphs/graph1.html[url- https://pixe.la/v1/users/a-know/graphs/test-graph]

#STEP 3: Creating a pixel in the graph, endpt-  /v1/users/<username>/graphs/<graphID>

today = datetime.now()
modified_date = today.strftime("%Y%m%d") , #https://www.w3schools.com/python/python_datetime.asp for date modifications

value_endpoint = f"{pixela_endpt}/{USERNAME}/graphs/{GRAPH_ID}"
value_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you cycle today? "),
}
# value_postdata = requests.post(url = value_endpoint,json = value_params,headers = headers)
# print(value_postdata.text)
# print(value_postdata.status_code)
#https://pixe.la/v1/users/rups/graphs/graph1.html- check the output here

#updating the data through PUT HTTP Method, endpt- /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
#updating quantity from 15 to 10 for yesterday [first create pixel quantity for 2 days]
update_pixel = f"{pixela_endpt}/{USERNAME}/graphs/{GRAPH_ID}/20260518"
update_params = {
    "quantity" : "10",
}
# updated_graph = requests.put(url = update_pixel, json = update_params, headers = headers)
# print(updated_graph.text)
# print(updated_graph.status_code)

#deleting one pixel through DELETE HTTP Method, endpt- /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_pixel = f"{pixela_endpt}/{USERNAME}/graphs/{GRAPH_ID}/20260517"
deleted_graph = requests.delete(url = delete_pixel, headers = headers)
print(deleted_graph.text)
print(deleted_graph.status_code)

