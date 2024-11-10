#! /usr/bin/python
# -*- encoding: utf-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import os
import base64
import google.generativeai as genai
import base64
from PIL import Image
import io

# Set the API key directly in the script
os.environ["API_KEY"] = "AIzaSyD1PB2ymbZxTvEuV1YpVYOwUiTirWumzrE"

# Retrieve the API key from the environment variable
api_key = os.environ["API_KEY"]

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
app.config['SECRET_KEY'] = 'ines'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client_message')

def analyse_data(data):
	prompt = f"""
	Given a piece of text, classify it as harassment or non-harassment. \n
	text: {data}"""
	#model = genai.GenerativeModel("gemini-1.5-flash")
	model = genai.GenerativeModel("gemini-1.5-flash-8b")

	response = model.generate_content(contents=prompt)

	if "Non-harassment" in response.text: 
    	#print(temp)
		emit('server_message',data,broadcast=True)
	else:
		new_data = {
            "nickname": data['nickname'],
			"message": data,
			"status": "Inapp"
		}
		emit('server_message',new_data,broadcast=False)
            
def handle_message(data):
    #emit('server_message', data, broadcast=True)
    analyse_data(data)

@socketio.on('client_image')
def handle_image(data):
    emit('server_message', data, broadcast=True)
    #image_data = data['image']
    #new_str = image_data.replace('data:image/jpeg;base64,', '')
    #image = base64.b64decode(str(new_str))

    #img = Image.open(io.BytesIO(image))

    #fileName = 'test.jpeg'
    #imagePath = ('D:\\base64toImageNewPath\\'+fileName)

    #img.save(imagePath, 'jpeg')
    
    #prompt = f"""The image contains the following text: {img}"""

    # Create the model instance
    #model = genai.GenerativeModel("gemini-1.5-flash-8b")

    # Generate content from the model
    #response = model.generate_content(contents=prompt)
    #print(response)

    # Call the function to analyze the generated response
    #analyse_data(response)

if __name__ == '__main__':
    socketio.run(app, debug=True)
