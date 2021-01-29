#!/usr/bin/python3
import yfinance as yf
import pandas as pd
import argparse

def getOptionsTable(ticker,strike_date,TYPE=None):
    data = yf.Ticker(ticker)
    options_table_put = data.option_chain(strike_date)[1]
    options_table_call = data.option_chain(strike_date)[0]
    
    if TYPE == "put":
        print("######## PUT TABLE ###########")
        print(options_table_put)
    elif TYPE == "call":
        print("######## CALL TABLE ###########")
        print(options_table_call)
    else:
        print("######## PUT TABLE ###########")
        print(options_table_put)
        print("######## CALL TABLE ###########")
        print(options_table_call)
    # return options_table_put


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--ticker", help="ticker")
    parser.add_argument("-s", "--strikedate", help = "strike date (YYYY-MM-DD)")
    parser.add_argument("--type", help = "put / call / both")
    args = parser.parse_args()
    #print(args.ticker)

    getOptionsTable(args.ticker,args.strikedate,args.type)
    
