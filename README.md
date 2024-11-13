# Google Clean Talk
A clean talk, harassment-free chat platform for Google hackathon.

## Mission
The main objective of our application **Google Clean Talk** is to create a safer, harassment-free, and reliable chat application by proactively identifying and flagging inappropriate content before it reaches the recipient. This application is designed to support respectful communication across professional, educational, and gaming chat platforms, aiming to protect individuals—especially women and other vulnerable users—from experiencing online bullying, harassment, and unwanted advances without prior consent. Using Google's real-time AI-driven content moderation, Google Clean Talk fosters a more inclusive and respectful digital space where all users can engage confidently and safely, whether in professional, academic, or gaming contexts.
This application "Google Clean Talk" aims to fulfill objective 5.2 of the Goal 5 targets highlighted in [UN SDG 5](https://www.un.org/sustainabledevelopment/gender-equality/).


## Architecture
Google Clean Talk is a simple bidirectional communication web-based chat application that allows users to send text messages and images. However, it comes with an additional AI-based text moderation layer to flag potentially inappropriate messages. This application mainly makes use of Google's Gemini AI model to classify text messages as harassment or not.
The basic software architecture of the application can be explained as follows:

1) **Frontend**: The user interface is created with HTML, including input fields for text messages and image uploads. Messages and images are displayed in a message box. If a message is identified to be harassing, it is displayed in the sender's message box in red with a warning. Javascript and Socket.IO are used that enable real-time communication with the server. Users can send messages and images that are immediately transmitted to the server. Javascript also listens for responses from the server to display incoming messages and images.
2) **Backend**: At the backend, we have the Flask and Socket.IO server. The Flask application hosts the webpage and serves static files using Flask's routing and template capabilities. On the other hand, the Socket.IO server manages the exchange of text messages and images between the sender and receiver. We have two functions namely client_message and client_image to listen to events (that is text messages and images).
3) **Google's Gemini AI model**: Google's Gemini model is the heart of the application. The Gemini AI model is used to classify text messages to identify whether they contain harassment or inappropriate content. When a sender sends a message, the backend code calls the pre-trained **gemini-1.5-flash-8b** model to classify the message as either "harassment" or "non-harassment". If the model detects harassment, the message is flagged, and only the sender sees it with a red warning message. For now, the application is built considering only text as input, but later it could also be extended for other inputs such as images and video. 

## Getting Started
The Google Clean Talk application can be used by following three simple steps as described below:

1) **Cloning**
```bash
$ git clone https://github.com/Raghu-dev-pixel/Google_clean_talk.git
$ cd Google_clean_talk
$ pip install -r requirements.txt
```

2) **Running**
```bash
$ python main.py
```

3) **Execution**
* If the execution of the script is successful, the Flask application will start in development mode and it is now possible to open the chat application through the web browser by clicking on the address "http://127.0.0.1:5000" as shown below.

* Two chat applications as shown below can be opened. To resemble male and female users respectively.


* Appropriate Conversations: We can now exchange text messages like any other chat application. And as long as the conversations are appropriate the messages exchanged will be delivered to both the sender and receiver.

* Inappropriate Conversations: If the messages are inappropriate or harassing in nature, the message will be flagged and will not be delivered to the reader and the sender will receive a warning message as shown below.

  
    

