import requests
import json
# from pprint import pprint
class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def user_get_status(self, inf):
        resp = requests.get(f"{self.url}/{inf}")
        json_data = resp.json()
        return json_data

    def get_appversion(self,inf):
        json_data = self.user_get_status("info")
        appversion = json_data['appversion']
        return appversion

some_resource_client = SomeResourceClient("https://qa-xgs.xenial.com")
print(some_resource_client.get_appversion("inf"))

#res = requests.get("https://qa-xgs.xenial.com/info")

#data = res.json()
#pprint(data)