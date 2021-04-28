from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import requests, os

PORT = os.getenv('PORT')
REDIRECT_URL = os.getenv('REDIRECT_URL');
STATE = os.getenv()
CLIENTID = os.getenv('CLIENTID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

app = Flask(__name__)
api = Api(app)
access_token = ''

@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        return jsonify({'message': 'Hello'})

@app.route('/auth/redirect')
def getResponse():
	code = request.args.get("code")
	if code != None:
		ACCESS_URI = f"https://www.coinbase.com/oauth/token?grant_type=authorization_code&code={code}&client_id={clientID}&client_secret={secret}&redirect_uri={REDIRECT_URL}"
		at = requests.post(ACCESS_URI).json()
		access_token = at['access_token']
		return render_template('index.html')
	else:
			return "Invalid token"

class Token(Resource):
    def get(self):
        return jsonify({'token': access_token})

api.add_resource(Token, 'auth/token')

