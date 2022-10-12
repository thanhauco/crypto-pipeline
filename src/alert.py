import requests
def alert(msg):
    requests.post('https://hooks.slack.com', json={'text': msg})