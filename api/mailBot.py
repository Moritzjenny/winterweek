import json
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr




def get_config():
    with open('config.json', 'r', encoding='unicode_escape') as f:
        data = json.load(f)
        return data

def get_pw(file):
    with open(file, 'r') as f:
        pw = f.read()
        return pw


def get_lists_of_registered_users(data):
    documentIDMembers = data["googleApi"]["icuMemberDocumentID"]
    documentIDStudents = data["googleApi"]["studentDocumentID"]
    documentIDNonStudents = data["googleApi"]["nonStudentDocumentID"]

    APIKey = data["googleApi"]["apiKey"]

    # get icu members list
    response = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDMembers + "/values/B1:B?key=" + APIKey)
    icu = (response.json()["values"])[1:]

    # get students list
    response = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDStudents + "/values/B1:B?key=" + APIKey)
    students = (response.json()["values"])[1:]

    # get non students list
    response = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDNonStudents + "/values/B1:B?key=" + APIKey)
    nonStudents = (response.json()["values"])[1:]

    return [icu, students, nonStudents]

def get_user_data(data, sheetIndex, rowIndex):
    APIKey = data["googleApi"]["apiKey"]
    userData = {}
    dataList = []
    cost = 0
    if sheetIndex == 0:
        documentIDMembers = data["googleApi"]["icuMemberDocumentID"]
        # get icu members list
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDMembers +
            "/values/A"+str(rowIndex+2)+":S"+str(rowIndex+2)+"?key=" + APIKey)
        dataList = (response.json()["values"])[0]
        cost = data["pricing"]["icuMember"]

    elif sheetIndex == 1:
        documentIDStudents = data["googleApi"]["studentDocumentID"]

        # get students list
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDStudents +
            "/values/A"+str(rowIndex+2)+":S"+str(rowIndex+2)+"?key=" + APIKey)
        dataList = (response.json()["values"])[0]
        cost = data["pricing"]["student"]

    elif sheetIndex == 2:
        documentIDNonStudents = data["googleApi"]["nonStudentDocumentID"]

        # get non students list
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDNonStudents +
            "/values/A"+str(rowIndex+2)+":S"+str(rowIndex+2)+"?key=" + APIKey)
        dataList = (response.json()["values"])[0]
        cost = data["pricing"]["nonStudent"]

    userData["timestamp"] = dataList[0]
    userData["email"] = dataList[1]
    userData["phoneNumber"] = dataList[2]
    userData["fullName"] = dataList[3]
    userData["group"] = dataList[4]
    userData["food"] = dataList[5]
    userData["skiPass"] = dataList[6]
    userData["lessons"] = dataList[7]
    userData["tour"] = dataList[8]
    userData["age"] = dataList[9]
    userData["stillStudent"] = dataList[10]
    userData["else"] = dataList[11]
    userData["cost"] = cost
    return userData


def compare_registered_and_mailed_users(data, listOfRegisteredUsers):
    icuMemberFile = data["mail"]["listOfIcuMemberMails"]
    studentFile = data["mail"]["listOfStudentMails"]
    nonStudentFile = data["mail"]["listOfNonStudentMails"]

    listOfUserDataToBeSent = []

    for i, filename in enumerate([icuMemberFile, studentFile, nonStudentFile]):
        with open(filename, "r") as f:
            fileData = json.load(f)
            unwrittenAddresses = []
            for row, address in enumerate(listOfRegisteredUsers[i]):
                if address != [] and address[0] not in fileData["addresses"]:
                    unwrittenAddresses.append(address[0])
                    userDataToBeSent = get_user_data(data, i, row)
                    print(userDataToBeSent)
                    listOfUserDataToBeSent.append(userDataToBeSent)
            for unwrittenAddress in unwrittenAddresses:
                fileData["addresses"].append(unwrittenAddress)
            f.seek(0)
            with open(filename, "w") as outfile:
                json.dump(fileData, outfile)
    return listOfUserDataToBeSent

def send_mail(userData, data):
    smtp_server = data["mail"]["smtpServer"]
    port = data["mail"]["port"]
    sender_email = formataddr((data["mail"]["senderName"], data["mail"]["senderMail"]))
    receiver_email = userData["email"]
    password = get_pw(data["mail"]["senderPassword"])

    message = MIMEMultipart("alternative")
    message["Subject"] = data["mail"]["subject"]
    message["From"] = sender_email
    message["To"] = receiver_email

    timestamp = userData["timestamp"]
    email = userData["email"]
    phoneNumber = userData["phoneNumber"]
    fullName = userData["fullName"]
    group = userData["group"]
    food = userData["food"]
    skiPass = userData["skiPass"]
    lessons = userData["lessons"]
    tour = userData["tour"]
    age = userData["age"]
    stillStudent = userData["stillStudent"]
    anythingElse = userData["else"]
    cost = userData["cost"]


    html = """\
    <html>
    <head>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        th, td {
          padding: 5px;
          text-align: left;
        }
        </style>
      <body>
        <p>Hi """ + str(fullName) + """<br>
           Thanks for registering for the winter week 2023! <br>
        </p>
        <table>
  <caption style="text-align: left"><b>Your registration</b></caption>
  <tr>
    <th>Phone number</th>
    <th>Name</th>
    <th>Traveling with the Group</th>
    <th>Vegetarian Dinner</th>
    <th>Ski Pass</th>
    <th>Ski Lessons</th>
    <th>Freeriding</th>
    <th>Price</th>    
  </tr>
  <tr>
    <td>""" + str(phoneNumber) + """</td>
    <td>""" + str(fullName) + """</td>
    <td>""" + str(group) + """</td>
    <td>""" + str(food) + """</td>
    <td>""" + str(skiPass) + """</td>
    <td>""" + str(lessons) + """</td>
    <td>""" + str(tour) + """</td>
    <td>""" + str(cost) + """ CHF</td>
  </tr>
</table>
<br><br>
<p>
Please transfer the registration fee (""" +  str(cost) + """ CHF) within the next 2 weeks. The payment details are listed below<br>
If you are an ICU Member, note that the registration is only finalized after the payment of the ICU-Membership fee.<br>
If any of your information is wrong or if you have any additional questions, feel free to contact us. <br>
<b>E-mail: </b>""" + data["mail"]["contactMail"] + """<br>
<b>WhatsApp: </b>""" + data["mail"]["contactNumber"] + """<br>
</p>

<p>
Traveling with the group:<br>
Departure: """ + data["mail"]["departure"] + """ <br>
Arrival: """ + data["mail"]["arrival"] + """  <br><br>
If you can’t make the dates, contact us as early as possible.<br><br>

Freeriding:<br>
If you are interested in doing a guided ski/ freeride tour. You can get some more information and register yourself here: TODO<br>
</p>

<p>
Stay tuned for further Information<br>
Greetings<br>
Your Winter Week team =)<br>
</p>

<p>
------- Payment Details -------<br>
Kontonamen: Fachverein Informatik ICU (FV INF ICU)<br>
Zahlungszweck: Winter Week 2023, """ + email + """<br>
Kontonummer: 80-25124-4<br>
BC-Nummer: 9000<br>
BIC: POFICHBEXXX<br>
Prüfziffer: 36<br>
IBAN: CH36 0900 0000 8002 5124 4<br>
---------------------------------------<br>
</p>

      </body>
    </html>
    """
    part1 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(data["mail"]["senderMail"], password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

data = get_config()
[icu, students, nonStudents] = get_lists_of_registered_users(data)
userDataObjects = compare_registered_and_mailed_users(data, [icu, students, nonStudents])
for userDataObject in userDataObjects:
    send_mail(userDataObject, data)

