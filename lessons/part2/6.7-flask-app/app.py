from flask import Flask, request
from umbrella import makeUmbrellaDecision
app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    if makeUmbrellaDecision(city, 'us'):
        return 'Bring an umbrella'
    else:
        return 'No need for an umbrella'
    
@app.route("/wasabi")
def wasabi():
    return "you guessed it"

