from flask import Flask, jsonify, json, request
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        data = json.loads(request.get_json());
        tweet = data['text']
        tweet_blob = TextBlob(tweet)
        return (str(tweet_blob.sentiment.polarity))
    return("working")
