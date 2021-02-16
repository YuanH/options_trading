#!/usr/local/bin/python3
from util import *
import requests
import pandas as pd
import datetime
import subprocess
import gspread
import numpy as np




tickers = {'DAL':'put','MSFT':'put','AAPL':'both','NVDA':'put','FB':"put",'ADBE':"put",
            'AMD':"put",'MA':"put",'NIO':"put",'MCD':"put",'TSM':"put",'TSLA':"put",'SQ':"put",
            'ROKU':"put",'PLTR':"put",'PYPL':"put",'ABNB':'put','APT':"put"}
strikedate = "2021-02-19"
TYPE = "put"


# Creating Google Spreadsheet if it doesn't already exist
gc = gspread.service_account(filename='./credentials.json')
try:
    sh = gc.open('options_trading_'+strikedate)
except:
    sh = gc.create('options_trading_'+strikedate)
    sh.share('yuan.huang10@gmail.com', perm_type='user', role='writer')
    sh.share('minshichen@gmail.com', perm_type='user', role='writer')
    sh.share('yixianwen@gmail.com', perm_type='user', role='writer')



for ticker in tickers:
    if tickers[ticker] == "both":
        data = getOptionsTable(ticker, strikedate, 'put')
        sheetname = ticker+'_'+TYPE
        upload_to_gspreadsheet(data, sheetname, sh)

        data = getOptionsTable(ticker, strikedate, 'call')
        sheetname = ticker+'_'+TYPE
        upload_to_gspreadsheet(data, sheetname, sh)
    else:
        try:
            TYPE = tickers[ticker]
            data = getOptionsTable(ticker, strikedate, TYPE)
            sheetname = ticker+'_'+TYPE
            upload_to_gspreadsheet(data, sheetname, sh)
        except:
            continue
    #

    



#sh.del_worksheet("Sheet1")


"""
with pd.ExcelWriter(filename) as writer:
    for ticker in tickers:
        print(ticker)
        data = getOptionsTable(ticker, strikedate, TYPE)

        sheetname = ticker+'_'+TYPE

        #upload_to_gspreadsheet(data, sheetname, strikedate)

        print(sheetname)
        data.to_excel(writer,sheet_name=sheetname)
"""
