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
root.geometry("400x400")
thebackground = "#0237CC"
root.config(background=thebackground)

img = Image.open("f:/egs_transparent.png")
img = ImageTk.PhotoImage(img)

traderGasLabel = Label(root, font=("Calibri bold", 20), bg="white")
traderGasLabel.grid(row=0, sticky="N", padx=100)


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
#avgGasLabel.config(text=average_gwei)
#slowGasLabel.config(text=slow_gwei)


# Pass API data to tk
#tstampLabel.grid(row=0, sticky="N", padx=100)
#Label(root, image=img, bg="white").grid(row=1, sticky="E")

traderGasLabel.grid(row=1, sticky="N", padx=100)
# traderGas.after(60000, )

#fastGasLabel.grid(row=2, sticky='N', padx=100)

#avgGasLabel.grid(row=3, sticky="N", padx=100)

#slowGasLabel.grid(row=4, sticky="N", padx=100)

root.mainloop()