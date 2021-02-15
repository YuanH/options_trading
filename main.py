#!/usr/local/bin/python3
from util import *
import requests
import pandas as pd
import datetime
import subprocess
import gspread
import numpy as np

def upload_to_gspreadsheet(df,sheetname,strikedate):


    gc = gspread.service_account(filename='./credentials.json')


    sh = gc.create('options_trading'+strikedate)
    sh.share('yuan.huang10@gmail.com', perm_type='user', role='writer')

    worksheet=sh.add_worksheet(sheetname,rows='100',cols='20')
    worksheet = sh.worksheet(sheetname)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())




tickers = ['DAL','MSFT','AAPL','NVDA','FB','ADBE','HD','AMD','MA','NIO','MCD','TSM','TSLA','SQ','ROKU','PLTR','PYPL','ABNB']
strikedate = "2021-02-19"
TYPE = "put"
filename = strikedate+"_"+TYPE+".xlsx"

gc = gspread.service_account(filename='./credentials.json')
sh = gc.open('options_trading_'+strikedate)
#sh = gc.create('options_trading_'+strikedate)

sh.share('yuan.huang10@gmail.com', perm_type='user', role='writer')
sh.share('minshichen@gmail.com', perm_type='user', role='writer')
sh.share('yixianwen@gmail.com', perm_type='user', role='writer')



for ticker in tickers:
    data = getOptionsTable(ticker, strikedate, TYPE)
    data['lastTradeDate'] = data['lastTradeDate'].dt.strftime('%Y%m%d%H%M%S')
    data = data.replace(np.nan, '')
    sheetname = ticker+'_'+TYPE
    #worksheet=sh.add_worksheet(sheetname,rows='100',cols='20')
    worksheet = sh.worksheet(sheetname)
    worksheet.update([data.columns.values.tolist()] + data.values.tolist())

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