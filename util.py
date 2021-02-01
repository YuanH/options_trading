#!/usr/local/bin/python3
import yfinance as yf
import pandas as pd
import argparse
from pandas.tseries.offsets import *
from datetime import date


def businessDayDiff(strikeDate):
    today = date.today()
    today = today.strftime('%Y-%m-%d')
    
    return len(pd.bdate_range(today, strikeDate))

def calculate_return(options_table,bid,strikeDate):
    options_table['priceNow'] = bid
    options_table['dailyReturn'] = options_table['bid']/options_table[['strike','priceNow']].min(axis=1)/businessDayDiff(strikeDate)
    options_table['annualizedReturn'] = options_table['dailyReturn']*251
    options_table['strikeDistance'] = options_table['strike']/options_table['priceNow']-1
    return options_table    


def getOptionsTable(ticker,strike_date,TYPE=None):
    data = yf.Ticker(ticker)
    bidprice = data.info['bid']
    
    if TYPE == "put":
        print("######## PUT TABLE ###########")
        return calculate_return(data.option_chain(strike_date).puts,bidprice,strike_date)
    elif TYPE == "call":
        print("######## CALL TABLE ###########")
        return calculate_return(data.option_chain(strike_date).calls,bidprice,strike_date)
    else:
        return data.option_chain(strike_date)
        """
        print("######## PUT TABLE ###########")
        print(data.option_chain(strike_date).puts)
        print("######## CALL TABLE ###########")
        print(data.option_chain(strike_date).calls)
        """
    # return options_table_put


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--ticker", help="ticker")
    parser.add_argument("-s", "--strikedate", help = "strike date (YYYY-MM-DD)")
    parser.add_argument("--type", help = "put / call / both")
    args = parser.parse_args()
    #print(args.ticker)

    getOptionsTable(args.ticker,args.strikedate,args.type)
    
