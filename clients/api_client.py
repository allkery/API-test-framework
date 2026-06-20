import requests
from dotenv import dotenv_values


class APIClient:
    def __init__(self, base_url=dotenv_values(".env").get("BASE_URL")):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        response = self.session.get(f"{self.base_url}{endpoint}", **kwargs)
        return response
    
    def post(self, endpoint, json=None, **kwargs):
        response = self.session.post(f"{self.base_url}{endpoint}", json=json, **kwargs)
        return response
    
    def put(self, endpoint, json=None, **kwargs):
        response = self.session.put(f"{self.base_url}{endpoint}", json=json, **kwargs)
        return response
    
    def delete(self, endpoint, **kwargs):
        response = self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
        return response
    

    def patch(self, endpoint, json=None, **kwargs):
        response = self.session.patch(f"{self.base_url}{endpoint}", json=json, **kwargs)
        return response
