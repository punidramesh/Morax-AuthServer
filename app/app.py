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
		return render_template('inprogress.html', code = code)
	else:
		abort(404)