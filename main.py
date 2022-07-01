import openai
from flask import Flask, redirect, render_template, request, url_for
import mic

app = Flask(__name__)

mic_text = ""
openai.api_key = "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"


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
    return render_template("index.html", result=result)


def recognize_sound():
    text = mic.RecognizeAudio()
    return text


if __name__ == "__main__":
    app.run(debug=True)
