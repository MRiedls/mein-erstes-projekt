from flask import Flask, render_template, request
import anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route("/", methods=["GET", "POST"])
def index():
    analyse = None
    if request.method == "POST":
        idee = request.form["idee"]
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"""Analysiere diese Geschäftsidee als erfahrener Unternehmer und Investor:

Idee: {idee}

Bitte analysiere in diesen 4 Punkten:
💡 STÄRKEN: Was ist stark an der Idee?
⚠️ RISIKEN: Was sind die grössten Risiken?
🎯 ZIELGRUPPE: Wer sind die idealen Kunden?
🚀 NÄCHSTE SCHRITTE: Wie sollte man starten?"""
                }
            ]
        )
        analyse = message.content[0].text

    return render_template("index.html", analyse=analyse)

if __name__ == "__main__":
    app.run(debug=True)