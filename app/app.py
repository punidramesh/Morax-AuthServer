from flask import Flask, jsonify, request, render_template, abort,make_response
import requests, os
from dotenv import load_dotenv

PORT = os.getenv('PORT')
REDIRECT_URL = os.getenv('REDIRECT_URL');
STATE = os.getenv('STATE')
CLIENTID = os.getenv('CLIENTID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

app = Flask(__name__, template_folder='templates')
code = ''
flag = 0

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods = ['GET'])
def home():
	if request.method == 'GET':
		return jsonify({'message': 'Hello'})

@app.route('/auth/redirect')
def getResponse():
	code = request.args.get('code')
	if code != None:
		flag = 1
		return render_template('inprogress.html')
	else:
		abort(404)

@app.route('/api/code', methods=['GET'])
def returncode():
	print(code)
	return jsonify({'code': code})	
	
@app.route('/api/status', methods=['GET'])
def userStatus():
	return jsonify({'flag': flag})	

@app.route('/api/auth/status', methods=['POST'])
def status():
	status = request.args.get('status').json()
	if status['status'] == 'success':
		return render_template('complete.html')
	elif status['status'] == 'invalidAT':
		return render_template('error.html', message = 'Authentication failed, Invalid code received from Coinbase')
	elif status['status'] == 'invalidC':
		return render_template('error.html', message = 'Authenication failed, access token was not received from Coinbase')
