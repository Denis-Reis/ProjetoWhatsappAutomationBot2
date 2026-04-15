import json

def look_answer(question):
    with open ("src/faq.json", "r", encoding="utf-8") as f:
        faq = json.load(f)
    return faq.get(question.lower(), "Desculpe, não entendi. Vou encaminhar para o suporte.")    