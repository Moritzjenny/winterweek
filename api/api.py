from flask import Flask
import requests
import json


app = Flask(__name__, static_folder='../build', static_url_path='/')

def get_config():
    with open('config.json', 'r') as f:
        data = json.load(f)
        return data

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/message')
def get_message():

    data = get_config()

    documentIDMembers = data["googleApi"]["icuMemberDocumentID"]
    documentIDStudents = data["googleApi"]["studentDocumentID"]
    documentIDNonStudents = data["googleApi"]["nonStudentDocumentID"]

    APIKey = data["googleApi"]["apiKey"]
    totalPlaces = data["registration"]["totalNumberOfFreePlaces"]

    #get icu members list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDMembers + "/values/B1:B?key=" + APIKey)
    icu = len(list(filter(None, response.json()["values"]))) - 1

    #get students list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDStudents + "/values/B1:B?key=" + APIKey)
    students = len(list(filter(None, response.json()["values"]))) - 1

    #get non students list
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/"+ documentIDNonStudents + "/values/B1:B?key=" + APIKey)
    nonStudents = len(list(filter(None, response.json()["values"]))) - 1

    placesLeft = totalPlaces - nonStudents - icu - students

    icu = data["pricing"]["icuMember"]
    student = data["pricing"]["student"]
    nonStudent = data["pricing"]["nonStudent"]

    return {'message': placesLeft, 'icuMember': icu, 'student': student, 'nonStudent': nonStudent}


