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
try:
    request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
    data = request_data.json()
except EXCEPTION as e:
    data  = "Error!"

# In Gwei
fast_gwei = data['fast'] / 10
average_gwei = data['average'] / 10
slow_gwei = data['safeLow'] / 10
trader_gwei = data['fastest'] / 10

# Current Time
date = datetime.datetime.today()

# Set the gas alert condition
colorState = None

if trader_gwei <= 100:
    colorState = "#2FB999"


# Display Gas Fees
# Format time and display api results
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
timestamped = now.strftime(format)


# Pass API data to tk
tstampLabel = Label(root, text='Timestamp: ' + str(timestamped), font=("Calibri bold", 18))
traderGasLabel = Label(root, text='Trader: ' + str(trader_gwei), font=("Calibri bold", 20), background=colorState)
fastGasLabel = Label(root, text='Fast: ' + str(fast_gwei), font=("Calibri bold", 20 ))
avgGasLabel = Label(root, text='Average: ' + str(average_gwei), font=("Calibri bold", 20))
slowGasLabel = Label(root, text='Slow: ' + str(slow_gwei), font=("Calibri bold", 20))

tstampLabel.pack()
traderGasLabel.pack()
fastGasLabel.pack()
avgGasLabel.pack()
slowGasLabel.pack()

root.mainloop()