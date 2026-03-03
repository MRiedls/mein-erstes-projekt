import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

print("🚀 Willkommen beim KI-Ideen-Validator!")
print("----------------------------------------")

idee = input("Beschreibe deine Geschäftsidee: ")

print("\n⏳ KI analysiert deine Idee...\n")

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

print(message.content[0].text)
