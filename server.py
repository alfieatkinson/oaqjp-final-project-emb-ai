"""server.py

This module is the server for the emotion detection system.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    """Function to detect emotion of given text via POST request

    Returns:
        str: The emotion detection result
    """
    # Get the text from the incoming JSON request
    data = request.get_json()
    text_to_analyse = data.get('text', '')

    # Get the emotion detection result
    result = emotion_detector(text_to_analyse)

    # If dominant emotion is None, return error message
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response
    emotion_scores = result
    dominant_emotion = emotion_scores['dominant_emotion']

    msg = f"For the given statement, the system response is " \
            f"'anger': {emotion_scores['anger']}, 'disgust': {emotion_scores['disgust']}, " \
            f"'fear': {emotion_scores['fear']}, 'joy': {emotion_scores['joy']} and " \
            f"'sadness': {emotion_scores['sadness']}. The dominant emotion is {dominant_emotion}."

    return msg

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
