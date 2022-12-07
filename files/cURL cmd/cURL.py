import requests
from requests.structures import CaseInsensitiveDict

url = "https://neosalpha-999-default-rtdb.firebaseio.com/cURL.json"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "0"

resp = requests.put(url, headers=headers, data=data)

print(resp.status_code)

