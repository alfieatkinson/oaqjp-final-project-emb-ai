from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    # Get the text from the incoming JSON request
    data = request.get_json()
    text_to_analyse = data.get('text', '')

    # Check if text is provided
    if not text_to_analyse:
        return jsonify({"error": "No text provided"}), 400
    
    # Get the emotion detection result
    result = emotion_detector(text_to_analyse)
    
    # Format the response
    emotion_scores = result
    dominant_emotion = emotion_scores['dominant_emotion']
    
    response_message = f"For the given statement, the system response is " \
                       f"'anger': {emotion_scores['anger']}, 'disgust': {emotion_scores['disgust']}, " \
                       f"'fear': {emotion_scores['fear']}, 'joy': {emotion_scores['joy']} and " \
                       f"'sadness': {emotion_scores['sadness']}. The dominant emotion is {dominant_emotion}."
    
    return response_message

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
