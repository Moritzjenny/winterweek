from flask import Flask

app = Flask(__name__)

@app.route('/message')
def get_message():
    print("message sent")
    return {'message': 'there are 38 places left! '}