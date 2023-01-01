import time
def fetch_with_retry():
    time.sleep(1)
    return requests.get('url').json()