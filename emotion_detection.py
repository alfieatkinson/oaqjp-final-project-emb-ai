import requests

def emotion_detector(text_to_analyse):
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
    
    # Return the 'text' attribute of the response object
    response_json = response.json()
    response_EP = response_json.get('emotionPredictions', [{}])[0]
    response_EM = response_EP.get('emotionMentions', [{}])[0]
    return response_EM.get('span', {}).get('text', 'No text found')