# Gas Now API - work in progres ...
import requests
import csv
import time
import datetime
from playsound import playsound
from colorama import Fore, Back, Style
import defipulse_credentials

# Wav file used as the alert
myalert = "f:/watame.wav"

# Timed loop to call gas now api for current eth gas prices
#while True:
    # Get Ethereum price in USD from CoinGecko
request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
price = request_price.json()['ethereum']['usd']

    # Get gas data from EthGasStation
request_data = requests.get(f'https://www.gasnow.org/api/v3/gas/price?utm_source=:GasnowOni')
gasData = request_data.json()

print(price)
print(gasData)
testdata = gasData['data']
print(testdata)

tradergas = testdata['rapid'] / 1000000000
print(tradergas)






    # In Gwei
    #trader_gwei = data['rapid'] / 10
    #fast_gwei = data['fast'] / 10
    #average_gwei = data['standard'] / 10
    #slow_gwei = data['slow'] / 10



    # Eth tx In USD
    #fast_fee = round(fast_gwei * price / 1000000 * 21, 2)
    #average_fee = round(average_gwei * price / 1000000 * 21, 2)
    #slow_fee = round(slow_gwei * price / 1000000 * 21, 2)
    #trader_fee = round(trader_gwei * price / 1000000 * 21, 2)


    # Erc20 tx In USD
    #erc20_fast_fee = round(fast_gwei * price / 1000000 * 80, 2)
    #erc20_average_fee = round(average_gwei * price / 1000000 * 80, 2)
    #erc20_slow_fee = round(slow_gwei * price / 1000000 * 80, 2)
    #erc20_trader_fee = round(trader_gwei * price / 1000000 * 80, 2)


    #date = datetime.datetime.today()


    # Display Gas Fees
    # Format time and display api results
    #now = date.today()
    #format = "%a, %b %d %H:%M:%S"
    #timestamped = now.strftime(format)

    #print(Fore.BLUE + 'Eth Gas Station:')
    #print(f'{timestamped}')
    #print(f'Trader: {trader_gwei} Fast: {fast_gwei} Standard: {average_gwei}  Slow: {slow_gwei} ')
    #print()
    #print(f'ERC20 Trader Fee: {erc20_trader_fee} Trader Fee: {trader_fee}')


    # Play alert if condtions are met
    #if average_gwei <= 40:
    #    playsound(myalert)
    #else:
    #    pass


    # 5 min updates
    #time.sleep(180)