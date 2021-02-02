"""
Modified example coming from:
Python Web Penetration Testing Cookbook.pdf
"""

import requests


def main():
    verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
    for verb in verbs:
        req = requests.request(verb, 'http://localhost/juice-shop-master/')
        print(verb, req.status_code, req.reason)
        if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
            print('Possible Cross Site Tracing vulnerability found')


if __name__ == "__main__":
    main()