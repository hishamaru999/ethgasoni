#!/usr/bin/python
import requests
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
import time
import datetime
import defipulse_credentials

root = Tk()
root.title('ETH Gas Station')
root.iconbitmap('f:/ethgas.ico')
root.geometry("400x400")
thebackground = "#0237CC"
root.config(background=thebackground)

img = Image.open("f:/egs_transparent.png")
img = ImageTk.PhotoImage(img)


# Get gas data from EthGasStation
def getGas():
    request_data = requests.get(
        f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
    data = request_data.json()

    # In Gwei
    fast_gwei = data['fast'] / 10
    average_gwei = data['average'] / 10
    slow_gwei = data['safeLow'] / 10
    trader_gwei = data['fastest'] / 10

    traderGasLabel.config(text=trader_gwei)
    fastGasLabel.config(text=fast_gwei)
    avgGasLabel.config(text=average_gwei)
    slowGasLabel.config(text=slow_gwei)


# Current Time
date = datetime.datetime.today()

# Display Gas Fees
# Format time and display api results
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
timestamped = now.strftime(format)

# Pass API data to tk
# tstampLabel = Label(root, text='Time: ' + str(timestamped), font=("Calibri bold", 20), background=thebackground)
# tstampLabel.grid(row=0, sticky="N", padx=100)
# Label(root, image=img, bg="white").grid(row=1, sticky="E")

# traderGasLabel = Label(root, text='Trader: ' + str(trader_gwei), font=("Calibri bold", 20), background=thebackground)
traderGasLabel.grid(row=1, sticky="N", padx=100)
# traderGas.after(60000, )

# fastGasLabel = Label(root, text='Fast: ' + str(fast_gwei), font=("Calibri bold", 20), background=thebackground)
fastGasLabel.grid(row=2, sticky='N', padx=100)

# avgGasLabel = Label(root, text='Average: ' + str(average_gwei), font=("Calibri bold", 20), background=thebackground)
avgGasLabel.grid(row=3, sticky="N", padx=100)

# slowGasLabel = Label(root, text='Slow: ' + str(slow_gwei), font=("Calibri bold", 20), background=thebackground)
slowGasLabel.grid(row=4, sticky="N", padx=100)

root.mainloop()