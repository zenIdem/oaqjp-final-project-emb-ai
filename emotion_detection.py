import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    d = json.loads(response.text)
    o=d['emotionPredictions'][0]['emotion']
    emozioni_rate = dict(zip(o.values(), o.keys()))
    emozione_forte=max(emozioni_rate.keys())
    tipoemozione_forte = emozioni_rate[emozione_forte]
    return tipoemozione_forte