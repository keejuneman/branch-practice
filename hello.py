import requests

def get_response() -> int:
    return requests.get("https://wgoogle.com/").status_code
