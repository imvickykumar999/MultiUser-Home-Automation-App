
# pip install -r requirements.txt

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='My Name is Vicks.')

TestApp().run()


# create button to call below function for 0 and 1


# import requests
# from requests.structures import CaseInsensitiveDict

# url = "https://home-automation-336c0-default-rtdb.firebaseio.com/A/B/C/Switch.json"

# headers = CaseInsensitiveDict()
# headers["Content-Type"] = "application/x-www-form-urlencoded"

# data = "0"


# resp = requests.put(url, headers=headers, data=data)

# print(resp.status_code)

