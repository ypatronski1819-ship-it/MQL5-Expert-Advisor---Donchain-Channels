#  py version 3.11.9
# numpy==1.23.5

#+------------------------------------------------------------------+
# //| #Using MetaTrader 5 (python library), we start by initializing the    |
# //| platform.                                                             |
#+------------------------------------------------------------------+

import pandas as pd
import numpy as np
import MetaTrader5 as mt5
from datetime import datetime

if not mt5.initialize(): # Initialize the MetaTrader 5 platform
    print("initialize() failed")
    mt5.shutdown()

#+------------------------------------------------------------------+
# //| #After MetaTrader 5 platform initialization, we can obtain trading    |
# //| information from it using the copy_rates_from_pos method.             |
#+------------------------------------------------------------------+

def getData(start = 1, bars = 1000):
    rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_H1, start, bars)
    if rates is None or len(rates) < bars: # if the received information is less than specified
        print("Failed to copy rates MetaTrader 5, error = ", mt5.last_error())
        return None
    
 # Create a pandas dataframe out of the obtained data
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df

#+------------------------------------------------------------------+
# Run the function                                                   |
#+------------------------------------------------------------------+
if __name__ == "__main__":
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000) #prevents line from wrapping

        df = getData()
        
        if df is not None:
             print(df.head())

             # Print column name explicitly
             print("\nColumns:", df.columns.tolist())

             # Print last 5 bars
             print("\nLast 5 bars:\n", df.tail())


             print("\nLast bar time:", df["time"].iloc[-1])
             print("Total bar:", len(df))
