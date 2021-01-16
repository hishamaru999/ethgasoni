#!/usr/bin/python
# ETH Gas Station via DeFi Pulse API - using Tkinter
import requests
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
import time
import datetime
import defipulse_credentials

root = Tk()
root.title('ETH Gas Station')
root.geometry("400x400")
thebackground = "#0237CC"
root.config(background=thebackground)

img = Image.open("f:/egs_transparent.png")
img = ImageTk.PhotoImage(img)


traderGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
traderGasLabel.grid(row=0, sticky="N", padx=100)
fastGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
fastGasLabel.grid(row=1, sticky="N", padx=100)
averageGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
averageGasLabel.grid(row=2, sticky="N", padx=100)
slowgasLabel = Label(root, font=("Calibri bold", 20), bg="white")
slowgasLabel.grid(row=3, sticky="N", padx=100)

# TODO:  Create function to pull API data so it can be called from a while loop

# Get gas data from EthGasStation
request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
data = request_data.json()


# In Gwei
fast_gwei = data['fast'] / 10
average_gwei = data['average'] / 10
slow_gwei = data['safeLow'] / 10
trader_gwei = data['fastest'] / 10


date = datetime.datetime.today()
now = date.today()
format = "%m/%d/%Y %H:%M:%S"
timestamped = now.strftime(format)


#tstampLabel.config(text=timestamped)
traderGasLabel.config(text="Trader:" + str(trader_gwei))

#fastGasLabel.config(text=fast_gwei)
fastGasLabel.config(text="Fast:" + str(fast_gwei))

#avgGasLabel.config(text=average_gwei)
averageGasLabel.config(text="Average: " + str(average_gwei))

#slowGasLabel.config(text=slow_gwei)
slowgasLabel.config(text="Slow: " + str(slow_gwei))


root.mainloop()