"""effettua il rilevamento delle emozioni sul testo ricevuto da richiesta GET di app web"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#attiviamo il server Flask per l'applicazione di rilevamento delle emozioni
app=Flask("Emotion Detector")

#route per la home page dell'applicazione
@app.route("/emotionDetector")

def emot_detector():
    """effettuiamo il rilevamento delle emozioni"""
    #otteniamo il testo da analizzare dalla richiesta GET
    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    #gestione del caso in cui il testo non è valido, restituisce un messaggio di errore
    dominant_emotion=response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    #restituiamo la risposta del sistema in un formato leggibile

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")

def render_index_page():
    """renderizza la pagina index.html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
