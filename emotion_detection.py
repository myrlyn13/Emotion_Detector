import requests
import json

def emotion_detector(text_to_analyze):
    URL = ''https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict''
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input json: { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        return formatted_response
    elif response.status_code == 400:
        formatted_response = {
                            'anger': anger_score,
                            'disgust': disgust_score,
                            'fear': fear_score,
                            'joy': joy_score,
                            'sadness': sadness_score,
                            'dominant_emotion': '<name of the dominant emotion>' 
                            }
        return formatted_response

def emotion_predictor(detected text):
    if all(value is None for value in detected_text.values()):
        return detected_text
    if detected_text['emotionPredictions'] is not None:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)
        #max_emotion_score = emotions[max_emotion]
        formatted_dict_emotions = {
                                'anger': anger,
                                'disgust': disgust,
                                'fear': fear,
                                'joy': joy,
                                'sadness': sadness,
                                'dominant_emotion': max_emotion
                                 }
    return formatted_dict_emotions