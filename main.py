#!/usr/local/bin/python3
from util import *

tickers = ['DAL','MSFT','AAPL','NVDA','FB','ADBE','HD','AMD','MA']
strikedate = "2021-02-05"
TYPE = "put"
filename = strikedate+".xlsx"

with pd.ExcelWriter(filename) as writer:
    for ticker in tickers:
        print(ticker)
        data = getOptionsTable(ticker, strikedate, TYPE)
        sheetname = ticker+'_'+TYPE
        print(sheetname)
        data.to_excel(writer,sheet_name=sheetname)