"""emotion_detection.py

This module contains the emotion detection function that uses the Watson NLP API to detect the emotion of a given text.
"""

import requests
import json

def emotion_detector(text_to_analyse):
    """Function to detect the emotion of a given text using the Watson NLP API

    Args:
        text_to_analyse (str): The text to analyse for emotion detection

    Returns:
        dict[str, float | str]: A dictionary containing the emotion scores and the dominant emotion
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Send POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check if the status code is 400, indicating a bad request
    if response.status_code == 400:
        # Return a dictionary with None values for all emotions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the JSON response if the status code is not 400
    response_json = response.json()
    response_EP = response_json.get('emotionPredictions', [{}])[0]
    
    # Extract emotion scores from the response
    emotions = response_EP.get('emotion', {})
    
    # Get the required emotions and their scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion (highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
