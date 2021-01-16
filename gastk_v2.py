#!/usr/bin/python
# ETH Gas Station via DeFi Pulse API - using Tkinter
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
import time
import requests
import datetime
import defipulse_credentials

root = Tk()
root.title('ETH Gas Station')
root.geometry("200x200")
thebackground = "white"
root.config(background=thebackground)

img = Image.open("f:/ethgas.ico")
img = ImageTk.PhotoImage(img)


traderGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
traderGasLabel.grid(row=0, sticky="N", padx=100)
fastGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
fastGasLabel.grid(row=1, sticky="N", padx=100)
averageGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
averageGasLabel.grid(row=2, sticky="N", padx=100)
slowgasLabel = Label(root, font=("Calibri bold", 20), bg="white")
slowgasLabel.grid(row=3, sticky="N", padx=100)
timeGasLabel = Label(root, font=("Calibri bold", 10), bg="white")
timeGasLabel.grid(row=4, sticky="N", padx=80)


# Get gas data from EthGasStation API
def getGas():
        request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
        data = request_data.json()
        # In Gwei
        fast_gwei = data['fast'] / 10
        average_gwei = data['average'] / 10
        slow_gwei = data['safeLow'] / 10
        trader_gwei = data['fastest'] / 10

        traderGasLabel.config(text=trader_gwei)
        fastGasLabel.config(text=fast_gwei)
        averageGasLabel.config(text=average_gwei)
        slowgasLabel.config(text=slow_gwei)

        # Timestamp
        date = datetime.datetime.today()
        now = date.today()
        format = "%a, %b %d %H:%M:%S"
        timestamped = now.strftime(format)

        timeGasLabel.config(text=timestamped)


        root.update()


# Call the function to get the API data
getGas()

root.mainloop()

#ToDo: Add refresh ability