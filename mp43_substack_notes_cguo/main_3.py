import os
import requests

def post_note(tweet: str):
    if not tweet:
        return

    # Start a session.
    session = requests.Session()

    # Log in to Substack.
    login_url = "https://substack.com/api/v1/login"
    login_data = {
        "redirect": "",
        "for_pub": "",
        "email": os.environ.get("SUBSTACK_EMAIL"),
        "password": os.environ.get("SUBSTACK_PASSWORD"),
        "captcha_response": None,
    }
    login_response = session.post(login_url, json=login_data)

    # Bail if we were unable to log in.
    if login_response.status_code != 200:
        raise ValueError

    # Assemble data for Note.
    note_url = "https://substack.com/api/v1/comment/feed"
    note_headers = {
        "Content-Type": "application/json",
    }

    note_content = []
    for line in tweet.split("\n"):
        if line:
            note_content.append(
                {"type": "paragraph", "content": [{"type": "text", "text": line}]}
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

    # Post the Note.
    note_response = session.post(note_url, headers=note_headers, json=note_data)
    return note_response