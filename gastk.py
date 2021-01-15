#!/usr/bin/python
import requests
import json
from tkinter import *
from PIL import ImageTk, Image
import time
import datetime
import defipulse_credentials

root = Tk()
root.title('ETH Gas Station')
root.iconbitmap('f:/ethgas.ico')
root.geometry("400x400")

# Get gas data from EthGasStation
request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
data = request_data.json()

# In Gwei
fast_gwei = data['fast'] / 10
average_gwei = data['average'] / 10
slow_gwei = data['safeLow'] / 10
trader_gwei = data['fastest'] / 10

# Current Time
date = datetime.datetime.today()

# Display Gas Fees
# Format time and display api results
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
timestamped = now.strftime(format)


# Pass API data to tk
tstamp = Label(root, text=timestamped)
traderGas = Label(root, text=trader_gwei)
fastGas = Label(root, text=fast_gwei)
avgGas = Label(root, text=average_gwei)
slowGas = Label(root, text=slow_gwei)
tstamp.pack()
traderGas.pack()
fastGas.pack()
avgGas.pack()
slowGas.pack()

root.mainloop()