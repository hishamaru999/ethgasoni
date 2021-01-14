# Kivy ETH Gas Station app - work in progress
# TODO: Need to fix this.  Label is not updating
import time
import datetime
from playsound import playsound
import defipulse_credentials
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from functools import partial

# Designate .kv design file
Builder.load_file('popup.kv')


# Define class
class MyLayout(Widget):
    pass

class GasApp(App):
    def build(self):
        return MyLayout()

    def run_UrlRequests(self, *args):
        trader_time = data['fastestWait']
        self.r = UrlRequest("https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}", req_body=trader_time, on_success=partial(self.up_label))

    def update_label(self, *args):
        print(self.r.result)


if __name__ == "__main__":
    GasApp().run()





## In Gwei
#fast_gwei = data['fast'] / 10
#average_gwei = data['average'] / 10
#slow_gwei = data['safeLow'] / 10
#trader_gwei = data['fastest'] / 10
#
#
# Format time
#date = datetime.datetime.today()
#now = date.today()
#format = "%m/%d/%Y %H:%M:%S"
#thetime = now.strftime(format)
#

#print(f'Time {thetime}:  Trader: {fast_gwei}')