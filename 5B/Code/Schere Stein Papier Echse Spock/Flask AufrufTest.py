import requests

def SetUpdateTest():
    url = 'http://127.0.0.1:5000/'
    data = {
        'name': 'new_user',
        'amount': 4
    }
    response = requests.post(url + "updateTotalWins", data=data)
    print(response.text)

def GetTest():
    url = 'http://127.0.0.1:5000/getTotalWins'
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    GetTest()
