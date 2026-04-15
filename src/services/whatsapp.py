import requests

ACCESS_TOKEN = "EAASBMDfVVRYBRDaFCZBXKHRR63dCtC5tooVtsbwGyzdnHnLXUySxoZCzfI2m4tBGsh345dSKp9Rws9WncV4MEeK1PlqQ9ZCBdp9MXdntzZB1xxvj1XQsNXZCZAFvX6lnDaybSfV5SYMDtyk07QH3y7bL3OpZCBQePG5FfNHegcLo7ZCFPFqPZCpm5s4aMeo0WXEMDuZARfwtdxWsPhriZC8HgWi6osaQUAQO5KV21bzZCt11M1n2QZByBoI0ulEzWrA8hNQY9RdBXleYsifp6gX6YhOMhHisX"
PHONE_NUMBER_ID = "1012538745285014"

def send_answer(to, menssage):
    url = "https://graph.facebook.com/v17.0/1012538745285014/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body":menssage}

    }
    response = requests.post(url, headers=headers, json=payload)
    print("Status:", response.status_code)
    print("Resposta enviada:", response.text)
