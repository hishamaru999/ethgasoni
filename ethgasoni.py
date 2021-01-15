# ETH Gas Station API - work in progres ...
import requests
import csv
import time
import datetime
from playsound import playsound
from colorama import Fore, Back, Style
import defipulse_credentials

myalert = "f:/watame.wav"

with open('fees.csv', 'w') as csvfile:  # this will overwrite the already existing file
    writer = csv.writer(csvfile)

    # Write column titles
    writer.writerow(
        ["Time", "ETH Price", "Fast Gwei", "Average Gwei", "Slow Gwei", "Fast Mins", "Average Mins", "Slow Mins",
         "Fast tx USD", "Average tx USD", "Slow tx USD", "Fast erc tx USD", "Average erc tx USD", "Slow erc tx USD"])


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


    # Eth tx In USD
    fast_fee = round(fast_gwei * price / 1000000 * 21, 2)
    average_fee = round(average_gwei * price / 1000000 * 21, 2)
    slow_fee = round(slow_gwei * price / 1000000 * 21, 2)
    trader_fee = round(trader_gwei * price / 1000000 * 21, 2)


    # Erc20 tx In USD
    erc20_fast_fee = round(fast_gwei * price / 1000000 * 80, 2)
    erc20_average_fee = round(average_gwei * price / 1000000 * 80, 2)
    erc20_slow_fee = round(slow_gwei * price / 1000000 * 80, 2)
    erc20_trader_fee = round(trader_gwei * price / 1000000 * 80, 2)


    # In Mins
    fast_time = data['fastWait']
    average_time = data['avgWait']
    slow_time = data['safeLowWait']
    trader_time = data['fastestWait']

    date = datetime.datetime.today()


    # Write to csv file
    with open('fees.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(
            [date, price, fast_gwei, average_gwei, slow_gwei, trader_gwei, fast_time, trader_time,
             average_time, slow_time, trader_fee, fast_fee, average_fee, slow_fee, erc20_trader_fee,
             erc20_fast_fee, erc20_average_fee, erc20_slow_fee])


    # Display Gas Fees
    # Format time and display api results
    now = date.today()
    format = "%a, %b %d %H:%M:%S"
    timestamped = now.strftime(format)

    print(Fore.BLUE + 'Eth Gas Station:')
    print(f'{timestamped}')
    print(f'Trader: {trader_gwei} Average: {average_gwei}  Slow: {slow_gwei} ')
    print()


    # Play alert if condtions are met
    if average_gwei <= 30:
        playsound(myalert)
    else:
        pass


    # 5 min updates
    time.sleep(180)