import requests
import random
from flask import Flask, request, jsonify
import time
# for the api
import json
from io import StringIO
import sys
import logging
#############################################
# FLASK STUFF
#############################################

app = Flask(__name__)

headers = {
    # Your headers go here
}

def get_random_proxy():
    proxy = "socks5://3L0hfAKZOOH:L5sjDMggT@par.socks.ipvanish.com:1080"
    print(f"CURRENT PROXY - - {proxy}")
    return proxy

def check_email(email, url, max_attempts=5, retry_delay=60, request_delay_range=(1, 3)):
    attempts = 0
    # proxies = {
    #     'http': get_random_proxy(),
    #     'https': get_random_proxy(),
    # }
    proxies = dict(http=get_random_proxy(),https=get_random_proxy())

    while attempts < max_attempts:
        try:
            data = {
                'email': email,
                'date': 'Apr 18, 2023 13:25 PM',
                'url': 'https://informcareschedule.freshdesk.com/',
            }
            response = requests.post(f"{url}", headers=headers, data=data, proxies=proxies)
            status = response.status_code
            if status == 200:
                return email, status, response.text
            else:
                print(f"Request failed with status code {status}. Retrying...")
                proxies = {
                    'http': get_random_proxy(),
                    'https': get_random_proxy(),
                }
                attempts += 1
                time.sleep(retry_delay)
        except requests.RequestException as e:
            print(f"Request failed with error: {e}. Retrying...")
            proxies = {
                'http': get_random_proxy(),
                'https': get_random_proxy(),
            }
            time.sleep(retry_delay)

        delay = random.uniform(*request_delay_range)
        time.sleep(delay)
    return email, None, None

@app.route('/check_email')
def api_check_email():
    email = request.args.get('email')
    url = "http://nykanolfoqmpds.com/send_batch.php"
    
    email, status, response_text = check_email(email, url)
    
    return jsonify({
        'email': email,
        'status': status,
        'response': response_text
    })
  debug_output.close()
