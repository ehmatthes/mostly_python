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