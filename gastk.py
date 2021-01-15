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
root.config(background="blue")

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
    colorState = "green"
elif trader_gwei >= 100:
    colorState = "red"
else:
    colorState = "lightblue"


# Display Gas Fees
# Format time and display api results
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
timestamped = now.strftime(format)


# Pass API data to tk
tstamp = Label(root, text='Timestamp: ' + str(timestamped), font=("Helvetica", 18), background="lightblue")
traderGas = Label(root, text='Trader: ' + str(trader_gwei), font=("Helvetica", 20), background=colorState)
fastGas = Label(root, text='Fast: ' + str(fast_gwei), font=("Helvetica", 20), background="lightblue")
avgGas = Label(root, text='Average: ' + str(average_gwei), font=("Helvetica", 20), background="lightblue")
slowGas = Label(root, text='Slow: ' + str(slow_gwei), font=("Helvetica", 20), background="lightblue")
tstamp.pack()
traderGas.pack()
fastGas.pack()
avgGas.pack()
slowGas.pack()

root.mainloop()