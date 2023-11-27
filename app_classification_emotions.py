from flask import Flask
from flask import request
from flask import render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    text=[text]
    meilleurclassifieur = joblib.load(f'meilleurclassifieur.pkl')
    d={0: 'la colère', 1: 'la peur', 2: 'la joie',3:'l\'amour',4:'la tristesse',5:'la surprise'}
    emotion_dict=dict(d)
    emotion_predict=''
    emotion=meilleurclassifieur.predict(text) 
    if emotion[0] in emotion_dict.keys():
       emotion_predict=emotion_dict[emotion[0]]
    return render_template("prediction.html" , message = emotion_predict)

if __name__ == '__main__':
    app.run()
