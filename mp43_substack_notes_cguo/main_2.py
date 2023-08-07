import requests

session = requests.Session()

# Log in, using the existing session.
login_url = "https://substack.com/api/v1/login"
login_data = {
    "redirect": "",
    "for_pub": "PUBLICATION",
    "email": "MY_EMAIL",
    "password": "MY_PASSWORD",
    "captcha_response": None,
}

login_response = session.post(login_url, json=login_data)

# Assemble data for the note.
note_url = "https://substack.com/api/v1/comment/feed"
note_headers = {"Content-Type": "application/json"}
note_content = []

for line in tweet.split("\n"):
    if line:
        note_content.append(
            {"type": "paragraph",
                "content": [{"type": "text", "text": line}]}
        )
    else:
        note_content.append({"type": "paragraph"})

note_data = {
    "bodyJson": {
        "type": "doc",
        "attrs": {"schemaVersion": "v1"},
        "content": note_content,
    },
    "tabId": "for-you",
    "replyMinimumRole": "everyone",
}

note_response = session.post(note_url,
        headers=note_headers, json=note_data)