import json
import requests
import random

from swagger_server import util
users={}
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
values={}
active_users=0
lost_users=0

def newgame():
    global values
    global active_users
    random.shuffle(deck)
    values.clear()
    active_users=len(users)
    for user in users:
        status={}
        status["user"]=user
        status["value"]=0
        status["playing"]=1
        values[user]=status
        
    return response(200,"Game Started")


#{
#  "image": "string",
#  "ip": "string",
#  "name": "adios"
#}

def onboarding(body):  # noqa: E501
    if len(body) > 0:
        ip = body["ip"]
        name= body["name"]
        image= body["image"]
        try:
            ret=requests.get("http://"+ip+"/swagger-ui/alive")
            if ret.status_code != 200:
                return response(400,f"Host not available please check ip and port {ip}")
        except Exception as e:
            return response(400,f"Exception {e}: Host not available please check ip and port {ip}")

        if ret.status_code != 200:
            return response(400,f"Server not available, or ip incorrect {ip}")
        if len(name)==0:
            return response(400,"Name not specified")
        else:
            users[name]=body 
            return response(200,"User added correctly")
    else:
        raise("Error in user")

def nextcard():  # noqa: E501
    global active_users
    global values
    global lost_users
    for user in values:
        print(user)
        if values[user]["playing"] == 1:
            
            ip=users[values[user]["user"]]["ip"]
            #return response(200,ip)
            ret=requests.get("http://"+ip+"/swagger-ui/card")
            if ret.status_code == 200:
                card=deck.pop()
                data ={
                "card": card
                }
                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                ret=requests.post(url = f'http://{ip}/swagger-ui/getcard', json = data, headers=headers)
                values[user]["value"]=values[user]["value"]+card 
                if values[user]["value"]>21:
                    values[user]["playing"]=0
                    active_users=active_users-1
                    lost_users=lost_users+1 
            else:
                values[user]["playing"]=0
                active_users=active_users-1
    if active_users == 0:
        total=0
        win=True
        while win :
            total=total+deck.pop()
            if total<21:
                all_loose=
                for user in values:
                    if values[user]["playing"]


        return response(200,"GAME ENDED")
    return "END"

def getallplayers():  # noqa: E501
    return users

def getstatus(id_):  # noqa: E501
    return values[id_]
    

def response(code,message):
    ret={}
    ret["message"]=message
    ret["error_code"]=code
    return ret