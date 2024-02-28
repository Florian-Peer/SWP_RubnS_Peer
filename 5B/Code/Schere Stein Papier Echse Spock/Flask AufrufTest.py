import requests


def testAufruf():
    url = 'http://127.0.0.1:5000/'
    data = {
        'name': 'new_user',
        'amount': 4
    }
    response = requests.post(url + "updateChoice", data=data)
    print(response.text)


if __name__ == "__main__":
    testAufruf()
