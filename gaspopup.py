import requests
import time
import datetime
from playsound import playsound
import defipulse_credentials
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate .kv design file
Builder.load_file('popup.kv')


# Define class
class MyLayout(Widget):
    pass

class GasApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    GasApp().run()


# Get ETH Gas Station data from defipulse API
while (True):
    # Get Ethereum price in USD from CoinGecko
    request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    price = request_price.json()['ethereum']['usd']

    # Get gas data from EthGasStation
    request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
    data = request_data.json()


    # In Gwei
    fast_gwei = data['fast'] / 10
    average_gwei = data['average'] / 10
    slow_gwei = data['safeLow'] / 10
    trader_gwei = data['fastest'] / 10


# Format time
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
thetime = now.strftime(format)


print(f'Time {thetime}:  Trader: {fast_gwei}')