
from flask import Flask
import datetime
import pytz # timezone 
import requests
import os

app = Flask(__name__)

@app.route('/')
def home_page():
	return "this is my homepage"



if __name__ == '__main__':
	app.run()
