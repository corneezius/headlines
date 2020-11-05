from flask import Flask, render_template, send_from_directory,redirect,url_for,request
import requests
import os
from flask_restful import Resource, Api,reqparse
from flask_cors import CORS
from multiprocessing import Process
import traceback
import runpy
server = Flask(__name__)
api = Api(server)
CORS(server)


class Run(Resource):
	def get(self):
		try:
			print ("running")
			directory = os.path.join(os.getcwd(),'script.py')
			runpy.run_path(directory,run_name='__main__')
			return 'Success'
		except Exception as err:
			error_message = traceback.format_exc()
			print (error_message)
			return error_message

api.add_resource(Run, '/run') 


@server.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
	server.run(host='0.0.0.0', debug=True, threaded=True)
