"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author(Learner): [Myrlyn13]
"""

"""
This module will enable customers to access this application on the web.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    """
    This function will take a text input from a user interface and
    pass back the emotion score of that text input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detection.emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    
    anger = dominant_emotion['anger']
    disgust = dominant_emotion['disgust']
    fear = dominant_emotion['fear']
    joy = dominant_emotion['joy']
    sad = dominant_emotion['sadness']
    max_emotion = max(dominant_emotion.items(), key=lambda x: x[1])[0]
    
    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
            f"'sadness': {sad}. "
            f"The dominant emotion is {max_emotion}")

@app.route("/")
def render_index_page():
    """
    This function will render the user interface
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
