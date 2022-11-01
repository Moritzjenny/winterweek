from flask import Flask
import requests
import json


app = Flask(__name__, static_folder='../build', static_url_path='/')

def get_config():
    with open('config.json', 'r', encoding='unicode_escape') as f:
        data = json.load(f)
        return data

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/message')
def get_message():

    data = get_config()

    icuMemberFile = data["mail"]["listOfIcuMemberMails"]
    fapsMemberFile = data["mail"]["listOfFapsMemberMails"]
    studentFile = data["mail"]["listOfStudentMails"]
    nonStudentFile = data["mail"]["listOfNonStudentMails"]

    for i, filename in enumerate([icuMemberFile, studentFile, nonStudentFile, fapsMemberFile]):
        with open(filename, "r") as f:
            fileData = json.load(f)
            length = len(fileData["addresses"])
            if (i == 0):
                lenIcu = length
            if (i == 1):
                lenStudents = length
            if (i == 2):
                lenNonStudents = length
            if (i == 3):
                lenFaps = length

    totalPlaces = data["registration"]["totalNumberOfFreePlaces"]

    placesLeft = totalPlaces - lenIcu - lenStudents - lenNonStudents - lenFaps 

    icu = data["pricing"]["icuMember"]
    fapsMember = data["pricing"]["fapsMember"]
    student = data["pricing"]["student"]
    nonStudent = data["pricing"]["nonStudent"]
    skiPrice = data["pricing"]["skiPrice"]

    return {'message': placesLeft, 'icuMember': icu, 'student': student, 'nonStudent': nonStudent, 'skiPrice': skiPrice, 'fapsMember': fapsMember}


