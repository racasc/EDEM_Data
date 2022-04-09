import json
import requests
import random

from swagger_client import util



def onboarding(body):  # noqa: E501
    return response(200,"OK")

def alive():  # noqa: E501
    return response(200,"OK")
   
def getcard(body):  # noqa: E501
    return response(200,"OK")

def result(body):  # noqa: E501
    return response(200,"OK")

def card():  # noqa: E501
    return response(200,"OK")

def response(code,message):
    ret={}
    ret["message"]=message
    ret["error_code"]=code
    return ret