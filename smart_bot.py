import vosk
import sounddevice as sd
import queue
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pyttsx3
import Lobbob
from mozg import *


q = queue.Queue()
model = vosk.Model('vosk-model-small-ru-0.22')
device =sd.default.device

engine = pyttsx3.init()
engine.setProperty('rate',150)#скорость озвучки
engine.setProperty('voice','ru')#казали что будт руский голос и скорость

samplerate = int(sd.query_devices(device[0],'input')['default_samplerate'])

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def synthesize_text(text):
    engine.say(text)
    engine.runAndWait()

def recognize(data, vectorizer, clf):
    name = Lobbob.voice_start.intersection(data.split())
    if not name:
        return

    data.replace(list(name)[0],'')
    text_vector = vectorizer.transform([data]).toarray()[0]

    answer = clf.predict([text_vector])[0]
    funk_name = str(answer).split()[0]
    synthesize_text(str(answer).replace(funk_name,''))

    exec(funk_name + '()')

    # synthesize_text(pogoda)# проверка голоса

def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(Lobbob.dataset.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(Lobbob.dataset.values()))

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device[0], dtype='int16', channels=1,
                           callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()

