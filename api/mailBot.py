import json
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr



def get_config():
    with open('config.json', 'r') as f:
        data = json.load(f)
        return data


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
        cost = "500"

    elif sheetIndex == 1:
        documentIDStudents = data["googleApi"]["studentDocumentID"]

        # get students list
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDStudents +
            "/values/A"+str(rowIndex+2)+":S"+str(rowIndex+2)+"?key=" + APIKey)
        dataList = (response.json()["values"])[0]
        cost = "650"

    elif sheetIndex == 2:
        documentIDNonStudents = data["googleApi"]["nonStudentDocumentID"]

        # get non students list
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/" + documentIDNonStudents +
            "/values/A"+str(rowIndex+2)+":S"+str(rowIndex+2)+"?key=" + APIKey)
        dataList = (response.json()["values"])[0]
        cost = "750"

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
    password = data["mail"]["senderPassword"]

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


    # Create the plain-text and HTML version of your message
    text = """
    Hi """ +fullName+ """
    Thanks for registering for the winter week 2023!
    
    Your Registration:
    Phone number: """ + phoneNumber + """
    Name: """ + fullName + """
    Traveling with the Group: """ + group + """
    Vegetarian Dinner: """ + food + """
    Ski Pass: """ + skiPass + """
    Ski Lessons: """ + lessons + """
    Freeriding: """ + tour + """
    Price: """ + cost + """CHF
    
    Please transfer the registration fee within the next 2 weeks. The payment details are listed below
    If you are an ICU Member, note that the registration is only finalized after the payment of the ICU-Membership fee.
    If any of your information is wrong or if you have any additional questions, feel free to contact us. 
    E-mail: """ + data["mail"]["senderMail"] + """
    WhatsApp: https://wa.me/41789807673
    
    Stay tuned for further Information
    Greetings
    Your Winter Week team =)
    
    Traveling with the group:
    Departure: 27.1.2023, 08:00, Zürich HB
    Arrival: 4.2.2023, 18:00, Zürich HB
    If you can’t make the dates, contact us as early as possible.
    
    Freeriding:
    If you are interested in doing a guided ski/ freeride tour. You can get some more information and register yourself here: TODO
    
    ------- Payment Details -------
    Kontonamen: Fachverein Informatik ICU (FV INF ICU)
    Zahlungszweck: Winter Week 2023, """ + email + """
    Kontonummer: 80-25124-4
    BC-Nummer: 9000
    BIC: POFICHBEXXX
    Prüfziffer: 36
    IBAN: CH36 0900 0000 8002 5124 4
    ---------------------------------------
    
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

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



