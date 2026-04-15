from flask import Flask, request
from services.whatsapp import send_answer
from services.nlp import fix_text
from faq import look_answer 

app = Flask(__name__)

VERIFY_TOKEN = "denilson123" 

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Erro de verificação", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    if "messages" in data["entry"][0]["changes"][0]["value"]:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        text_user = msg["text"]["body"]
        number_user = msg["from"]

        answer = look_answer(text_user)
        fixed_answer = fix_text(answer)

        send_answer(number_user, fixed_answer)

    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(port=5000)
