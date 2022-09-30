from flask import Flask
import requests

app = Flask(__name__)

documentIDMembers = "1Iq5uOSfdK6H2x6PCnvfLi9rNkBfzmbQotGFPN9KG7JE"
documentIDStudents = "1qnbm8QdaaZ52hRLmHPOVet_NRBxKRDG7AhNAb1BtSA0"
documentIDNonStudents = "1exnDn0rhZw6kQCeQOADmOzvRggZI2C3NN-TpLk-fH2k"

APIKey = "AIzaSyDZNVwfM0pzyPKzJArhwnOKafk3Cr7jpHc"
totalPlaces = 69

@app.route('/message')
def get_message():

    #get icu members list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDMembers + "/values/B1:B?key=" + APIKey)
    icu = len(list(filter(None,response.json()["values"]))) - 1

    #get students list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDStudents + "/values/B1:B?key=" + APIKey)
    students = len(list(filter(None,response.json()["values"]))) - 1

    #get non students list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDNonStudents + "/values/B1:B?key=" + APIKey)
    nonStudents = len(list(filter(None,response.json()["values"]))) - 1

    placesLeft = totalPlaces - nonStudents - icu - students

    return {'message': placesLeft}