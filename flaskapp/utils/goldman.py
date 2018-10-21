import requests
import json
# ID: 4a65bc7e4a3e4e0c9c9612b9e69d6aa1
# secret: e5478525fcdeef2665b3eebe230719f55365121903e85425fdd3f400bddd7897

def get_portfolio():
    auth_url = 'https://idfs.gs.com/as/token.oauth2'
    data = {
        'grant_type': 'client_credentials',
        'client_id': '4a65bc7e4a3e4e0c9c9612b9e69d6aa1',
        'client_secret': '66b44e829b883ef272a56a1dc46b39a26ab969ff4ffb692f27485e1ad4f91d9f',
        'scope': 'read_product_data'
    }
    resp = requests.post(auth_url, data=data).json()
    access_token = resp['access_token']
    
    with requests.Session() as session:

        session.headers.update({"Authorization":"Bearer "+ access_token})

        request_url = "https://api.marquee.gs.com/v1/portfolios/data"

        request = session.get(url=request_url)
        results = json.loads(request.text)

        print(results)

def get_risk():
    pass

if __name__ == '__main__':
    get_portfolio()