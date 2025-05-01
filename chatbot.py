from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Allows frontend to send requests to Flask
analyzer = SentimentIntensityAnalyzer()

@app.route("/analyze", methods=["POST"])
def analyze_message():
    data = request.json
    message = data.get("text", "")

    sentiment_score = analyzer.polarity_scores(message)

    # AI-generated responses based on sentiment
    if sentiment_score["compound"] > 0.75:
        response = "You're in a fantastic mood! 🎉 Keep spreading positivity!"
    elif sentiment_score["compound"] > 0.05:
        response = "You seem positive! 😊 That’s great to hear."
    elif sentiment_score["compound"] < -0.75:
        response = "It sounds like you’re feeling really low. 💙 I’m here for you."
    elif sentiment_score["compound"] < -0.05:
        response = "I sense some negativity—talk to me, I'm here to support!"
    else:
        response = "Neutral tone detected. Let’s chat!"

    return jsonify({"response": response})  # Sending response back to chatbot UI

if __name__ == "__main__":
    app.run(debug=True)
