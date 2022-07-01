import openai
from flask import Flask, redirect, render_template, request, url_for
import mic
import pyttsx3
import threading

app = Flask(__name__)
engine = pyttsx3.Engine()

mic_text = ""
openai.api_key = ""


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=recognize_sound(),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    engine.say(result)
    speakThread = threading.Thread(target=engine.runAndWait, args=[])
    endLoopThread = threading.Thread(target=engine.endLoop, args=[])
    speakThread.start()
    endLoopThread.start()
    return render_template("index.html", result=result)


def recognize_sound():
    text = mic.RecognizeAudio()
    return text


if __name__ == "__main__":
    app.run(debug=True)
